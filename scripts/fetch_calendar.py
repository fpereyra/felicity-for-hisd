#!/usr/bin/env python3
"""Scrape the HISD Legistar calendar into meetings/calendar.{json,md}.

Usage: python3 scripts/fetch_calendar.py [--years 2025 2026 ...] [--out meetings]

Stdlib only. For each meeting row captures: date, time, name, location,
meeting-detail URL, and the View.ashx links: agenda (M=A), packet (M=PA),
minutes (M=M), plus video if present.

Legistar's year selector is an ASP.NET postback; we replay it with the
page's __VIEWSTATE tokens. If the postback fails we fall back to whatever
the default GET view shows and say so on stderr.
"""
import argparse, html, json, re, sys, urllib.parse, urllib.request
from datetime import datetime
from html.parser import HTMLParser

BASE = "https://houstonisd.legistar.com/"
CAL = BASE + "Calendar.aspx"
UA = {"User-Agent": "Mozilla/5.0 (felicity-for-hisd briefing bot)"}


def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


class RowParser(HTMLParser):
    """Collect <tr> rows as lists of (text, hrefs) cells."""
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell, self.hrefs = [], None, None, None
        self.in_td = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell, self.hrefs, self.in_td = [], [], True
        elif tag == "a" and self.in_td and a.get("href"):
            self.hrefs.append(html.unescape(a["href"]))
    def handle_data(self, d):
        if self.in_td:
            self.cell.append(d)
    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.in_td:
            self.row.append((" ".join("".join(self.cell).split()), self.hrefs))
            self.in_td = False
        elif tag == "tr" and self.row is not None:
            if self.row:
                self.rows.append(self.row)
            self.row = None


def parse_rows(page):
    p = RowParser(); p.feed(page)
    out = []
    for row in p.rows:
        allhrefs = [h for _, hs in row for h in hs]
        if not any("MeetingDetail.aspx" in h for h in allhrefs):
            continue
        texts = [t for t, _ in row]
        rec = {"name": "", "date": "", "time": "", "location": ""}
        for t in texts:
            if not rec["date"] and re.fullmatch(r"\d{1,2}/\d{1,2}/\d{4}", t):
                rec["date"] = datetime.strptime(t, "%m/%d/%Y").date().isoformat()
            elif not rec["time"] and re.fullmatch(r"\d{1,2}:\d{2} [AP]M", t):
                rec["time"] = t
        # name = text of the cell holding the MeetingDetail link
        for t, hs in row:
            if any("MeetingDetail.aspx" in h for h in hs):
                rec["name"] = t
                rec["detail_url"] = urllib.parse.urljoin(BASE, [h for h in hs if "MeetingDetail" in h][0])
        # location: the longest cell that isn't name/date/time and has no links
        cands = [t for t, hs in row if not hs and t not in (rec["date"], rec["time"]) and not re.fullmatch(r"\d{1,2}/\d{1,2}/\d{4}", t)]
        rec["location"] = max(cands, key=len) if cands else ""
        for h in allhrefs:
            u = urllib.parse.urljoin(BASE, h)
            q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
            m = (q.get("M") or [""])[0].upper()
            if "View.ashx" in u:
                key = {"A": "agenda_url", "PA": "packet_url", "M": "minutes_url",
                       "AADA": "agenda_ada_url", "PADA": "packet_ada_url"}.get(m)
                if key: rec[key] = u
            elif "Video.aspx" in u or "granicus" in u.lower():
                rec.setdefault("video_url", u)
        out.append(rec)
    return out


def hidden_fields(page):
    return dict(re.findall(r'<input type="hidden" name="(__[A-Z]+)"[^>]*value="([^"]*)"', page))


def fetch_year(year, base_page):
    """Replay the year-dropdown postback. Returns page HTML or None."""
    hid = hidden_fields(base_page)
    if "__VIEWSTATE" not in hid:
        return None
    sel = re.search(r'name="(ctl00\$ContentPlaceHolder1\$lstYears)"', base_page)
    if not sel:
        return None
    form = dict(hid)
    form["__EVENTTARGET"] = sel.group(1)
    form["__EVENTARGUMENT"] = ""
    form[sel.group(1)] = str(year)
    # Telerik combobox mirrors the value in a *_ClientState field
    cs = re.search(r'name="(ctl00\$ContentPlaceHolder1\$lstYears_ClientState)"', base_page)
    if cs:
        form[cs.group(1)] = json.dumps({"logEntries": [], "value": str(year), "text": str(year), "enabled": True})
    try:
        return get(CAL, urllib.parse.urlencode(form).encode())
    except Exception as e:  # noqa
        print(f"[warn] postback for {year} failed: {e}", file=sys.stderr)
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int, default=[])
    ap.add_argument("--out", default="meetings")
    a = ap.parse_args()
    try:
        base = get(CAL)
    except Exception as e:
        sys.exit(f"[fatal] cannot reach {CAL}: {e} (403 tunnel = egress policy block)")
    recs = parse_rows(base)
    for y in a.years:
        pg = fetch_year(y, base)
        if pg:
            recs += parse_rows(pg)
        else:
            print(f"[warn] could not load year {y}; using default view only", file=sys.stderr)
    # dedupe on detail_url
    seen, uniq = set(), []
    for r in recs:
        k = r.get("detail_url") or (r["date"], r["name"])
        if k not in seen:
            seen.add(k); uniq.append(r)
    uniq.sort(key=lambda r: (r["date"], r["time"]))
    meta = {"source": CAL, "retrieved_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z", "count": len(uniq)}
    with open(f"{a.out}/calendar.json", "w") as f:
        json.dump({"meta": meta, "meetings": uniq}, f, indent=1)
    with open(f"{a.out}/calendar.md", "w") as f:
        f.write(f"# HISD Legistar calendar\n\nSource: {CAL}  \nRetrieved: {meta['retrieved_utc']}  \nMeetings: {len(uniq)}\n\n")
        f.write("| Date | Time | Meeting | Agenda | Packet | Minutes |\n|---|---|---|---|---|---|\n")
        for r in uniq:
            L = lambda k: f"[link]({r[k]})" if r.get(k) else ""
            f.write(f"| {r['date']} | {r['time']} | {r['name']} | {L('agenda_url')} | {L('packet_url')} | {L('minutes_url')} |\n")
    print(f"wrote {len(uniq)} meetings to {a.out}/calendar.{{json,md}}")


if __name__ == "__main__":
    main()
