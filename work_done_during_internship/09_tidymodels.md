# Project 3: Introduction to Tidymodels Teaching Script

## Overview

**First assignment** from Dr. Busjahn: write a teaching script introducing the **tidymodels machine learning framework** in R, replacing the older **caret**-based material in HealthTwiSt's ML training curriculum (the "RStatsbook" course).

- **Format:** Quarto document (`.qmd`) — renders to HTML with executable R code blocks
- **Published:** `github.com/thejusmahajan/Introduction_to_Tidymodels` (public)
- **Length:** 302 lines
- **Dataset:** Palmer Penguins (standard ML teaching dataset)
- **Status:** Completed, reviewed by Dr. Busjahn, described as "ready for the next batch" of students

## Curriculum Structure

The script follows a pedagogical progression:

1. **Simple Workflow** — barebone tidymodels snapshot: specify model → fit → predict → evaluate
2. **Building Blocks** — individual components explained:
   - **recipes** — data preprocessing and feature engineering (step_* functions)
   - **parsnip** — model specification (engine-agnostic API)
   - **workflows** — combining preprocessing + model into a single pipeline
   - **rsample** — data splitting and resampling (train/test, cross-validation)
   - **yardstick** — model evaluation metrics (RMSE, R², accuracy)
3. **Full Workflow** — complete pipeline using all building blocks together

## Technical Concepts Covered

- Linear regression and logistic regression model specification
- Feature engineering with `step_*()` functions (normalization, dummy encoding, imputation)
- Train/test splitting with `initial_split()`
- Cross-validation with `vfold_cv()`
- Hyperparameter tuning
- Model comparison and evaluation
- `tidyverse`-native pipe syntax (`|>`)
- `pacman::p_load()` for dependency management
- `conflicted` package for namespace conflict resolution

## Significance

- Completing this script quickly demonstrated R programming competency despite **no prior R experience**
- Dr. Busjahn's response ("ready for the next batch") confirmed quality
- Led directly to assignment of the main pipeline refactoring project
- The script is now part of **HealthTwiSt's training material** for future students
- Replaced the older caret-based ML curriculum with modern tidymodels
