# Skills & Experience — DeGIR radioDB Project

**Who:** Thejus Mahajan, MSc Bioinformatics student
**Where:** HealthTwiSt GmbH, Berlin (internship under Dr. Andreas Busjahn)
**When:** Feb 3 – Apr 30, 2026 (ongoing, status as of Mar 7, 2026)
**What:** Refactoring a medical data pipeline for Germany's interventional radiology quality registry (DeGIR)
**Prior background:** Fortran, Python. No prior R experience. German B1, progressing to B2.
**LinkedIn:** https://www.linkedin.com/in/thejusmahajan/
**Google Scholar:** https://scholar.google.com/citations?hl=en&user=PJkZwAwAAAAJ

---

## How to use this file

This is a factual inventory of skills gained and demonstrated during the DeGIR radioDB project. Every entry has a concrete evidence line. An agent preparing a CV or cover letter should map entries from this file to the target job's requirements. Do not invent skills not listed here.

---

## 1. Programming — R / tidyverse

**Level:** Learned from scratch during this project. Now working-proficient.

| Package/feature | What I used it for | Evidence |
|---|---|---|
| dplyr (mutate, filter, case_when, select, group_by, summarise) | Core pipeline transformations on 143K-row dataset | Entire import.R refactoring |
| stringr (str_detect, str_replace_all) | Regex-based intervention label matching, title normalization | 27 regex patterns in intervention_label_mapping.csv |
| readr (read_csv, read_csv2) | Reading config CSVs and the main 143K-row data export | All 8 config CSV integrations |
| tidyr (spread/gather → pivot_wider/pivot_longer) | Studied for D4 deprecated function replacement (363 call sites) | D4 analysis in refactoring_guide |
| R function design | Wrote `grade_complication(data, slot, grade_cols)` — handles asymmetric inputs (K1: 4 columns, K2/K3: 1 column each) | import.R, commit f2c14a5 |
| R base (`identical()`, `Reduce()`, `lapply()`, `switch()`) | Byte-level pipeline verification; functional dispatch in config loops | Every extraction verified with identical() |

## 2. Programming — Other languages

| Language | Context | Evidence |
|---|---|---|
| Python | Prior experience (pre-internship) | Background |
| Fortran | Prior experience (pre-internship) | Background |
| Quarto / RMarkdown | Wrote tidymodels introduction (first assignment); PDF report generation | github.com/thejusmahajan/Introduction_to_Tidymodels; renderReport.R |
| Bash | Pipeline execution scripts, conda automation | run_script/render_reports.sh |

## 3. Data engineering

| Skill | What I did | Scale | Evidence |
|---|---|---|---|
| Data pipeline refactoring | Refactored a 1,834-line monolithic R script — behavior-preserving, verified after every change | 143,120 rows x 216 columns (report-ready); 143,143 x 1,918 (full) | import.R: 1,834 → 1,348 lines (−26.5%), identical() output |
| Config externalization | Extracted 257 hardcoded correction rules into 8 CSV files — clinic IDs, module reassignments, title corrections, column lists, success criteria | 8 CSVs, 257 entries | config/ directory |
| Deduplication | Found registercolumns vector duplicated across 2 files, merged into single CSV source | 93 entries in 2 files → 1 CSV | config/registercolumns.csv |
| Data validation | Byte-level output comparison (identical()) after every refactoring step — zero tolerance for behavioral change | Every commit verified against baseline RDS | Baseline RDS files created pre-refactoring |

## 4. Code review & bug discovery

| Bug | What I found | How | Impact |
|---|---|---|---|
| Complication grading column inconsistency | Major_K1 checked 3 grade columns but individual grades checked 4 — logically inconsistent | Systematic line-by-line analysis during D2 refactoring | Theoretical (no patient in 2025 data affected). Documented, flagged for supervisor |
| Operator precedence error | Karotis Stenting success evaluation: `&` binds tighter than `|` in R, causing missing Intervention filter on Teilerfolg/Misserfolg conditions | Manual operator precedence analysis | Likely harmless in practice (columns only populated for Karotis patients). Documented, preserved behavior, flagged for supervisor |

**Approach:** Did not silently fix bugs. Documented them, preserved exact original behavior, flagged for discussion. Refactoring discipline: change structure, not behavior.

## 5. Domain knowledge — medical data

| Topic | What I learned | Evidence |
|---|---|---|
| Interventional radiology | DeGIR modules A–F (vascular, cardiac, oncologic, neuro, non-vascular, pediatric), ~33 intervention types | module_corrections_catalog.md, medical_terminology.md |
| Complication grading | 7-grade severity scale (kein_T through Tod), 3 complication slots (K1/K2/K3), Major classification | grade_complication() function design |
| Success criteria | Per-intervention Erfolg/Teilerfolg/Misserfolg logic — some single-column, some multi-condition with regex | 16 CSV rules + 10 code-only complex rules |
| Quality registry operations | ~300 German clinics submitting via samedi platform, annual reports for DeGIR board (~300 clinic directors) | Project context |
| GDPR/BDSG compliance | Real patient data: birth dates anonymized, doctor names stripped, no patient data in version control | .agent/rules/01_data_confidentiality.md |

## 6. Tools & infrastructure

| Tool | How I used it | Evidence |
|---|---|---|
| Git | Branching (thejus/d3-config-extraction), squashed commits for collaborative repo, force-adding past .gitignore, two-repo workflow (development vs collaborative) | GitHub branch, commit history |
| GitHub | Collaborative development on abusjahn/radioDB | Push to remote, branch management |
| Conda | Environment management for R pipeline (healthtwist_r) | conda run -n healthtwist_r Rscript import.R |
| TinyTeX | PDF report rendering — diagnosed and fixed PATH issue | render_reports.sh |
| Linux (Debian) | Daily development environment | All work done on Linux |

## 7. Documentation & communication

| Skill | What I did | Evidence |
|---|---|---|
| Code documentation | Documented entire 1,834-line pipeline: 11 processing stations, data flow, column transformations | code_documentation.md, import_walkthrough.md |
| Interactive visualization | Built 17-page HTML visualization of all pipeline stations | visualized_import/ (16 detail + 1 main) |
| Technical analysis catalogs | Cataloged 31 module corrections (3 match types, 3 order-dependent chains) and 27 intervention label patterns | module_corrections_catalog.md, intervention_label_mapping_catalog.md |
| Professional German email | Weekly status updates to supervisor in German (B1/B2 level) | email_update_2026-02-28.md, email_update_2026-03-06.md |
| Column naming reference | Decoded German medical abbreviation conventions in column names | column_name_decoder.md |

## 8. Professional / soft skills

| Skill | How demonstrated | Evidence |
|---|---|---|
| Independent work | Supervisor was ill for 2+ weeks — prioritized tasks, made design decisions, communicated progress via email without waiting for direction | D3 started and completed during supervisor absence |
| Strategic prioritization | Chose to start with D3 (config extraction, lowest risk) instead of D1 (R package, highest complexity) — reordered the supervisor's list based on risk assessment | D3 completed first, D2 second |
| Initiative beyond assignment | Identified and extracted intervention_label_mapping (27 patterns) — not in the supervisor's original plan. Also extracted registercolumns/paecolumns after noticing cross-file duplication | intervention_label_mapping.csv, registercolumns.csv, paecolumns.csv |
| Decision-making under constraints | Split success criteria into 16 CSV + 10 code: clear boundary based on expressibility, not arbitrary. Documented reasoning | success_criteria.csv + inline comments |
| Error handling discipline | Discovered own mistake (wrong intervention counts propagated across 14 files), wrote postmortem, established verification workflow | error_propagation_postmortem.md |
| German language (B1→B2) | Writing technical workplace emails in German, learning medical terminology in German, supervisor communicates in German | Emails, medical_terminology.md |

## 9. Quantitative summary

| Metric | Value |
|---|---|
| Pipeline input size | 143,143 rows x ~1,920 columns |
| Pipeline output size | 143,120 rows x 216 columns |
| Code reduction | 1,834 → 1,348 lines (−26.5%) |
| Config files created | 8 CSVs, 257 total entries |
| Functions designed | 1 (grade_complication) |
| Pre-existing bugs found | 2 |
| Verification method | identical() byte-comparison after every change |
| Documentation pages | 17 HTML visualizations + multiple markdown references |
| Weeks completed | 5 of 21 |
| Directives completed | 2 of 4 (D2, D3) |

---

*Source: MASTER_RECALL.md (verified 2026-03-07). This file is a snapshot — update when new work is completed.*
