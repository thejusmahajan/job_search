# Technical Skills — Other Languages, Tools & Infrastructure

## Other Programming Languages

| Language | Context |
|---|---|
| **Python** | Prior experience (pre-internship), MSc Bioinformatics coursework |
| **Fortran** | Prior experience (pre-internship), scientific computing |
| **Bash** | Pipeline execution scripts, conda automation, launcher scripts |
| **HTML/CSS** | Dashboard styling, interactive pipeline visualizations (17 HTML pages) |
| **LaTeX** | PDF report generation via knitr + kableExtra |

## Tools & Infrastructure

| Category | Tools |
|---|---|
| **Version control** | Git (branching, squash commits, force-add past .gitignore, two-repo workflow, branch management) |
| **Platforms** | GitHub (collaborative development, repository management) |
| **Environment** | Conda (healthtwist_r environment), R 4.3.1, module system |
| **Reporting** | Quarto, R Markdown, knitr, TinyTeX (LaTeX for PDF generation) |
| **Development** | RStudio, VS Code, Antigravity IDE |
| **Deployment** | shinyapps.io (rsconnect), localhost Shiny server |
| **Operating systems** | Linux (Debian, daily development), Windows (cross-platform verification) |
| **CI/Testing** | `identical()` byte-level comparison, `devtools::check()`, manual regression testing |

## Data Engineering & ETL Skills

| Skill | What I Did | Scale |
|---|---|---|
| Data pipeline refactoring | Refactored 1,834-line monolithic R script — behavior-preserving, verified after every change | 143,120 rows × 216 columns |
| Config externalization | Extracted 257 hardcoded correction rules into 8 CSV files | 8 CSVs, 257 entries |
| Deduplication | Found registercolumns duplicated across 2 files, merged into single CSV source | 93 entries |
| Data validation | Byte-level output comparison (identical()) after every refactoring step | Every commit verified |
| Cross-platform verification | Verified pipeline runs identically on Linux and Windows | Both OS verified |
