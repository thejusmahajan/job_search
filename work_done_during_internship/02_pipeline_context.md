# Project 1: DeGIR radioDB Pipeline Refactoring — Context & Architecture

## Context & Business Impact

**What is DeGIR?**
The Deutsche Gesellschaft für Interventionelle Radiologie und minimal-invasive Therapie (DeGIR) is the German national society for interventional radiology. It operates a **quality registry** where ~300 German clinics submit data about every interventional radiology procedure performed. This data is collected via the **samedi platform** and processed into annual quality reports.

**What does the pipeline do?**
1. Ingests a raw CSV export from samedi (~143,000 rows × ~1,920 columns per year)
2. Applies data corrections (clinic exclusions, module reassignments, title normalizations, intervention label mappings)
3. Computes clinical outcomes (complication severity grading, success/failure criteria)
4. Exports cleaned data as RDS files and Excel workbooks
5. Generates per-clinic and annual aggregate PDF quality reports via R Markdown

**Who uses the output?**
- The **DeGIR board** — annual quality reports
- ~300 **clinic directors** — per-clinic performance reports
- **HealthTwiSt GmbH** — data curation and report generation

**Why refactoring matters:**
The pipeline was a monolithic 1,834-line R script with hardcoded correction rules, copy-pasted logic, and deprecated function calls. Any real-world change (clinic merger, new intervention module, updated grading criteria) required editing R code. The refactoring made the pipeline maintainable by non-programmers (CSV edits instead of code changes) while guaranteeing zero behavioral change.

## Pipeline Architecture

```
Input: DeGIR-2025.csv (143,143 rows × ~1,920 columns — raw samedi export)
  │
  ▼
import.R (main ETL pipeline — 1,349 lines after refactoring)
  │ ├── Reads 8 config CSVs (corrections, column lists, success criteria)
  │ ├── Applies clinic exclusions, module corrections, title normalizations
  │ ├── Computes complication severity grading (7 SIR grades × 3 slots)
  │ ├── Computes success/failure criteria (26 intervention types)
  │ └── Exports cleaned data
  │
  ├──► rawdata-2025.RDS (143,120 rows × 216 columns — report-ready)
  │         │
  │         ▼
  │     renderReport.R → reportgenerator.Rmd → Per-clinic PDF reports
  │         │
  │         └──► orgdata_timefiltered.xlsx
  │
  ├──► orgdata-2025.RDS (143,143 rows × 1,918 columns — GDPR-stripped backup)
  │
  └──► 21 Excel exports (DeGIR aggregate, Greece, 18 per-intervention, Modulberichte)

reportgenerator_yearly2024.Rmd → Annual aggregate PDF (loads RDS directly)
```

**Row drop:** 143,143 → 143,120 = 23 rows dropped by `filter(!is.na(Intervention))`.
**Column drop:** ~1,920 → 216 = final column selection at pipeline end.

## Two-Repository Workflow

| Repository | Purpose | Access |
|---|---|---|
| `thejusmahajan/radioDB_on_duty` (private) | All work: agent files, docs, study notes, experiments | Thejus only |
| `abusjahn/radioDB` (collaborative) | Clean deliverables only — code changes, config files, package | Shared with Dr. Busjahn |

**Branches on collaborative repo:**
- `thejus/d3-config-extraction` — D3 config extraction + D2 refactoring (commits `e93275b`, `fdbd181`)
- `thejus/d4-d1-modernization` — D4 deprecated replacements + D1 package extraction (commits `28c8799`, `c5a990a`)
