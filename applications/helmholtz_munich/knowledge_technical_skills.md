# Technical Skills - Interview Knowledge File

## Overview
This knowledge file covers technical interview questions for the Bioinformatician/Data Scientist position at IDM Tübingen. Focus areas: R, Python, statistics, data analysis, pipeline development.

---

## Section 1: R Programming

### Q1.1: "Can you give a specific example of statistical analysis you've done in R?"

**Your Experience:**
- PostDoc: Ecological time-series analysis of cyanobacteria dynamics
- CQ Training: Biostatistics with patient datasets

**Example Answer:**
"During my PostDoc, I used R extensively for analyzing ecological time-series data. For example, I analyzed temperature response curves of cyanobacteria populations over multiple years, fitting nonlinear models to predict growth optima. I used `ggplot2` for visualization and `dplyr` for data wrangling.

More recently in my CQ biostatistics training, I've worked with clinical datasets—performing ANOVA to compare treatment groups, PCA for dimensionality reduction on multi-parameter patient data, and hierarchical clustering to identify patient subgroups. This directly relates to the sub-phenotyping work at IDM."

---

### Q1.2: "What R packages are you familiar with?"

| Package | Your Experience |
|---------|----------------|
| `ggplot2` | Visualization of time-series, publication-quality figures |
| `dplyr` / `tidyr` | Data manipulation, reshaping |
| `Bioconductor` | Biological data analysis (learned at CQ) |
| `tidymodels` | ML workflows (learning now, will use at HealthTwiSt) |
| `DESeq2` / `edgeR` | Differential expression (conceptual, CQ training) |
| `survival` | Survival analysis (CQ training) |
| `stats` | Base statistical functions |

---

### Q1.3: "How would you perform PCA in R and interpret the results?"

**Code Example:**
```r
# Load data
data <- read.csv("patient_data.csv")

# Prepare numeric matrix (exclude ID, categorical)
numeric_data <- data[, sapply(data, is.numeric)]

# Scale the data (important for PCA)
scaled_data <- scale(numeric_data)

# Perform PCA
pca_result <- prcomp(scaled_data, center = TRUE, scale. = TRUE)

# Summary - variance explained
summary(pca_result)

# Scree plot
plot(pca_result, type = "l", main = "Scree Plot")

# Biplot - visualize samples and loadings
biplot(pca_result, scale = 0)

# Extract PC scores for clustering
pc_scores <- pca_result$x[, 1:3]  # First 3 PCs
```

**Interpretation Points:**
- PC1 captures most variance—look at loadings to understand which variables drive it
- Cumulative variance: How many PCs needed to explain 80-90% variance?
- Clustering in PC space can reveal patient sub-phenotypes
- Loadings matrix shows variable contributions to each PC

---

### Q1.4: "Explain hierarchical clustering and when you'd use it"

**Answer:**
"Hierarchical clustering builds a tree (dendrogram) showing relationships between samples. I'd use it when:
- Exploring unknown structure in data
- Number of clusters isn't predetermined
- Want to visualize relationships at multiple scales

In prediabetes research, I'd cluster patients based on metabolic markers (glucose, insulin, HbA1c) to identify sub-phenotypes."

**Code Example:**
```r
# Distance matrix
dist_matrix <- dist(scaled_data, method = "euclidean")

# Hierarchical clustering
hc <- hclust(dist_matrix, method = "ward.D2")

# Plot dendrogram
plot(hc, labels = FALSE, main = "Patient Clustering")

# Cut tree to get clusters
clusters <- cutree(hc, k = 4)  # 4 clusters

# Add to original data
data$cluster <- as.factor(clusters)
```

---

### Q1.5: "How do you handle missing data in R?"

**Strategies:**
1. **Identify missing:**
```r
sum(is.na(data))
colSums(is.na(data))
```

2. **Complete case analysis:**
```r
complete_data <- na.omit(data)  # Loses rows
```

3. **Imputation:**
```r
library(mice)
imputed <- mice(data, m = 5, method = 'pmm')
complete_data <- complete(imputed)
```

4. **Simple mean/median imputation:**
```r
data$variable[is.na(data$variable)] <- median(data$variable, na.rm = TRUE)
```

**When to use what:**
- < 5% missing: complete case often OK
- MCAR (missing completely at random): any method
- MAR (missing at random): multiple imputation preferred
- Clinical data: document missingness, sensitivity analysis

---

## Section 2: Python Programming

### Q2.1: "What's your Python experience?"

**Your Background:**
- PostDoc: Analyzed NetCDF datasets with Python (xarray, pandas)
- PhD: C++ for signal processing (Python for prototyping)
- CQ: Object-oriented Python, Biopython

**Key Libraries:**
| Library | Use Case |
|---------|----------|
| `pandas` | Data manipulation, clinical datasets |
| `numpy` | Numerical operations, arrays |
| `scikit-learn` | ML models, preprocessing |
| `matplotlib` / `seaborn` | Visualization |
| `xarray` | Multi-dimensional arrays (NetCDF) |
| `Biopython` | Sequence analysis |

---

### Q2.2: "How would you load and explore a clinical dataset in Python?"

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("clinical_data.csv")

# Basic exploration
print(df.shape)  # rows, columns
print(df.dtypes)  # data types
print(df.describe())  # summary statistics
print(df.isnull().sum())  # missing values

# Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Distribution of key variable
sns.histplot(df['fasting_glucose'], kde=True)
plt.title("Fasting Glucose Distribution")
plt.show()
```

---

### Q2.3: "Explain the difference between pandas and numpy"

| Aspect | NumPy | Pandas |
|--------|-------|--------|
| Data structure | ndarray (homogeneous) | DataFrame/Series (heterogeneous) |
| Indexing | Integer-based | Label-based (column names, row index) |
| Use case | Numerical computation | Tabular data, mixed types |
| Speed | Faster for pure numeric | Convenient but slightly slower |
| Missing data | NaN (limited) | Native support (NA, NaN) |

**When to use:**
- NumPy: Matrix operations, image data, neural network backends
- Pandas: CSV/Excel data, clinical datasets, data cleaning

---

### Q2.4: "How would you build a simple classification model in scikit-learn?"

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Prepare features and target
X = df[['age', 'bmi', 'fasting_glucose', 'hba1c']]
y = df['diabetes_status']  # 0 = healthy, 1 = prediabetes, 2 = diabetes

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Feature importance
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importance)
```

---

## Section 3: Statistics & Biostatistics

### Q3.1: "Explain ANOVA and when you'd use it"

**Answer:**
"ANOVA (Analysis of Variance) tests whether means differ across 3+ groups. I'd use it to compare, say, metabolic parameters across different prediabetes sub-phenotypes."

**Assumptions:**
1. Independence of observations
2. Normality within groups
3. Homogeneity of variances (Levene's test)

**Example:**
```r
# One-way ANOVA
model <- aov(glucose ~ phenotype_cluster, data = patients)
summary(model)

# Post-hoc (which groups differ?)
TukeyHSD(model)

# Check assumptions
shapiro.test(residuals(model))  # normality
leveneTest(glucose ~ phenotype_cluster, data = patients)  # homogeneity
```

---

### Q3.2: "What's the difference between parametric and non-parametric tests?"

| Parametric | Non-parametric |
|------------|----------------|
| Assumes normal distribution | Distribution-free |
| Uses means | Uses medians/ranks |
| More power if assumptions met | More robust to outliers |
| t-test, ANOVA | Wilcoxon, Kruskal-Wallis |

**When to use non-parametric:**
- Small sample size
- Ordinal data
- Clear non-normality
- Outliers present

---

### Q3.3: "How do you handle multiple testing correction?"

**The Problem:** 
Testing many hypotheses inflates false positive rate.

**Solutions:**
```r
# Bonferroni (conservative)
p_adjusted <- p.adjust(p_values, method = "bonferroni")

# Benjamini-Hochberg (FDR control)
p_adjusted <- p.adjust(p_values, method = "BH")
```

| Method | Use Case |
|--------|----------|
| Bonferroni | Few tests, need strict control |
| Benjamini-Hochberg | Many tests (e.g., gene expression), accept some false positives |
| FDR | Exploratory analysis |

---

### Q3.4: "Explain survival analysis"

**Answer:**
"Survival analysis models time-to-event data—like time until diabetes diagnosis in prediabetic patients. It handles censoring (patients lost to follow-up)."

**Key Concepts:**
- **Kaplan-Meier curves:** Visualize survival probability over time
- **Log-rank test:** Compare survival between groups
- **Cox proportional hazards:** Identify risk factors

```r
library(survival)
library(survminer)

# Create survival object
surv_obj <- Surv(time = data$follow_up_years, 
                 event = data$developed_diabetes)

# Kaplan-Meier by phenotype
km_fit <- survfit(surv_obj ~ phenotype, data = data)

# Plot
ggsurvplot(km_fit, data = data, 
           pval = TRUE, 
           risk.table = TRUE)

# Cox model
cox_model <- coxph(surv_obj ~ age + bmi + fasting_glucose, data = data)
summary(cox_model)
```

---

## Section 4: Practical Coding Problems

### Problem 4.1: "Write a function to identify outliers in patient data"

```r
identify_outliers <- function(data, column, method = "iqr", threshold = 1.5) {
  x <- data[[column]]
  
  if (method == "iqr") {
    q1 <- quantile(x, 0.25, na.rm = TRUE)
    q3 <- quantile(x, 0.75, na.rm = TRUE)
    iqr <- q3 - q1
    lower <- q1 - threshold * iqr
    upper <- q3 + threshold * iqr
    outliers <- x < lower | x > upper
  } else if (method == "zscore") {
    z <- scale(x)
    outliers <- abs(z) > threshold
  }
  
  return(which(outliers))
}

# Usage
outlier_rows <- identify_outliers(patient_data, "bmi", method = "iqr")
```

---

### Problem 4.2: "Normalize gene expression data (in Python)"

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def normalize_expression(df, method='zscore'):
    """
    Normalize gene expression data
    
    Parameters:
    df: DataFrame with genes as columns, samples as rows
    method: 'zscore', 'minmax', or 'log2'
    """
    if method == 'zscore':
        scaler = StandardScaler()
        normalized = pd.DataFrame(
            scaler.fit_transform(df),
            columns=df.columns,
            index=df.index
        )
    elif method == 'minmax':
        scaler = MinMaxScaler()
        normalized = pd.DataFrame(
            scaler.fit_transform(df),
            columns=df.columns,
            index=df.index
        )
    elif method == 'log2':
        # Add pseudocount to avoid log(0)
        normalized = np.log2(df + 1)
    
    return normalized
```

---

### Problem 4.3: "Calculate BMI and categorize patients"

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate BMI from weight and height"""
    return weight_kg / (height_m ** 2)

def categorize_bmi(bmi):
    """WHO BMI categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Apply to dataframe
df['bmi'] = df.apply(lambda row: calculate_bmi(row['weight'], row['height']), axis=1)
df['bmi_category'] = df['bmi'].apply(categorize_bmi)
```

---

## Section 5: Domain-Specific Questions

### Q5.1: "How would you approach analyzing multi-organ data?"

**Answer:**
"Given IDM's focus on organ crosstalk (brain, liver, pancreas, fat), I would:

1. **Integrate datasets:** Merge patient data across organ measurements by patient ID
2. **Handle different scales:** Normalize each organ's measurements separately
3. **Correlation analysis:** Look for cross-organ correlations (e.g., liver fat vs. brain insulin sensitivity)
4. **Network analysis:** Build correlation networks to visualize organ interactions
5. **Multi-block methods:** Consider methods like multi-block PCA or canonical correlation analysis"

---

### Q5.2: "What challenges do you expect with clinical data?"

**Answer:**
1. **Missing data:** Patients miss visits, some tests not done
2. **Heterogeneity:** Different visits, protocols, measurement devices
3. **Confounders:** Age, sex, medication—need careful adjustment
4. **Longitudinal structure:** Repeated measurements need mixed models
5. **Regulatory requirements:** Data privacy, audit trails

---

## Quick Reference Card

| Task | R | Python |
|------|---|--------|
| Load CSV | `read.csv()` | `pd.read_csv()` |
| Summary | `summary()` | `df.describe()` |
| Missing values | `is.na()`, `na.omit()` | `df.isnull()`, `df.dropna()` |
| PCA | `prcomp()` | `sklearn.decomposition.PCA` |
| Clustering | `hclust()`, `kmeans()` | `sklearn.cluster` |
| t-test | `t.test()` | `scipy.stats.ttest_ind()` |
| ANOVA | `aov()` | `scipy.stats.f_oneway()` |
| Visualization | `ggplot2` | `matplotlib`, `seaborn` |
| ML workflow | `tidymodels` | `scikit-learn` |
