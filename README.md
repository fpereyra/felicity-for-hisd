# felicity-for-hisd

Working repository for board-meeting briefings for Felicity Pereyra, elected HISD Trustee, District I.

## Layout
```
meetings/
  calendar.{json,md}          # scraped Legistar calendar (all meetings, links)
  YYYY-MM-DD/
    packet/AgendaPacket.pdf   # combined agenda packet + manifest.txt (URL, timestamp, SHA256)
    pages/                    # pdftoppm renders of policy redlines (read images, not text)
    analysis/                 # inventory, redlines, verification, flags, briefing, ledger, remarks
    news/sources.md           # news sweep sources for the lookback window
scripts/
  fetch_calendar.py           # Legistar calendar -> meetings/calendar.{json,md}
  fetch_packet.sh DATE [URL]  # download + validate packet, write manifest, log attempts
  render_pages.sh DATE CODE S E   # render pages S..E to pages/CODE-*.png
  inventory.py packet.txt     # first-pass item locator from pdftotext output
  verify.py packet.txt [--pages A-B]   # NTE sums, largest award share, HUB tally
hisd_d1.geojson               # District I boundary
```

## Run order
1. `python3 scripts/fetch_calendar.py --years 2025 2026`
2. `scripts/fetch_packet.sh 2026-09-10` (add the packet URL as a second argument to bypass the calendar)
3. Commit the packet before analysis.
4. `pdftotext -layout meetings/DATE/packet/AgendaPacket.pdf meetings/DATE/analysis/packet.txt`
5. `python3 scripts/inventory.py ...` then hand-verify; render every `(LOCAL)` policy with `render_pages.sh` and read the images.
6. `python3 scripts/verify.py ...` and paste output into `analysis/verification.md`.

## Requirements
- `poppler-utils`, `qpdf`, Python 3 (stdlib only).
- Outbound access to `houstonisd.legistar.com` and `*.legistar1.com`. If the fetch scripts log `CONNECT tunnel failed, response 403`, the environment's egress policy is blocking Legistar; allow those hosts or commit the PDF manually to `meetings/DATE/packet/AgendaPacket.pdf`.

## Rules that travel with the analysis
- `pdftotext` drops strikethrough and underline. Redline content comes only from rendered page images.
- Every number in a briefing traces to printed arithmetic in `analysis/verification.md`.
- Claims are tagged `[DOC]`, `[REPORTED]`, `[DISTRICT]`, `[ADVOCACY]`, `[UNVERIFIED]`. Nothing untagged gets spoken.
