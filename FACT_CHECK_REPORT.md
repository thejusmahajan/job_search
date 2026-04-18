## FACT-CHECK REPORT — 2026-04-18

### CONFLICTS FOUND

| # | Item | Source A (value) | Source B (value) | Recommended Canonical Value | Justification |
|---|---|---|---|---|---|
| 1 | Deprecated Function Call Count | `cv_english.tex` / `CV_Mahajan.pdf` (357) | `05_directive_d4.md` / `16_metrics.md` / `01_executive_summary.md` (360) | 360 | The `work_done_during_internship/` directory is the authoritative source for internship accomplishments. `05_directive_d4.md` breaks down the 360 calls exactly (19 + 53 + 187 + 15 + 86). |
| 2 | Internship Date Range | `skills_and_experience.md` (Feb 3 – Apr 30, 2026) | `01_executive_summary.md` (Feb 2 – Apr 15, 2026) | Feb 2 – Apr 15, 2026 | `skills_and_experience.md` is a stale snapshot from March 7, 2026. `01_executive_summary.md` represents the final, verified duration. Additionally, `02/2026 - 04/2026` aligns with ground truth PDFs. |
| 3 | Line Count Claims (import.R) | `cv_english.tex` / `CV_Mahajan.pdf` (1,348 lines) | `01_executive_summary.md` / `16_metrics.md` (1,349 lines) | 1,349 | `work_done_during_internship/` files are the authoritative source for project metrics, all correctly indicating 1,349 lines. |

### ALL CHECKS PASSED

| # | Item | Value | Sources Verified |
|---|---|---|---|
| 1 | HealthTwiSt Internship Dates | 02/2026 - 04/2026 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 2 | CQ Beratung Education Dates | 08/2025 - 02/2026 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 3 | Guest Scientist Hereon Dates | 05/2025 - 10/2025 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 4 | Job Search Dates | 02/2025 - 04/2025 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 5 | Post-doc Hamburg Dates | 08/2021 - 01/2025 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 6 | Career Transition Dates | 04/2021 - 07/2021 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 7 | Physics Tutor Dates | 10/2018 - 03/2021 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 8 | PhD Paris-Saclay Dates | 10/2015 - 09/2018 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 9 | Research Project IIT Mandi Dates | 02/2015 - 08/2015 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 10 | M.Sc. NIT Calicut Dates | 07/2012 - 12/2014 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 11 | B.Sc. Calicut Dates | 06/2009 - 04/2012 | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 12 | global.R line count reduction | 767 to 70 (-91%) | `16_metrics.md`, `cv_english.tex` |
| 13 | Dashboard line count | 1,468 lines across 10 files | `16_metrics.md`, `08_degir_dashboard.md` |
| 14 | Tidymodels line count | 302 lines | `16_metrics.md`, `09_tidymodels.md` |
| 15 | Publications List | 5 items identical in details | `CV_Mahajan.pdf`, `cv_english.tex` |
| 16 | Language Proficiency (English) | Fluent (C1) | `CV_Mahajan.pdf`, `cv_english.tex` |
| 17 | Language Proficiency (German) | B1 Goethe, B2 in preparation | `CV_Mahajan.pdf`, `cv_english.tex`, `personal_data_and_grades.md` |
| 18 | M.Sc. Degree Grade | First Class with Distinction (CGPA 8.71/10) | `CV_Mahajan.pdf`, `personal_data_and_grades.md` |
| 19 | B.Sc. Degree Grade | B+ (CGPA 3.49/4.0) | `CV_Mahajan.pdf`, `personal_data_and_grades.md` |
| 20 | PhD Grade | No grade mentioned | `CV_Mahajan.pdf`, `personal_data_and_grades.md` |

### STALE/OUTDATED SOURCES

| File | Why It's Stale | Safe to Use For |
|---|---|---|
| `reference/skills_and_experience.md` | Snapshotted on March 7, 2026. Metrics report 5 of 21 weeks completed and 2 of 4 directives. Final metrics are 10.5 total weeks completed and 4 of 4 directives. | Descriptions of skills and domain knowledge, but NOT for timeline, progress metrics, or final completion numbers. |
