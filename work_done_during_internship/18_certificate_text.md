# Certificate Text & Formal Task Description

## Task Description (sent to Dr. Busjahn for Praktikumszeugnis, Apr 13)

During my internship at HealthTwiSt GmbH, I worked on two projects that involved data engineering, clinical data processing, and machine learning.

My first project was writing a teaching script for machine learning in R using the tidymodels framework (published as a Quarto document). I designed the curriculum to cover supervised learning workflows: data preprocessing, feature engineering with recipes, model specification with parsnip, ML pipeline automation with workflows, and model evaluation with yardstick. This replaced the older caret-based material in HealthTwiSt's training program.

My main project was refactoring the production data pipeline for the DeGIR Quality Registry. The pipeline processes real-world clinical data — about 143,000 interventional radiology patient records per year from roughly 300 German clinics — and produces statistical quality reports and clinical outcome analyses for the DeGIR board. I implemented and verified four refactoring directives on my own:

- Externalized 241 hardcoded data correction rules into 7 CSV config files, plus 16 success criteria into another config file (8 files, 257 entries total). Cut the main script by over 26% (1,834 to 1,349 lines) while keeping output byte-identical.
- Consolidated complication severity grading logic (7 SIR severity grades across 3 patient slots) into one parameterized function, replacing 124 lines of repeated code with 3 function calls.
- Replaced 360 deprecated function calls across 4 files (gather→pivot_longer, spread→pivot_wider, %<>%→explicit assignment, as.tibble→as_tibble).
- Extracted 9 utility functions into a standalone R package (degirtools) using devtools and roxygen2, with R CMD check passing cleanly. Global.R: 767 → 70 lines.

Also worked with clinical data: reviewing patient-level registry records, clinical outcome classifications (SIR complication grading), and defining clinical endpoints (success/partial success/failure criteria for 26 intervention types). Found and documented two pre-existing bugs.

Built an interactive R Shiny dashboard for exploring and visualizing the clinical data outputs.

Every change verified with identical() against original RDS baselines. Zero regressions.

## Skills Listed for Certificate

- R programming (tidyverse: dplyr, tidyr, ggplot2, stringr, readr, purrr)
- Machine learning in R (tidymodels: recipes, parsnip, workflows, yardstick, rsample)
- R package development (devtools, roxygen2, NAMESPACE management, R CMD check)
- R Shiny web application development
- Reproducible reporting (Quarto, R Markdown)
- Clinical registry data management
- Data engineering and ETL pipeline design at scale (143,000 records, 1,918 variables)
- Statistical reporting for clinical governance boards
- Software refactoring with automated regression testing
- Quality assurance — byte-level verification after every code change
- Version control (Git, GitHub: branching, pull requests, multi-repo workflows)
- GDPR/DSGVO-compliant handling of sensitive medical patient data
- Domain knowledge in interventional radiology
- Professional communication — weekly status reports and technical emails
- Independent project management
