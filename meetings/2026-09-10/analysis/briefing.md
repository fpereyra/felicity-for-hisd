# Briefing — HISD Regular Board Meeting, 2026-09-10

## Big picture
The agenda packet could not be retrieved: this session's network policy blocks houstonisd.legistar.com and every news, HISD, and TEA domain, so **nothing in this briefing describes what the board is voting on tonight**. The strongest live thread is special education: the state found the district out of compliance in July, reporting says corrective action is due October 9, and the superintendent and commissioner have both tied the end of the takeover to this exact issue. The district has real, concede-able gains in the August ratings (a second B year, Wheatley's first A). The one question that requires a numeric answer tonight, and that no packet is needed to ask, is how many reassigned special-education students had a family meeting before they moved.

## Packet status: NOT ACQUIRED
- Target: `https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F` (supplied by trustee; also the calendar page).
- Result: `curl: (56) CONNECT tunnel failed, response 403` from the egress proxy; the calendar scraper failed the same way. Full log in `acquisition_log.md`.
- Side channels checked: no packet on the git remote, in Google Drive (PDFs since Sept 1), or as a Gmail attachment (35 days).
- Per the runbook, no inventory, redline, quantitative, or flag analysis was attempted. Phases 3–6 are not started.
- **To unblock:** allow `houstonisd.legistar.com` (and `*.legistar1.com`) in the environment's egress policy, then run `scripts/fetch_calendar.py --years 2025 2026` and `scripts/fetch_packet.sh 2026-09-10`. Alternatively commit the PDF to `meetings/2026-09-10/packet/AgendaPacket.pdf` on this branch.

## Item inventory
Not available. Community Voices for Public Education states the agenda has items 1–18 and is mobilizing on libraries, Grimes Park, and a curriculum for students with disabilities. That is an advocacy characterization and is **not** an inventory.

## Flags (ranked by strength)
No packet-based flags. News-derived candidates to test the moment the packet is in:
1. **Oversight-reducing / procedurally irregular:** any item touching the Grimes Park lease termination or the Southside Launchpad project. Check whether it is on consent, whether a prior authorization is cited, and the funding source.
2. **Inequitable / contrary to research:** any item adopting a district-built curriculum for STAAR-Alt students (reported from leaked slides). Check for evidence of field testing, alignment review, and who approved it.
3. **Oversight-reducing:** any special-education monitoring report. Check for blank ARD/IEP-meeting counts or "in progress" fields; that is the exact data the state's October deadline turns on.
4. **Anti-teacher / inequitable:** any librarian or library-services staffing item.
5. **Procedurally irregular:** any 1882 partnership contract amendment (June re-approval after TEA found missing details establishes the pattern).

## News (window 2026-08-06 → 2026-09-10; headline/snippet level only)
- **Ratings (Aug 13–14):** HISD held a B for a second year; Wheatley earned its first A; reported campus distribution 92 A / 113 B / 46 C / 9 D / 5 F / 7 not rated (verify). One source says Miles referred to four F elementaries; resolve the 4-vs-5 discrepancy on TXschools before quoting.
- **Takeover exit (Aug 14–late Aug):** Morath: "relatively soon." Miles: expects end after 2026-27; Morath decision expected June 2027. Reported exit criteria: no consecutive D/F campuses, improved board governance, SPED compliance. Three campuses reportedly had back-to-back D/F.
- **Special education (letter July 7; coverage into August):** TEA letter says changes violate student rights; ordered IEP reviews, family meetings before moves, training; monthly reports; Oct 9 deadline with possible further sanctions; conservators directed to review the ~5,000-student plan. District said meetings "as needed" during the year. OCR investigation opened in May; status unknown.
- **Grimes Park / Southside Launchpad (Aug–Sept):** HISD ended lease early; City removing ~$1.3M of improvements; council members questioned the arrangement. Project figures (~$100M, 2028) come only from a construction listing and are not citable.
- **Miles consulting (Aug):** Texas Observer: Miles cancelled a paid Third Future Schools agreement after the Observer obtained it; ~$190K over three years reported.
- **Workforce (Texas Monthly, Aug issue):** ~1/3 of teachers left in each of two post-takeover years; first-year teachers up ~65%; >20% uncertified at start of 2025-26. Verify denominators.
- **Meals (Community Impact, Aug):** 33 campuses not automatically on free meals in 2026-27.
- **Advocacy:** CVPE calling speakers for tonight on libraries, Grimes Park, disability curriculum.
- **Not found in window:** new litigation, new TEA orders beyond ratings, a Chronicle agenda preview.

Full source table: `../news/sources.md`. Tagged claims and the say/attribute/do-not-say lists: `claim_ledger.md`.

## Verification notes
**Confirmed directly:** nothing. No primary document was opened in this session.
**Confirmed at headline level (named outlet's headline states it):** TEA letter says SPED changes violate student rights (HPM); Morath "relatively soon" (Chronicle, HPM); Miles expects end after this year (Chronicle, Houston Press); HISD stays at B (K-12 Dive); OCR investigation opened (HPM, Texas Tribune); Grimes Park lease ended and $1.3M removal (ABC13); Miles cancelled Third Future contract (Texas Observer); $2B budget / $25M deficit (Chronicle); 1882 contracts re-approved after missing details (Chronicle).
**Snippet-level only (attribute, verify before asserting):** July 7 date; October 9 deadline; the three ordered actions; ~5,000 students; rating counts; three consecutive-D/F campuses; Texas Monthly workforce figures; 33 CEP campuses; pay bands.
**Could not access:** Legistar (packet, calendar, prior packets); houstonisd.org; tea.texas.gov; all news domains; CVPE's Sept 10 post.
**Longitudinal baseline:** none exists in this repo. This is the first meeting archived; the "recurring pattern" tracking starts with the next run.
