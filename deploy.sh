#!/bin/bash
set -e

echo "[Task 1] DONE"

# Task 2
cat << 'MD_EOF' > applications/roche_biostatistician_penzberg/VERIFICATION_REPORT.md
## CV ↔ Praktikumsbestätigung cross-check

| # | Claim | CV value | Certificate value | Match |
|---|---|---|---|---|
| 1 | Internship start date | 02/2026 | 02. Februar 2026 | PARTIAL |
| 2 | Internship end date | 04/2026 | 15. April 2026 | PARTIAL |
| 3 | Pipeline line count BEFORE refactor | 1.834 | 1.834 | YES |
| 4 | Pipeline line count AFTER refactor | 1.349 | 1.349 | YES |
| 5 | Percent reduction | -26,5% | über 26% | PARTIAL |
| 6 | Hardcoded correction rules → CSV | 257 | 241 | NO |
| 7 | Success criteria → separate config | Not found | 16 | NO |
| 8 | Deprecated function calls replaced | 360 | 360 | YES |
| 9 | Files touched by deprecation replacement | 4 | 4 | YES |
| 10 | Utility functions extracted to R-package | 9 | 9 | YES |
| 11 | Bugs discovered & documented | 2 | 2 | YES |
| 12 | Intervention types (Erfolg/Teilerfolg/Misserf) | Not found | 26 | NO |
| 13 | Registry scale (entries/year) | 143.000+ | ca. 150.000 | NO |
| 14 | Number of contributing clinics | ~300 | etwa 300 | PARTIAL |
| 15 | R-package name | degirtools | (not in cert) | N/A |
| 16 | Registry name (DeGIR) | DeGIR | (not in cert) | N/A |
MD_EOF

echo "[Task 2] DONE"
echo "Matches != YES:"
echo "Row 1: PARTIAL"
echo "Row 2: PARTIAL"
echo "Row 5: PARTIAL"
echo "Row 6: NO"
echo "Row 7: NO"
echo "Row 12: NO"
echo "Row 13: NO"
echo "Row 14: PARTIAL"

# Task 3
echo ""
echo "Discrepancy 1: CV says \"02/2026\" — certificate says \"02. Februar 2026\"."
echo "Discrepancy 2: CV says \"04/2026\" — certificate says \"15. April 2026\"."
echo "Discrepancy 3: CV says \"-26,5%\" reduction — certificate says \"über 26%\"."
echo "Discrepancy 4: CV says \"257 hardcodierten Korrekturregeln\" sum — certificate says \"241 Korrekturregeln + 16 Erfolgskriterien\"."
echo "Discrepancy 5: CV has no mention of success criteria separate count — certificate says \"16 Erfolgskriterien\"."
echo "Discrepancy 6: CV has no mention of 26 Intervention types — certificate says \"26 Interventionstypen\"."
echo "Discrepancy 7: CV says \"143.000+\" — certificate says \"ca. 150.000\"."
echo "Discrepancy 8: CV says \"~300\" — certificate says \"etwa 300\"."
echo "[Task 3] DONE"
