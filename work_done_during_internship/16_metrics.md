# Quantitative Metrics Summary

## Key Numbers for CV/Cover Letter

| Metric | Value |
|---|---|
| **Pipeline input size** | 143,143 rows × ~1,920 columns |
| **Pipeline output size** | 143,120 rows × 216 columns |
| **Main script reduction (D2+D3)** | 1,834 → 1,349 lines (−26.5%) |
| **global.R reduction (D1)** | 767 → 70 lines (−91%) |
| **Config files created (D3+D2)** | 8 CSVs, 257 total entries |
| **Deprecated calls replaced (D4)** | 360 sites across 4 files |
| **Functions extracted to package (D1)** | 9 functions, 859 lines |
| **Pre-existing bugs discovered** | 2 |
| **Verification checks passed** | Every commit — cumulative `identical()` = TRUE |
| **Dashboard modules** | 6 interactive modules |
| **Dashboard code** | 1,468 lines across 10 files |
| **Translation entries (i18n)** | 224 lines (DE/EN) |
| **Tidymodels script** | 302 lines |
| **Documentation pages** | 17 HTML visualizations + 30+ markdown documents |
| **Flashcards created** | 110 cards (3 levels, 3 types) |
| **Clinics served by pipeline** | ~300 German clinics |
| **Patient records processed/year** | ~143,000 |
| **Supervisor meetings** | 5 formal meetings |
| **Status emails sent** | 2 in German + multiple in English |
| **Presentations delivered** | 2 (interim 15 min + final 20 min) |
| **Pipeline runtime** | ~6 seconds (143K rows, 1,920 columns) |
| **Directives completed** | 4 of 4 (100%) |
| **Internship duration** | 10.5 weeks, 40 hrs/week |

## Deliverables Inventory

### Code Deliverables (pushed to collaborative repo)

| Deliverable | Branch |
|---|---|
| D3: 7 config CSVs | thejus/d3-config-extraction |
| D2: grade_complication() + success_criteria.csv | thejus/d3-config-extraction |
| D4: 360 deprecated replacements | thejus/d4-d1-modernization |
| D1: degirtools package (9 functions) | thejus/d4-d1-modernization |

### Standalone Projects

| Deliverable | Location |
|---|---|
| DeGIR Dashboard | github.com/thejusmahajan/degir-dashboard + shinyapps.io |
| Introduction to Tidymodels | github.com/thejusmahajan/Introduction_to_Tidymodels |
