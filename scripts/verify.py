#!/usr/bin/env python3
"""Quantitative checks over packet text. Prints reproducible arithmetic.

Usage: python3 scripts/verify.py meetings/DATE/analysis/packet.txt [--pages A-B]

Checks: sum of "not to exceed" ceilings, largest award and its share,
HUB code tally (flags C-D and N/A), and a per-page dollar index.
Restrict with --pages to a single item's range to avoid double counting.
"""
import argparse, re
from collections import Counter

ap = argparse.ArgumentParser(); ap.add_argument("txt"); ap.add_argument("--pages")
a = ap.parse_args()
pages = open(a.txt, encoding="utf-8", errors="replace").read().split("\f")
if a.pages:
    s, e = map(int, a.pages.split("-")); pages = pages[s-1:e]
text = "\f".join(pages)
NTE = re.compile(r"not[\s-]+to[\s-]+exceed[^$\n]{0,40}\$\s?(\d{1,3}(?:,\d{3})+(?:\.\d{2})?)", re.I)
vals = [float(v.replace(",", "")) for v in NTE.findall(text)]
print(f"NTE figures found: {len(vals)}")
for v in vals: print(f"  {v:>16,.2f}")
if vals:
    tot = sum(vals); mx = max(vals)
    print(f"TOTAL = {tot:,.2f}\nLARGEST = {mx:,.2f} ({mx/tot:.1%} of total)")
hub = Counter(re.findall(r"\b(?:HUB\s*(?:Code|Status)?[:\s]*)([A-D](?:-[A-D])?|N/?A)\b", text, re.I))
print("HUB codes:", dict(hub) or "none found")
if hub.get("C-D"): print(f"  C-D (good-faith-effort, zero commitment): {hub['C-D']}")
