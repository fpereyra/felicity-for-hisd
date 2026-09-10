#!/usr/bin/env bash
# Render packet pages to PNG for redline reading (pdftotext drops strike/underline).
# Usage: scripts/render_pages.sh DATE CODE START END [DPI=130]
set -euo pipefail
DATE=$1; CODE=$2; S=$3; E=$4; DPI=${5:-130}
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/meetings/$DATE/pages"
pdftoppm -f "$S" -l "$E" -r "$DPI" -png "$ROOT/meetings/$DATE/packet/AgendaPacket.pdf" "$ROOT/meetings/$DATE/pages/$CODE"
ls "$ROOT/meetings/$DATE/pages/$CODE"*
