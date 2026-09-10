# Quantitative verification — 2026-09-10

All arithmetic reproducible from `packet.txt` page numbers cited. Chart values were read from rendered PNGs (`../pages/MON-*.png`), not from text extraction.

## A. Contract ceilings
| Item | "Amount not to Exceed" | Source |
|---|---|---|
| 13 CTE certifying agencies, 4 school years, fund 199 (general fund) | **$1,500,000.00** | p116 |
| 15 vendor awards: 3 vendor-name-change amendments (23-05-06 J-1 visa teacher program; 23-06-08 drug/alcohol testing; 23-10-08 awards/promo) | N/A each → **$0 new** | pp125–127 |
| **Total new ceilings** | **$1,500,000**; item 13 = 100% | |

## B. HUB codes (item 15)
| Vendor | HUB |
|---|---|
| GeoVisions Inc. dba Teacher Lounge (J-1 exchange-visitor teachers "to meet critical shortage teaching needs") | **C-D** (good-faith effort, 0% commitment) |
| Zenith Health Network dba Unif Health | B-25% |
| iPROMOTEu.com dba Top Tier Branding | A-100% |
C-D: 1 of 3. No cooperative purchases this month.

## C. Item 14 library titles by campus (pp119–123)
Parsed 337 rows with a level and posting dates. Campus classification from HISD's own GIS layer "All HISD Schools and Facilities" (services7.arcgis.com, owner demographics_HoustonISD, queried 2026-09-10; fields NES_Flag, Is_Title_I_Schoolwide, Board_Me_1, Rating_2025/2026, *_Current ethnicity counts).

| Campus | Titles | Share | Trustee district | NES | Title I schoolwide | Magnet | 2025→2026 rating | Enrollment | White / Hispanic / Black |
|---|---|---|---|---|---|---|---|---|---|
| Shearn ES | 139 | 41.2% | IV | Not-NES | Yes | No | C → B | 451 | 1% / 65% / 29% |
| Pin Oak MS | 95 | 28.2% | V | Not-NES | No | Yes | A → A | 1,280 | 29% / 37% / 11% |
| Field ES | 64 | 19.0% | **I** | Not-NES | Yes | No | A → A | 560 | 30% / 53% / 7% |
| Briarmeadow Charter | 22 | 6.5% | VII | Not-NES | Yes | No | A → A | 621 | 19% / 25% / 14% |
| Baker Montessori | 9 | 2.7% | VII | Not-NES | No | Yes | B → B | 643 | 23% / 41% / 10% |
| Oak Forest ES | 6 | 1.8% | II | Not-NES | No | Yes | A → A | 996 | 45% / 20% / 4% |
| Horn ES | 2 | 0.6% | V | Not-NES | No | No | A → A | 752 | 28% / 17% / 7% |

District denominators (same layer, 255 regular instructional campuses): NES 121/255 = **47.5%**; Title I schoolwide 230/255 = **90.2%**; student ethnicity White **10%**, Hispanic 58%, Black 19% (N = 152,793 current counts).
- Receiving campuses that are NES: **0 of 7** (expected under proportional allocation ≈ 3.3).
- Receiving campuses not Title I schoolwide: **4 of 7** (57%) vs 10% districtwide.
- Six of seven have White enrollment share 2–4.5× the district's 10%; Shearn (1%) is the exception and receives the most titles.
- Caveat: n = 7 campuses in one month; "Is_CEP" is unpopulated in the layer, so economic disadvantage is proxied by Title I schoolwide status only. August 13's library item (its item 17) is tabulated below for a second data point.

**August 13, 2026 list (item 17 of that packet), same method — 367 titles, 7 campuses:**

| Campus | Titles | Trustee district | NES | Title I schoolwide | Magnet | 2025→2026 | Enrollment | White / Hispanic / Black |
|---|---|---|---|---|---|---|---|---|
| West University ES | 173 | V | Not-NES | No | No | A → A | 1,195 | 53% / 16% / 3% |
| Baker Montessori | 78 | VII | Not-NES | No | Yes | B → B | 643 | 23% / 41% / 10% |
| Field ES | 65 | I | Not-NES | Yes | No | A → A | 560 | 30% / 53% / 7% |
| Briarmeadow Charter | 21 | VII | Not-NES | Yes | No | A → A | 621 | 19% / 25% / 14% |
| Sinclair ES | 13 | VIII | Not-NES | No | Yes | B → A | 785 | 38% / 31% / 8% |
| Lovett ES | 11 | V | Not-NES | Yes | Yes | B → A | 655 | 18% / 37% / 29% |
| Oak Forest ES | 6 | II | Not-NES | No | Yes | A → A | 996 | 45% / 20% / 4% |

Two months combined: 704 titles, 10 distinct campuses (Field, Briarmeadow, Baker, Oak Forest appear both months), **0 NES**, 5 of 10 not Title I schoolwide. Under the district's 47.5% NES share, the chance that 10 independently drawn campuses are all non-NES is about 0.525^10 ≈ 0.2%; the campuses are not independent draws (librarian staffing determines participation), which is the point.

- Mechanism, not inference: book orders are campus-initiated ("Campus Submission — Librarians submit book orders", p117). Librarian positions were eliminated at NES campuses in 2023 (KPRC 2023-07-26; ABC13; Chronicle). A campus without a librarian does not appear in this approval item. The monthly SB 13 list is therefore a running census of where library service still operates.

## D. Item 10 pre-K partnership sites (pp100–101)
10 centers. Actual enrollment sums to 57 (matches packet total); projected sums to 193 (matches). Actual/projected = **29.5%**. Three centers show **0** actual (Visionary Pre-K at Regency Lofts, Laugh N Discover, Precious Moments). Which centers are the "additional sites" is not marked; no prior Appendix 8 appears in the March 19, March 26, June 25, or August 13 packet text, so the delta cannot be computed. Cost line reads "None."

## E. Item 11 GPM target changes (pp103–105) vs current language (pp16–17, 50) and achieved values (Figs 27, 30)
| GPM | Current | Achieved (EOY 23-24, 24-25, 25-26) | Proposed 2026–2028 | Effect |
|---|---|---|---|---|
| 4.1 SWD reading growth | 48% (Jun 2024) → 55% (Jun 2028) | 48, **58**, **56** | "remain at 55 percent or above" | Growth target becomes a floor **1 pt below current (56) and 3 below 2024-25 (58)** |
| 4.2 SWD math growth | 46% → **58%** (Jun 2028) | 39, **51** | 51% (May 2026) → **55%** (Jun 2028) | 2028 target **lowered 3 pts**; required pace falls from 3.5 to 2.0 pts/yr |
| 4.3 SWD projected Meets (new) | temporarily removed Nov 2025 | — | 30% → 36% (May 2028) | reinstated at a lower base than the May 2025 language (27% → 35%) |
| Goal 3 | 26% (2026-27 grads) | 28% (class of 2025) | 34% (2026-27 grads) | raised |
| 1.1 / 1.2 (NES) reading projected Meets | — | — | 52→58 / 43→49 | NES gap 9 pts held constant |
| 2.1 / 2.2 (NES) math | — | — | 42→48 / 36→42 | NES gap 6 pts held constant |
Cover sheet (p102) lists the affected measures as "1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.4, 3.5, and 4.3" — **4.1 and 4.2 are omitted from the cover but changed in the attachment.** The November 2025 proposal (Nov packet p96) stated 4.1 and 4.2 "already measure Met Expected Growth and do not require revision."

## F. Constraint 2.1 — initial ARD timeliness (p70, Fig 35)
Values: 87.2 (22-23), 99.7, 99.9, **97.7 (25-26)**. Constraint text: "maintain 100-percent compliance through June 2028." Status label: **"In Progress."** Key takeaway: "Over 3,700 initial ARDs were held within compliant timelines." Implied: if ~3,700 compliant at 97.7%, total ≈ 3,787 and **≈ 87 initial ARDs missed the federal timeline** (range 87–92 for 3,700–3,900 compliant). Footnote: "Preliminary SPP submission data, subject to change."

## G. Goal 4 and GPM 4.2 framing (pp51–52, 59–60)
- Fig 24: achieved 63, 66, 68, 69 vs targets 64, 66, 72, 76, 78 → 2025-26 missed by 3; status Not Met. Takeaway: "More than half… continue to demonstrate growth."
- Fig 25: Black SWD 65 → 67 = +2 pts; takeaway says "3% higher" (relative: +3.1%). Asian* 76 → 68 and Two+* 74 → 65 (small n, flagged *).
- Fig 30: 39 → 51; takeaway "**increased by 31%** year over year" = (51−39)/39 = 30.8% relative; absolute +12 pts. Footnote on the same slide: "NWEA MAP Growth results in 24-25 do not include EISA algorithm. All data presented using 2025 norms; may not match prior presentations."
- Item 11 cover (p102): NWEA's 2025 changes made it "necessary to re-establish baselines to ensure accurate year-over-year comparisons and prevent misinterpretation of progress."
- Fig 10 (p29): NES 11th-grade TSI 6 → 9 = +3 pts, takeaway "increased… by 50%"; EAS 28 → 28; All 20 → 22.
- Fig 12 (p32): 12th-grade CTE on-track **38 → 27** (definition now requires an IBC); takeaway cites 10th and 11th grades only.

## H. Constraint 1 (p67, Fig 33; p68, Fig 34)
D/F total 37 (2024), 17 (2025), 13 (2026 preliminary); multi-year 5, 0, 0. A/B campuses 93 → 170 → 198 → 205. HPM 08-14 (from article text): 92 A, 113 B, 46 C, **9 D, 5 F**, 7 not rated of 272 → 14 D/F vs the packet's 13. HPM 08-17: the five F campuses "passed last year or were unrated," so no multi-year designation — consistent with the packet's zero.

## I. Investment report (p76), market value 6/30/2025 → 6/30/2026
| Fund | 2025 | 2026 | Δ |
|---|---|---|---|
| General Fund | 1,039,420,550 | 931,406,517 | **−108,014,033 (−10.4%)** |
| Capital Projects | 46,950,382 | 91,860,022 | +44,909,640 |
| Debt Service | 166,877,534 | 187,289,982 | +20,412,448 |
| Child Nutrition | 40,587,567 | 28,327,928 | −12,259,639 (−30.2%) |
| Activity | 29,639,714 | 26,832,889 | −2,806,825 |
| **Total** | 1,323,475,747 | 1,265,717,338 | **−57,758,409 (−4.4%)** |
Header on p75 reads "July 1, 2027 – June 30, 2026" and "July 2025 – June 20026."

## J. Monitoring calendar diff — see `redlines.md` (item 7). Months with no goal report: 2 → 3; dedicated GPM 3.2 report removed; April prior-year Constraint 1 check removed.

## K. Blank / placeholder data
None found ("awaiting data", "TBD", empty series) in items 3–4. Superintendent's "Special Education Success Program Update" has **no attachment at all** (agenda p2; no other mention in 136 pages).
