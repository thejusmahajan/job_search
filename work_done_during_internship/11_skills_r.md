# Technical Skills Inventory — R Programming

**Starting level:** Zero prior R experience. Learned from scratch during this internship.
**Ending level:** Working-proficient in R/tidyverse, Shiny, R package development, tidymodels.

## R / tidyverse

| Package/Feature | What I Used It For | Scale |
|---|---|---|
| **dplyr** (mutate, filter, case_when, select, group_by, summarise, left_join, across) | Core pipeline transformations | 143K rows × 216 columns |
| **tidyr** (pivot_longer, pivot_wider, unnest, separate, unite) | Data reshaping — replaced deprecated gather/spread | 101 sites across 4 files |
| **stringr** (str_detect, str_replace_all, str_to_lower, str_trim) | Regex-based intervention label matching, title normalization | 27 regex patterns |
| **readr** (read_csv, read_csv2, write_csv) | Reading config CSVs and main data export | 8 config CSVs |
| **purrr** (map, map2, map_df, walk) | Functional programming in statistical computations | summary_tables(), cat_desc_stats() |
| **ggplot2** (theme_set, theme_update, geom_*, scale_*) | Plot configuration and statistical visualization | Dashboard plots |
| **forcats** (fct_reorder, fct_lump, fct_infreq) | Factor level manipulation | Intervention categorization |
| **lubridate** (ymd, year, month, as.Date) | Date parsing and filtering | Treatment date processing |
| **magrittr** (%>% pipe) | Pipe-based data transformation chains | Entire codebase |
| **R base** (identical(), Reduce(), lapply(), switch(), factor()) | Byte-level verification, functional dispatch | Every extraction verified |
| **R function design** | Designed grade_complication() with asymmetric inputs | K1: 4 cols, K2/K3: 1 col each |
| **tidy evaluation** (quo(), !!, sym(), enquo()) | Non-standard evaluation for dynamic column references | German umlaut column names |
| **Quarto / R Markdown** | Reproducible documents, presentations | Tidymodels script, reports, presentation |

## R Package Development

| Skill | Evidence |
|---|---|
| Package structure (DESCRIPTION, NAMESPACE, R/, man/) | degirtools v0.1.0 |
| roxygen2 documentation (@param, @return, @export, @importFrom) | All 9 functions documented |
| devtools workflow (load_all, document, check, install, build) | 0 errors on R CMD check |
| NAMESPACE management (exports, imports) | roxygen2-generated NAMESPACE |
| globalVariables() for R CMD check compliance | globals.R |
| Dependency declaration (Imports field) | 12 dependencies listed |

## Shiny Web Application Development

| Skill | Evidence |
|---|---|
| Shiny module pattern (UI + server functions) | 6 modules in degir-dashboard |
| bslib framework (page_fillable, page_navbar, sidebar, nav_panel) | Modern Bootstrap-based UI |
| Reactive programming (reactive(), observeEvent(), reactiveVal()) | Central filtered data shared across modules |
| Plotly integration (renderPlotly, ggplotly, plot_ly) | Interactive charts with hover/zoom |
| DT tables (renderDT, datatable, formatStyle) | Searchable/sortable data tables |
| Internationalization (i18n) | Custom bilingual DE/EN system |
| Custom CSS theming | www/custom.css, bslib theme customization |
| Deployment (rsconnect, shinyapps.io) | Live production deployment |

## Machine Learning (tidymodels)

| Concept | Covered In |
|---|---|
| recipes (preprocessing, feature engineering, step_* functions) | Tidymodels script |
| parsnip (model specification, engine-agnostic API) | Tidymodels script |
| workflows (combining preprocessing + model) | Tidymodels script |
| rsample (train/test split, cross-validation, vfold_cv) | Tidymodels script |
| yardstick (evaluation metrics: RMSE, R², accuracy) | Tidymodels script |
| Linear regression, logistic regression | Tidymodels script |
| Hyperparameter tuning, model comparison | Tidymodels script |
