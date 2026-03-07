# Machine Learning & Tidymodels in R

## 1. Why ML in Single-Cell Genomics?
Standard statistics (like t-tests or ANOVA) assume you are comparing a few clean variables. Single-cell data has 20,000 variables (genes) for 100,000 cells. It is heavily sparse (mostly zeroes). Machine learning is required for:
- **Dimensionality Reduction:** Compressing 20,000 genes into a 2D or 3D map so a human can look at it (PCA, UMAP, t-SNE).
- **Clustering:** Automatically grouping cells that are mathematically similar to discover new cell types (K-means, Louvain, Leiden).
- **Prediction:** Training a model on known cell types to automatically classify new cells.

## 2. The Tidymodels Framework
Tidymodels is the modern ecosystem for modeling and machine learning in R using the `tidyverse` philosophy. It replaces the older `caret` package.

### The Core Packages You Taught (Introduction to Tidymodels repo)
- **`rsample`:** For data splitting and resampling (e.g., separating data into training and testing sets, or creating cross-validation folds).
- **`recipes`:** For data preprocessing and feature engineering. This is where you declare your statistical transformations (e.g., centering, scaling, dummy variables, imputing missing data) *before* applying them to the model.
- **`parsnip`:** A standardized, unified interface to various ML models. Instead of learning different syntaxes for Random Forests (`randomForest::randomForest()`) vs. XGBoost (`xgboost::xgb.train()`), `parsnip` uses one clean interface (`rand_forest() %>% set_engine("ranger")`).
- **`workflows`:** Bundles a `recipe` and a `parsnip` model together so they can be trained, tuned, and evaluated as a single object. This prevents data leakage.
- **`yardstick`:** For evaluating model performance (calculating accuracy, RMSE, ROC-AUC, etc.).

## 3. Interview Talking Points
- **Your teaching experience:** You literally wrote the introductory script transitioning Dr. Busjahn's course from `caret` to `Tidymodels`. Teaching a concept is the highest form of understanding.
- **Your Python ML skills:** You are also completing the IBM ML with Python certification on Coursera. This gives you a strong dual-language threat: you can do ML in `Tidymodels` (R) AND `scikit-learn` (Python).
- **Translating this to the Lab:** Emphasize that you know how to structure an ML pipeline properly (train/test splits, preventing data leakage via workflows, robust evaluation). This rigorous methodology is exactly what is needed when trying to predict cell fates or integrate DOGMA-seq modalities.
