# Project 2: DeGIR Dashboard — Interactive Shiny Web Application

## Overview

Built an **interactive web dashboard** for exploring the DeGIR pipeline's clinical data output. The dashboard serves as both a **data exploration tool** and a **portfolio demonstration piece** ("visiting card").

- **Technology:** R Shiny (bslib framework)
- **Deployment:** shinyapps.io (free tier) — live at `https://thejusmahajan.shinyapps.io/degir-dashboard/`
- **Data:** Synthetic data only — fully GDPR-compliant, no real patient information
- **Bilingual:** Full German/English internationalization (i18n) toggle
- **Repository:** `github.com/thejusmahajan/degir-dashboard`

## Architecture & Modules

**Total codebase:** 1,468 lines of R across 10 files (6 modules + 3 utilities + main app).

| File | Lines | Role |
|---|---|---|
| `app.R` | 147 | Main entry point: UI layout, server logic, module orchestration |
| `R/mod_overview.R` | 146 | Pipeline overview — data dimensions, structure summary |
| `R/mod_interventions.R` | 129 | Intervention analysis — counts, distributions, filtering by module |
| `R/mod_complications.R` | 193 | Complication grading — SIR grades A–F visualization, rates by module |
| `R/mod_success.R` | 208 | Success/failure rates — Erfolg/Teilerfolg/Misserfolg per intervention |
| `R/mod_doses.R` | 197 | Radiation dose analysis — DLP, DAP, CTDI metrics by intervention |
| `R/mod_about.R` | 66 | About page — project context, methodology, data disclaimer |
| `R/utils_i18n.R` | 224 | Internationalization — complete DE/EN translation dictionary |
| `R/utils_plots.R` | 61 | Shared plotting utilities — consistent theme, color palettes |
| `R/utils_filters.R` | 97 | Central filtering logic — clinic, date range, intervention, module |

## Technical Features

- **Modular Shiny architecture** — each tab is a self-contained Shiny module (UI + server functions)
- **Reactive programming** — central filtered data reactives shared across modules; filters apply globally
- **Benchmark comparisons** — modules compare individual clinic data against the benchmark (all clinics)
- **Interactive visualizations** — Plotly-based charts with hover tooltips, zoom, pan
- **Data tables** — DT-based searchable/sortable tables with English tooltips for German intervention names
- **i18n system** — custom translation utility with 224 lines of translation mappings
- **CSS theming** — custom styling via `www/custom.css`, bslib Bootstrap theme (Flatly), Google Fonts (Source Sans Pro)
- **Loading states** — shinycssloaders spinners during computation
- **Sidebar filters** — clinic selector, date range picker, intervention filter, module checkboxes, reset button
- **Responsive layout** — bslib `page_fillable` + `page_navbar` for mobile-friendly navigation

## Dependencies
shiny, bslib, bsicons, plotly, DT, dplyr, tidyr, stringr, forcats, lubridate, scales, readr, shinycssloaders, htmltools

## Bug Fix: renderUI Timing Issue
Discovered and fixed a **renderUI timing bug** that caused empty plots across 4 benchmark modules. Root cause: `updateSelectInput` called before `renderUI` completed. Fixed by ensuring proper initialization sequence.

## Deployment
- Deployed to **shinyapps.io** (free tier) using `rsconnect`
- HTTP 200 verified
- Zero external dependencies beyond CRAN packages
- Self-contained — no degirtools dependency
