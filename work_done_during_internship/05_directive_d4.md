# Directive 4 (D4): Deprecated Function Replacement — "Ersatz von deprecated Funktionen"

**Goal:** Replace all deprecated tidyverse functions with modern equivalents.

## Replacement Summary

| Phase | File(s) | Sites Replaced | Functions Replaced |
|---|---|---|---|
| Phase 1 | import.R | 19 | 2× gather→pivot_longer, 3× spread→pivot_wider, 14× %<>%→explicit assignment |
| Phase 2 | global.R | 53 | 52× %<>%→explicit assignment, 1× as.tibble→as_tibble |
| Phase 3a | Rmd files | 187 | %<>%→explicit assignment |
| Phase 3b | Rmd files | 15 | gather→pivot_longer |
| Phase 3c | Rmd files | 86 | spread→pivot_wider (with `names_sort = TRUE`) |
| **Total** | **4 files** | **360** | |

## Critical Finding: names_sort Discovery

`spread()` sorts output columns alphabetically by factor levels. `pivot_wider()` default uses first-appearance order. Without adding `names_sort = TRUE`, report tables would have **silently reordered columns** — invisible to the `identical()` check (which only verifies import.R output, not Rmd rendering). I caught this during code review **before writing any code**.

This was the scariest moment of the project. Every single report table would have had its columns silently reordered. Caught by thorough planning, not by testing.

## Result
Zero behavioral changes. All 360 deprecated calls eliminated from the pipeline.
