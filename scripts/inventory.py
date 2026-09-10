#!/usr/bin/env python3
"""First-pass agenda inventory from `pdftotext -layout` output.

Usage: python3 scripts/inventory.py meetings/DATE/analysis/packet.txt > meetings/DATE/analysis/inventory_draft.md

Pages are delimited by form feeds in pdftotext output. The script locates
candidate item headers, `(LOCAL)` policy codes, dollar figures, and
consent/closed-session markers per page. It is a locator, not the answer:
every row must be hand-verified against the packet, and redline content
must come from rendered page images, never from this text.
"""
import re, sys
from collections import OrderedDict

txt = open(sys.argv[1], encoding="utf-8", errors="replace").read()
pages = txt.split("\f")
ITEM = re.compile(r"^\s*((?:[A-Z]-\d+|[A-Z]\.\s*\d*|\d+\.)\s+.{8,120})$", re.M)
POLICY = re.compile(r"\b([A-Z]{2,4})\s*\((?:LOCAL|LEGAL)\)")
MONEY = re.compile(r"\$\s?\d{1,3}(?:,\d{3})+(?:\.\d{2})?")
NTE = re.compile(r"(?:not[\s-]+to[\s-]+exceed|NTE)\s*(?:amount|of)?[:\s]*\$?\s?(\d{1,3}(?:,\d{3})+(?:\.\d{2})?)", re.I)
FLAGS = {
    "consent": re.compile(r"consent\s+agenda", re.I),
    "closed": re.compile(r"closed\s+session|executive\s+session|§\s*551\.\d+|Section\s+551\.", re.I),
    "second_reading": re.compile(r"second\s+reading", re.I),
    "first_reading": re.compile(r"first\s+reading", re.I),
    "HUB": re.compile(r"\bHUB\b", re.I),
    "awaiting": re.compile(r"awaiting\s+data|data\s+not\s+available|TBD|placeholder", re.I),
}
print("| page | candidate header / policy | $ (max on page) | NTE | markers |\n|---|---|---|---|---|")
for i, p in enumerate(pages, 1):
    heads = [h.strip() for h in ITEM.findall(p)][:2]
    pols = sorted(set(POLICY.findall(p)))
    money = MONEY.findall(p); nte = NTE.findall(p)
    marks = [k for k, rx in FLAGS.items() if rx.search(p)]
    if not (heads or pols or nte or marks):
        continue
    mx = max((float(m.replace("$", "").replace(",", "").strip()) for m in money), default=0)
    print(f"| {i} | {' / '.join(heads + [f'`{c} (LOCAL)`' for c in pols])[:110]} | {mx:,.0f} | {', '.join(nte)} | {', '.join(marks)} |")
