# 02. Methodological Lineage: GP to ConvCNP

> **Reading Time:** ~35 minutes  
> **Target:** Master the mathematical mechanics, inductive biases, and algorithmic trade-offs of the Neural Process family.

---

## 1. The Methodological Tree at a Glance

```
Gaussian Process (GP)
  |  [Exact Bayesian inference, calibrated uncertainty, but O(N^3) scaling & rigid kernels]
  v
Conditional Neural Process (CNP)  (Garnelo et al., 2018)
  |  [Deep learning scalability O(N_c + N_t), linear time, mean aggregation bottleneck]
  +-------------------------------------------------+
  |                                                 |
  v                                                 v
Neural Process (NP) (Latent NP)           Attentive Neural Process (ANP)
  (Garnelo et al., 2018)                    (Kim et al., 2019)
  [Global stochastic latent z,               [Cross-attention over context points,
   correlated function draws]                 resolves underfitting near sensors]
  |                                                 |
  +-----------------------+-------------------------+
                          |
                          v
         Convolutional Conditional Neural Process (ConvCNP)
              (Gordon et al., 2020; Vaughan et al., 2021)
              [Translation equivariance, continuous field mapping,
               multi-scale CNN backbone for gridded + off-grid data]
```

---

## 2. Gaussian Processes (GPs): The Classical Benchmark

In spatial geostatistics, predicting air quality at unmonitored locations has traditionally been performed using **Kriging**, which is mathematically identical to **Gaussian Process regression**.

### 2.1 Formulation
A Gaussian Process is a collection of random variables, any finite number of which have a joint Gaussian distribution. A GP is completely specified by a mean function `m(x)` (often assumed zero) and a covariance kernel `k(x, x')`:

```
f(x) ~ GP(m(x), k(x, x'))
```

Given training observations `D = {(x_i, y_i)}_{i=1}^N` with noise `y_i = f(x_i) + eps`, where `eps ~ N(0, sigma_n^2)`:
- Covariance matrix of training points: `K_XX` of size `N x N`, where `(K_XX)_{i,j} = k(x_i, x_j)`.
- Cross-covariance vector for a new target `x_*`: `k_X*` of size `N x 1`.
- Prior variance at target: `k(x_*, x_*)`.

The posterior predictive distribution at `x_*` is Gaussian `p(f_* | x_*, D) = N(mu_*, sigma_*^2)`:

```
mu_*      = k_X*^T * (K_XX + sigma_n^2 * I)^(-1) * y
sigma_*^2 = k(x_*, x_*) - k_X*^T * (K_XX + sigma_n^2 * I)^(-1) * k_X*
```

### 2.2 Why GPs Fail for Urban-Scale Deep Learning (AEON-UP)

1. **Cubic Computational Complexity `O(N^3)`:** Inverting the `N x N` matrix `(K_XX + sigma_n^2 * I)` requires `O(N^3)` operations and `O(N^2)` memory. In an urban setting with 100 sensors recording hourly over a year (`N = 100 * 8760 = 876,000`), `N^3` exceeds `6.7 * 10^17` operations, which is completely intractable.
2. **Stationarity and Rigid Kernels:** Standard stationary kernels (Radial Basis Function / Matérn) assume spatial correlation depends solely on Euclidean distance `||x - x'||`. In urban environments, spatial correlation is highly non-stationary: two sensors 50 meters apart on opposite sides of a tall building row experience completely decoupled airflow.
3. **No Direct Representation Learning:** GPs cannot easily ingest heterogeneous high-dimensional auxiliary grids (e.g. 15 meteorological layers, 3D building morphology, dynamic traffic maps) without complex hand-engineered kernel engineering.

---

## 3. Conditional Neural Processes (CNP)

Introduced by Garnelo et al. (2018), the **Conditional Neural Process (CNP)** combines the flexible representation learning of deep neural networks with the conditional uncertainty estimation of Gaussian Processes.

### 3.1 Step-by-Step Forward Pass Walkthrough

```
Context Set C: {(x_c, y_c)} (Sparse Sensors)
      |
      v
+-------------------+
|  Encoder h_theta  |  (MLP applied independently to each context point)
+-------------------+
      |
      v  r_c = h_theta(x_c, y_c)  in R^d
+-------------------+
|   Aggregator a    |  (Permutation-invariant mean: r = (1/N_c) * sum(r_c))
+-------------------+
      |
      v  r in R^d (Global context representation)
      +-----------------------------------------+
                                                |
Target Inputs T: {x_t} (Target Coordinates)     |
      |                                         |
      v                                         v
+---------------------------------------------------+
|                  Decoder g_phi                    |  (MLP: (x_t, r) -> mu, sigma^2)
+---------------------------------------------------+
      |
      v
Predictive Distribution: p(y_t | x_t, C) = N(mu(x_t), sigma^2(x_t))
```

#### Step 1: Context and Target Split
- **Context Set `C = {(x_c, y_c)}_{c=1}^{N_c}`:** The known observations (e.g., coordinates `x_c` and measured pollutant concentration `y_c` at `N_c` physical monitoring stations).
- **Target Inputs `T = {x_t}_{t=1}^{N_t}`:** The query locations where predictions are required (e.g. coordinates on an urban 10m grid).

#### Step 2: Context Encoder
Each context point is mapped into a latent representation `r_c` via an MLP encoder `h_theta`:
```
r_c = h_theta(x_c, y_c)     where r_c is a d-dimensional vector in R^d
```

#### Step 3: Permutation-Invariant Aggregation
To ensure that the order of sensor inputs does not affect the prediction, the representations are averaged:
```
r = (1 / N_c) * sum_{c=1}^{N_c} r_c
```
This single vector `r` summarizes the entire context set.

#### Step 4: Decoder
For each target location `x_t`, the decoder MLP `g_phi` concatenates the target location with the global context vector `r` and outputs the parameters of a Gaussian distribution:
```
(mu(x_t), log_sigma(x_t)) = g_phi(x_t, r)
sigma^2(x_t) = exp(2 * log_sigma(x_t)) + eps
```

#### Step 5: Computational Complexity
The encoder processes `N_c` points in `O(N_c)` time. The aggregator takes `O(N_c)` time. The decoder evaluates `N_t` points in `O(N_t)` time.
**Total Complexity: `O(N_c + N_t)`** — strictly linear!

### 3.2 Episodic Training as Meta-Learning

Training a CNP is not standard supervised regression on fixed points; it is **meta-learning across tasks (episodes)**:
1. Sample a batch of time snapshots (e.g. hourly concentration fields across a city).
2. For each snapshot, randomly partition the available measurement stations into:
   - Context set `C` of random size `N_c ~ Uniform(1, N_total - 1)`
   - Target set `T` of size `N_t = N_total` (often including context points to ensure consistency)
3. Compute the Negative Log-Likelihood (NLL) of the true target values under the predicted distribution:
   ```
   Loss(theta, phi) = - (1 / N_t) * sum_{t in T} log N(y_t; mu(x_t), sigma^2(x_t))
   ```
4. Backpropagate the loss to update encoder weights `theta` and decoder weights `phi`.

By training across thousands of random context/target splits, the model learns the **general underlying functional prior**, allowing instant zero-shot conditioning on new sensor configurations at test time.

---

## 4. Attentive Neural Processes (ANP)

While the CNP achieved linear scaling, it suffered from a fundamental flaw: **the mean aggregation bottleneck**.

### 4.1 The Underfitting Problem in CNPs
Because `r = (1 / N_c) * sum r_c` averages all context points uniformly, the representation `r` is dominated by the global mean. When predicting at a target location `x_t` right next to an active traffic sensor reporting 80 ug/m3, the CNP decoder receives the same averaged `r` as a target in a quiet park. Consequently, CNPs **underfit context points** and produce overly smooth fields that fail to capture localized peaks.

### 4.2 Cross-Attention Mechanism (Kim et al., 2019)
The **Attentive Neural Process (ANP)** replaces the uniform average with a **cross-attention mechanism**, querying the context points based on target location:

```
Target Query x_t --->  q_t = W_q * x_t
Context Key x_c  --->  k_c = W_k * x_c
Context Value    --->  v_c = W_v * r_c

Attention Weight a(x_t, x_c):
a_{t, c} = exp( (q_t . k_c) / sqrt(d_k) ) / sum_{c'} exp( (q_t . k_c') / sqrt(d_k) )

Target-Specific Context Vector:
r_t = sum_{c=1}^{N_c} a_{t, c} * v_c
```

The decoder evaluates `g_phi(x_t, r_t)`. When `x_t` is close to context sensor `x_c`, `a_{t, c} -> 1`, allowing the model to perfectly reconstruct localized sensor peaks while maintaining global awareness.

---

## 5. ConvCNP: The Paradigm for Gridded and Spatial Data

The **Convolutional Conditional Neural Process (ConvCNP)** (Gordon et al., 2020; Foong et al., 2020) and its climate application (*Convolutional conditional neural processes for local climate downscaling*, Vaughan et al., 2021, arXiv:2101.07950) represent the foundational architecture for AEON-UP.

### 5.1 Why Translation Equivariance is Essential
Physical atmospheric dispersion satisfies **translation equivariance**: if an emission source and wind field are shifted by vector `delta`, the resulting concentration plume shifts by exactly `delta`:

```
Physics:    Dispersion(Shift_delta(Emissions, Wind)) = Shift_delta(Dispersion(Emissions, Wind))
```

Standard MLPs and ANPs do not possess translational inductive bias; they must learn coordinate-specific mappings for every neighborhood. A **Convolutional Neural Network (CNN)** naturally enforces translation equivariance, vastly improving data efficiency and enabling **zero-shot transfer across cities**.

### 5.2 The 3-Stage ConvCNP Architecture

```
Stage 1: Off-the-Grid Functional Embedding (Discretization)
----------------------------------------------------------
Sparse Sensor Context C: {(x_c, y_c)}
  |
  |  Continuous Kernel Smoothing with Gaussian RBF psi(x - x_c)
  v
Internal Discretization Grid G = {g_1, g_2, ..., g_K}:
  - Signal Channel:   h_0(g_k) = sum_{c=1}^{N_c} y_c * psi(g_k - x_c)
  - Density Channel:  d_0(g_k) = sum_{c=1}^{N_c} psi(g_k - x_c)
  - Normalized Field: f_0(g_k) = [ h_0(g_k) / (d_0(g_k) + eps),  d_0(g_k) ]

Stage 2: Deep 2D/3D Convolutional Backbone (e.g. U-Net / ResNet)
----------------------------------------------------------------
Grid Feature Map f_0  +  Gridded CTM Priors (EPISODE-CityChem NetCDF)
  |
  v
+-------------------------------------------------------------+
| Deep U-Net / ResNet (Multi-scale receptive fields)          |
| - Captures regional advection across kilometers             |
| - Resolves local building/terrain interactions              |
+-------------------------------------------------------------+
  |
  v
Processed Functional Grid Feature Map f_L(g_k)

Stage 3: Continuous Target Readout (Interpolation & Decoding)
-------------------------------------------------------------
Target Coordinate x_t (Arbitrary continuous query location)
  |
  |  Continuous Kernel Interpolation from Grid G
  v
Target Feature Vector: r(x_t) = sum_{k=1}^K f_L(g_k) * psi(x_t - g_k)
  |
  v
+-----------------------+
|  Decoder MLP g_phi    |
+-----------------------+
  |
  v
Predictive Distribution: p(y_t | x_t, C) = N(mu(x_t), sigma^2(x_t))
```

### 5.3 The Critical Role of the Density Channel `d_0`
The density channel `d_0(g_k)` is a mathematical breakthrough for spatial deep learning:
- Where `d_0(g_k)` is **high**, the CNN knows that actual physical sensor measurements are present nearby. The model relies on observed data and predicts low epistemic uncertainty.
- Where `d_0(g_k)` is **zero**, the normalized channel is empty. The CNN recognizes that it must rely entirely on the gridded physical CTM prior (EPISODE-CityChem) and outputs higher epistemic uncertainty.

---

## 6. Mathematical Comparison of the Lineage

| Model | Computational Scaling | Translation Equivariance | Spatial Off-Grid Input | Local Resolution Fidelity | Target Sample Correlation |
|---|---|---|---|---|---|
| **Gaussian Process (GP)** | `O(N^3)` (Intractable) | Only with stationary kernel | Native | High | Full covariance |
| **CNP** | `O(N_c + N_t)` (Linear) | No (MLP) | Native | Poor (Mean bottleneck) | Factorized |
| **ANP** | `O(N_c * N_t)` (Quadratic in tokens) | No (Attention) | Native | High (Cross-attention) | Factorized |
| **ConvCNP** | `O(N_c + N_grid + N_t)` (Linear in data) | **Yes (CNN)** | **Native (Density channel)** | **High (U-Net multi-scale)** | Factorized (or ConvNP for joint) |

---

## 7. Key Methodological References

1. **Garnelo, M., et al. (2018):** *Conditional Neural Processes*. ICML 2018. arXiv: [1807.01613](https://arxiv.org/abs/1807.01613).
2. **Garnelo, M., et al. (2018):** *Neural Processes*. ICML 2018 Workshop on Theoretical Foundations and Applications of Deep Generative Models. arXiv: [1807.01622](https://arxiv.org/abs/1807.01622).
3. **Kim, H., et al. (2019):** *Attentive Neural Processes*. ICLR 2019. arXiv: [1901.05761](https://arxiv.org/abs/1901.05761).
4. **Gordon, J., et al. (2020):** *Convolutional Conditional Neural Processes*. ICLR 2020. arXiv: [1910.13551](https://arxiv.org/abs/1910.13551).
5. **Foong, A. Y., et al. (2020):** *Meta-Learning Stationary Stochastic Processes with Convolutional Neural Processes*. NeurIPS 2020. arXiv: [2007.01332](https://arxiv.org/abs/2007.01332).
6. **Vaughan, A., et al. (2021):** *Convolutional conditional neural processes for local climate downscaling*. Geoscientific Model Development, 15, 251–268, 2022. arXiv: [2101.07950](https://arxiv.org/abs/2101.07950).
