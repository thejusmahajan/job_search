# 03. Uncertainty Quantification, Metrics, and Evaluation

> **Reading Time:** ~30 minutes  
> **Target:** Master the operational distinction between aleatoric and epistemic uncertainty, scoring rules (CRPS), calibration diagnostics, and spatial validation protocols.

---

## 1. Aleatoric vs. Epistemic Uncertainty: The Operational Spine

In AEON-UP, uncertainty estimation is not an academic vanity metric; it directly drives **urban decision-making and optimal sensor network design**.

```
+-----------------------------------------------------------------------------+
|                               TOTAL UNCERTAINTY                             |
+--------------------------------------+--------------------------------------+
|        ALEATORIC UNCERTAINTY         |        EPISTEMIC UNCERTAINTY         |
|         (Data / Irreducible)         |         (Model / Reducible)          |
+--------------------------------------+--------------------------------------+
| Cause: Stochastic turbulence,        | Cause: Lack of spatial data, sparse  |
| sensor hardware noise, unmonitored   | monitoring network, unobserved       |
| micro-vehicle accelerations.         | meteorological regimes.              |
|                                      |                                      |
| Nature: Inherent property of the     | Nature: Property of the model's      |
| physical environment and sensor.     | knowledge deficit.                   |
|                                      |                                      |
| Reducible by adding more sensors?    | Reducible by adding more sensors?    |
| >> NO.                               | >> YES.                              |
|                                      |                                      |
| OPERATIONAL ACTION:                  | OPERATIONAL ACTION:                  |
| - Filter noise in data ingestion     | - **PLACE A NEW MONITORING STATION** |
| - Report inherent variance bounds    | - Gather targeted field campaign data|
+--------------------------------------+--------------------------------------+
```

### The Sensor Placement Dilemma (Interview Gold)
If municipal authorities have a budget to install **three new Ultrafine Particle (UFP) monitoring stations** in Hamburg:
- **Where to place them?** Place them in neighborhoods exhibiting **high epistemic uncertainty** (where the model lacks data and variance is high because no nearby stations exist).
- **Where NOT to place them?** Do not place them next to an existing traffic station with high aleatoric variance (where high variance is driven by random truck turbulence, not a lack of spatial knowledge).

---

## 2. Methods for Producing Uncertainty Estimates

In modern probabilistic deep learning, four primary mechanisms generate uncertainty:

```
1. Heteroscedastic Regression (Aleatoric)
   Model outputs parameters of distribution: (mu(x), sigma^2(x)) directly via MLP/CNN.

2. Deep Ensembles (Aleatoric + Epistemic)
   Train M independently initialized models with different random seeds.
   - Total Mean:      mu_ens(x) = (1/M) * sum_{m=1}^M mu_m(x)
   - Aleatoric Var:   sigma_alea^2(x) = (1/M) * sum_{m=1}^M sigma_m^2(x)
   - Epistemic Var:   sigma_epis^2(x) = (1/M) * sum_{m=1}^M (mu_m(x) - mu_ens(x))^2
   - Total Variance:  sigma_total^2(x) = sigma_alea^2(x) + sigma_epis^2(x)

3. Monte Carlo Dropout (Gal & Ghahramani, 2016)
   Keep dropout active at test time. Sample S stochastic forward passes.
   Variance across the S passes estimates epistemic uncertainty.

4. Neural Processes / ConvCNP
   Naturally parameterizes the conditional predictive distribution p(y_t | x_t, C).
   The density channel d_0 directly guides epistemic variance: high density -> low variance,
   zero density -> high variance returning to the prior.
```

---

## 3. Evaluation Metrics: Proper Scoring Rules and CRPS

Standard point metrics like Mean Squared Error (MSE) or Mean Absolute Error (MAE) cannot evaluate whether predicted probability distributions are realistic. AEON-UP relies on **Proper Scoring Rules**.

### 3.1 What is a Proper Scoring Rule?
A scoring rule `S(P, y)` assigns a numerical penalty to a forecast probability distribution `P` when the true outcome `y` is observed. A scoring rule is **strictly proper** if and only if the expected score is uniquely minimized when the forecaster asserts the true data-generating distribution `Q` (i.e. `P = Q`).

- **Proper:** Negative Log-Likelihood (NLL), Continuous Ranked Probability Score (CRPS), Brier Score.
- **NOT Proper for Distributions:** MAE, RMSE (they ignore predictive variance entirely).

### 3.2 Continuous Ranked Probability Score (CRPS)

The **Continuous Ranked Probability Score (CRPS)** generalizes Mean Absolute Error to probabilistic distributions.

#### General Continuous Formula:
```
CRPS(F, y) = integral_{-infinity}^{+infinity} [ F(z) - 1(z >= y) ]^2 dz
```
Where `F(z)` is the predicted cumulative distribution function (CDF) and `1(z >= y)` is the Heaviside step function centered at the actual observation `y`.

```
Visualizing CRPS:
Probability F(z)
  1.0 ^              Predicted CDF F(z)
      |                  /-----------
      |                 / |
      |                /  | Shaded area = CRPS
      |     ----------/   |
  0.0 +-------------------|-------------------------> z
                          Actual Observation y
```

#### Closed-Form Plain-Text Formula for Gaussian `N(mu, sigma^2)`:
For a Gaussian prediction with mean `mu` and standard deviation `sigma`, let normalized error `z = (y - mu) / sigma`:

```
CRPS(N(mu, sigma^2), y) = sigma * [ z * (2 * Phi(z) - 1) + 2 * phi(z) - (1 / sqrt(pi)) ]
```
Where:
- `Phi(z)` is the standard normal cumulative distribution function (CDF).
- `phi(z)` is the standard normal probability density function (PDF): `phi(z) = (1 / sqrt(2*pi)) * exp(-0.5 * z^2)`.
- `1 / sqrt(pi) = 0.56418958...`

#### Why CRPS is Ideal for AEON-UP:
1. **Physical Units:** CRPS has the **exact same units** as the target pollutant (e.g. `ug / m3` for NO2, `particles / cm3` for UFP).
2. **Deterministic Limit:** If predictive uncertainty collapses to zero (`sigma -> 0`), CRPS simplifies exactly to the standard Mean Absolute Error `|y - mu|`.
3. **Robustness:** Unlike Negative Log-Likelihood (NLL), which heavily penalizes occasional extreme outliers with infinite loss, CRPS provides linear penalties for extreme errors, preventing training instability.

---

## 4. Calibration vs. Sharpness

Probabilistic forecasting has a dual objective: **maximize sharpness subject to calibration**.

```
Calibration (Reliability)            Sharpness (Resolution)
Are predicted probabilities true?    How tight are the prediction intervals?

       Ideal Calibration:                   High Sharpness vs. Low Sharpness:
Actual Coverage %                    Distribution Density
 100 ^         / Ideal (y = x)          ^
     |        /                         |       *  [Sharp Forecast: Tight, informative]
  80 |       /                          |      * *
     |      /                           |     *   *
  50 |     /                            |    *     *
     |    /                             |   *       *
     |   /                              |  *         *  [Unsharp: Wide climatology]
   0 +-------------------->             +------------------------------------>
     0   50   80   100                         Concentration (ug/m3)
       Nominal Level %
```

### 4.1 Calibration Diagnostics
1. **Prediction Interval Coverage Probability (PICP):**
   For a nominal `(1 - alpha)` prediction interval (e.g., 90% interval `[q_0.05, q_0.95]`):
   ```
   PICP = (1 / N) * sum_{i=1}^N  1( y_i in [q_0.05(x_i), q_0.95(x_i)] )
   ```
   A calibrated model achieves `PICP = 0.90`. If `PICP < 0.90`, the model is **overconfident** (intervals too narrow). If `PICP > 0.90`, the model is **underconfident** (intervals too wide).
2. **Probability Integral Transform (PIT) Histogram:**
   Compute `u_i = F_i(y_i)`. If the forecast is perfectly calibrated, `u_i` follows a **standard uniform distribution `Uniform(0, 1)`**.
   - **U-shaped histogram:** Underdispersed / overconfident model (true observations fall in tails).
   - **Inverted-U / dome histogram:** Overdispersed / underconfident model (predictive variance too large).

### 4.2 Sharpness
Sharpness measures the concentration of the predictive distribution, quantified by the **Mean Prediction Interval Width (MPIW)**:
```
MPIW = (1 / N) * sum_{i=1}^N ( q_0.95(x_i) - q_0.05(x_i) )
```
A climatological average that always predicts `[0, 150 ug/m3]` can be 100% calibrated, but it has zero sharpness and is practically useless. We want the smallest possible MPIW that maintains nominal PICP.

---

## 5. The Spatial Validation Protocol: Avoiding the Leakage Trap

Standard machine learning practices fail catastrophically in geospatial environmental modeling if applied naively.

```
THE SPATIAL LEAKAGE TRAP (Random K-Fold Cross-Validation):

Station A: [t1] (Train)  [t2] (Test)   [t3] (Train)  [t4] (Test)   --> LEAKAGE!
Station B: [t1] (Test)   [t2] (Train)  [t3] (Test)   [t4] (Train)  --> LEAKAGE!

Result: Test points are temporally adjacent to training points at the EXACT SAME location.
The model memorizes local sensor bias instead of learning spatial interpolation.
Validation metrics show inflated R^2 = 0.95, but real-world spatial generalization collapses.
```

### 5.1 The Required Protocol: Leave-One-Station-Out (LOSO) Cross-Validation

```
CORRECT PROTOCOL: Leave-One-Station-Out (LOSO) / Spatial Block CV

Fold 1: Train on Stations [B, C, D, E] across ALL time steps.
        Test EXCLUSIVELY on Station [A] (Unseen geographic coordinate).

Fold 2: Train on Stations [A, C, D, E] across ALL time steps.
        Test EXCLUSIVELY on Station [B].
```

- **Why LOSO is Mandatory:** LOSO evaluates the model's true capability to perform **spatial interpolation/extrapolation** to unmonitored urban locations.
- **Epistemic Test:** A well-calibrated Neural Process will predict wider confidence intervals at Station A if Station A is geographically isolated from B, C, D, and E, proving that its epistemic uncertainty quantification is functional.

---

## 6. Key References on Uncertainty and Spatial Validation

1. **Lakshminarayanan, B., et al. (2017):** *Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles*. NeurIPS 2017. arXiv: [1612.01474](https://arxiv.org/abs/1612.01474).
2. **Gneiting, T., & Raftery, A. E. (2007):** *Strictly Proper Scoring Rules, Prediction, and Estimation*. Journal of the American Statistical Association, 102(477), 359–378. DOI: [10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437).
3. **Gal, Y., & Ghahramani, Z. (2016):** *Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning*. ICML 2016. arXiv: [1506.02142](https://arxiv.org/abs/1506.02142).
4. **Roberts, D. R., et al. (2017):** *Cross-validation strategies for data with temporal, spatial, or hierarchical structure*. Ecography, 40(8), 913–929. DOI: [10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881).
