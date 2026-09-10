#!/usr/bin/env bash
# Download + validate the combined agenda packet for a meeting date.
# Usage: scripts/fetch_packet.sh YYYY-MM-DD [PACKET_URL]
# Resolves the URL from meetings/calendar.json unless one is given.
# Writes meetings/DATE/packet/AgendaPacket.pdf and manifest.txt.
set -euo pipefail
DATE="${1:?meeting date YYYY-MM-DD}"; URL="${2:-}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/meetings/$DATE/packet"; mkdir -p "$DIR"
LOG="$ROOT/meetings/$DATE/analysis/acquisition_log.md"; mkdir -p "$(dirname "$LOG")"
ts() { date -u +%Y-%m-%dT%H:%M:%SZ; }
note() { echo "- $(ts) $*" | tee -a "$LOG"; }

if [[ -z "$URL" ]]; then
  [[ -f "$ROOT/meetings/calendar.json" ]] || { note "no calendar.json; run scripts/fetch_calendar.py or pass a URL"; exit 2; }
  URL=$(python3 - "$ROOT/meetings/calendar.json" "$DATE" <<'PY'
import json,sys
cal=json.load(open(sys.argv[1]))["meetings"]
rows=[m for m in cal if m["date"]==sys.argv[2] and m.get("packet_url")]
# prefer the regular board meeting over work sessions on the same date
rows.sort(key=lambda m: ("Regular" not in m["name"] and "Board Meeting" not in m["name"], m["time"]))
print(rows[0]["packet_url"] if rows else "")
PY
)
  [[ -n "$URL" ]] || { note "calendar.json has no packet link for $DATE"; exit 2; }
fi
note "attempting packet download from $URL"
OUT="$DIR/AgendaPacket.pdf"
ERR=$(curl -sSL --retry 3 --retry-delay 5 --max-time 900 -A "Mozilla/5.0 (felicity-for-hisd)" -w "%{http_code}" -o "$OUT.part" "$URL" 2>&1) || true
CODE="${ERR: -3}"
if [[ "$CODE" != "200" ]]; then
  note "curl FAILED http=$CODE for $URL :: ${ERR%???} (403 'CONNECT tunnel failed' = egress policy blocking houstonisd.legistar.com)"
  rm -f "$OUT.part"; exit 3
fi
head -c 5 "$OUT.part" | grep -q '%PDF' || { note "downloaded file is not a PDF (magic bytes)"; rm -f "$OUT.part"; exit 4; }
mv "$OUT.part" "$OUT"
PAGES=$(pdfinfo "$OUT" | awk '/^Pages:/{print $2}')
CREATED=$(pdfinfo "$OUT" | sed -n 's/^CreationDate: *//p')
SHA=$(sha256sum "$OUT" | cut -d' ' -f1)
SIZE=$(stat -c %s "$OUT")
MIN_PAGES="${MIN_PAGES:-20}"   # regular packets are >20 pages; set MIN_PAGES=1 for special-meeting packets
(( PAGES >= MIN_PAGES )) || { note "page count $PAGES < MIN_PAGES=$MIN_PAGES; refusing (partial packet?). Override with MIN_PAGES=1 if this is a short special-meeting packet."; rm -f "$OUT"; exit 5; }
cat > "$DIR/manifest.txt" <<M
file: AgendaPacket.pdf
meeting_date: $DATE
source_url: $URL
retrieved_utc: $(ts)
sha256: $SHA
bytes: $SIZE
pages: $PAGES
pdf_creation_date: $CREATED
M
note "OK pages=$PAGES bytes=$SIZE sha256=$SHA created='$CREATED'"
(( SIZE > 100*1024*1024 )) && note "WARNING: >100MB; enable Git LFS before committing" || true
