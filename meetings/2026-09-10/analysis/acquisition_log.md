# Acquisition log — 2026-09-10 packet

- 2026-09-10T20:21:00Z attempting packet download from https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F
- 2026-09-10T20:21:00Z curl FAILED (exit 0) for https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F — if exit 56/000 via proxy, the egress policy is blocking houstonisd.legistar.com
- 2026-09-10T20:21:23Z scripts/fetch_calendar.py --years 2025 2026 -> urllib.error.URLError: Tunnel connection failed: 403 Forbidden (proxy egress policy; houstonisd.legistar.com not allowlisted)
- 2026-09-10T20:21:23Z side channels checked: origin branch has no packet commit; Google Drive has no PDFs modified since 2026-09-01; Gmail has no packet attachment in last 35 days
- 2026-09-10T20:21:24Z attempting packet download from https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F
- 2026-09-10T20:21:24Z curl FAILED http=000 for https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F :: curl: (56) CONNECT tunnel failed, response 403
 (403 'CONNECT tunnel failed' = egress policy blocking houstonisd.legistar.com)
- 2026-09-10T20:44:40Z attempting packet download from https://houstonisd.legistar.com/View.ashx?M=PA&ID=1315010&GUID=0BAA0864-ABEE-4DAC-86F6-80CD2882F80F
- 2026-09-10T20:44:44Z OK pages=136 bytes=13490224 sha256=7a70bd93186cad53c644e219d9bc27a507c7e001011a7fcdb9086161f7eeb1d7 created='Wed Sep  9 15'
