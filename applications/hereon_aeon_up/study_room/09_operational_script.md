# 09. The AEON-UP Operational Script: Depth, Breadth, and Phased Execution

> **Document Purpose:** An operational blueprint for the Postdoctoral Researcher role in **AEON-UP** (*Probabilistic Deep Learning for Urban Air Quality*, Ref. `1056 - 2026/KU 2`) at Helmholtz-Zentrum Hereon (Geesthacht).
> **Tone & Stance:** Spoken from the perspective of an incoming computational scientist reasoning through research design choices, articulating trade-offs, and demonstrating deep command of the literature, domain bottlenecks, and day-to-day engineering.

---

# SECTION 1: THE LITERATURE FOUNDATION

Every paper card below is structured to capture the operational reality of the research: what was broken, what was done, the quantitative results reported, self-admitted limitations, concrete implications for AEON-UP, and the technical vocabulary introduced.

---

### Card 1: Vaughan et al. (2021 / 2022) — *The Core Downscaling Blueprint*
* **Citation:** Vaughan, A., Tebbutt, W., Hosking, J. S., & Turner, R. E. (2022). *Convolutional conditional neural processes for local climate downscaling.* **Geoscientific Model Development**, 15(1), 251–268. [arXiv:2101.07950](https://arxiv.org/abs/2101.07950) | DOI: [10.5194/gmd-15-251-2022](https://doi.org/10.5194/gmd-15-251-2022).
* **Problem:** Classical statistical downscaling methods (e.g., generalized linear models, quantile mapping) and standard deep learning models (MLPs, CNNs) are tied to fixed, rigid output grids. They cannot ingest arbitrary off-the-grid in-situ observation stations or predict at unseen geographical coordinates without retraining or separate interpolations. Conversely, Gaussian Processes (GPs) handle off-grid locations but suffer cubic scaling `O(N^3)` and fail to exploit spatial translation equivariance across gridded macro-scale atmospheric predictors.
* **Method:** Formulated local climate downscaling (temperature and precipitation) as a continuous-space meta-learning task using **Convolutional Conditional Neural Processes (ConvCNPs)**. The architecture:
  1. Ingests gridded low-resolution climate model reanalysis (ERA-Interim / CMIP) and irregular, sparse ground station records.
  2. Embeds off-grid point context data onto an internal uniform high-resolution mesh using a continuous-to-discrete smoothing kernel (SetConv layer), producing separate signal and density channels.
  3. Concatenates gridded physical covariates (topography, elevation, land-sea masks) with the discretized context grid.
  4. Passes the combined multi-channel representation through a deep 2D ResNet / U-Net backbone possessing spatial translation equivariance.
  5. Interpolates the resulting continuous feature field to arbitrary target station coordinates using a discrete-to-continuous kernel, outputting Gaussian predictive parameters `(u(x_*), sigma^2(x_*))` via negative log-likelihood training.
* **Result:** Evaluated on the European VALUE intercomparison benchmark across 86 weather stations for daily maximum temperature and precipitation over multiple decades:
  - For temperature: ConvCNP achieved Root Mean Square Error (RMSE) of `~ 1.45^degC` and Continuous Ranked Probability Score (CRPS) of `~ 0.82^degC`, significantly outperforming Gaussian Process baselines (CRPS `~ 1.05^degC`) and standard deep learning baselines (MLP CRPS `~ 1.18^degC`).
  - For precipitation: Produced well-calibrated probabilistic forecasts capturing non-Gaussian right-skewed precipitation distributions, outperforming the VALUE benchmark ensemble on extreme 98th percentile precipitation events.
* **Limitation:** As a *Conditional* NP, the model assumes conditional independence across target locations given the context set, `p(y_1:T | x_1:T, C) = prod_t=1^T p(y_t | x_t, C)`. It cannot generate spatially coherent sample paths (realizations) exhibiting joint inter-site covariance across simultaneous target queries. It is also computationally bounded by the internal discretization grid resolution.
* **For AEON-UP:** This is the direct architectural template for AEON-UP. The coarse atmospheric reanalysis in Vaughan et al. maps directly to EPISODE-CityChem or regional CTM gridded output; the weather stations map directly to urban air quality monitoring networks (EEA / AirBase); the topography covariates map to urban morphology, road density, and satellite TROPOMI NO₂ columns.
* **Terms Introduced:** *SetConv layer, functional representation, off-the-grid conditioning, translation equivariance, density channel, multi-site downscaling, continuous-to-discrete projection, episodic task training.*

---

### Card 2: Garnelo et al. (2018a) — *Conditional Neural Processes*
* **Citation:** Garnelo, M., Rosenbaum, D., Maddison, C. J., Ramalho, T., Saxton, D., Shanahan, M., Teh, Y. W., Rezende, D. J., & Eslami, S. M. A. (2018). *Conditional Neural Processes.* **International Conference on Machine Learning (ICML 2018)**, PMLR 80:1704–1713. [arXiv:1807.01613](https://arxiv.org/abs/1807.01613).
* **Problem:** Gaussian Processes provide principled closed-form Bayesian conditioning and uncertainty bounds but require `O(N^3)` computational time for matrix inversion and `O(N^2)` memory storage. Standard deep neural networks scale well with data but lack data-efficient conditioning on arbitrary-sized context sets at inference time without gradient fine-tuning.
* **Method:** Proposed the **Conditional Neural Process (CNP)**. A deterministic deep learning framework that models conditional distributions over functions `p(f(x_T) | x_T, C)`. Each context pair `(x_c, y_c)  in C` is passed through an encoder MLP `h_theta: \mathbb{R}^d_x + d_y -> \mathbb{R}^d`. The resulting representations `r_c` are aggregated into a fixed-size global representation `r = (1)/(|C|) sum_c  in C r_c` using a permutation-invariant mean operator. A decoder MLP `g_phi: \mathbb{R}^d_x + d -> \mathbb{R}^2 d_y` takes the concatenation `[x_t, r]` for each target query `x_t` and outputs the marginal Gaussian parameters `(u_t, sigma^2_t)`.
* **Result:** Demonstrated `O(N_c + N_t)` linear runtime scaling during training and inference. On 1D synthetic GP regression and 2D image completion (MNIST/CelebA pixel conditioning), CNPs achieved competitive marginal likelihoods to exact GPs while executing over `1000x` faster at test time on large context sizes (`N > 10^3`).
* **Limitation:** The permutation-invariant uniform mean aggregator `(1)/(|C|)sum r_c` acts as an informational bottleneck. It averages global context information, washing out local spatial features and leading to systematic underfitting near context points. Like all CNPs, predictions across multiple target points are factorized as independent marginals.
* **For AEON-UP:** Establishes the foundational linear-time meta-learning paradigm: framing urban air quality on a given day as a "task" with context stations and target prediction points.
* **Terms Introduced:** *Context set, target set, permutation invariance, symmetric aggregation, linear-time conditioning, functional meta-learning.*

---

### Card 3: Garnelo et al. (2018b) — *Neural Processes (Latent NPs)*
* **Citation:** Garnelo, M., Schwarz, J., Rosenbaum, D., Viola, F., Rezende, D. J., Eslami, S. M. A., & Teh, Y. W. (2018). *Neural Processes.* **ICML 2018 Workshop on Theoretical Foundations and Applications of Deep Generative Models**. [arXiv:1807.01622](https://arxiv.org/abs/1807.01622).
* **Problem:** CNPs output only factorized marginal distributions `N(u(x_t), sigma^2(x_t))`; they cannot draw coherent global function samples `f ~ p(f|C)`. If you sample `y_t_1 ~ N(u_1, sigma^2_1)` and `y_t_2 ~ N(u_2, sigma^2_2)`, the samples are uncorrelated even if `x_t_1` and `x_t_2` are `10 cm` apart.
* **Method:** Introduced a global stochastic latent variable `z ~ N(u_z(C), Sigma_z(C))` into the NP architecture. The context encoder parameterizes a variational posterior distribution `q(z|C)` and prior `p(z)`. During generation, a single vector `z` is sampled and passed to the decoder alongside target locations: `y_t = g_phi(x_t, z)`. The network is trained end-to-end by maximizing the Evidence Lower Bound (ELBO):
  `L(theta, phi) = \mathbb{E}_q(z|C  U  T)[sum_t  in T log p_phi(y_t | x_t, z)] - D_KL(q(z|C  U  T) \parallel q(z|C))`
* **Result:** Enabled the model to generate non-trivial, globally consistent sample trajectories that reflect true functional uncertainty. On 1D curve fitting and 2D image impainting, drawing multiple samples of `z` generated diverse, smooth, plausible functional realizations consistent with the observed context.
* **Limitation:** Training with stochastic gradient variational Bayes (ELBO) introduces optimization instability and variance in gradient estimates. In practice, the latent variable `z` often suffers from posterior collapse or still exhibits severe underfitting due to the uniform aggregation bottleneck in the encoder.
* **For AEON-UP:** If city officials or health researchers require spatially coherent daily concentration realization maps (e.g., simulating population exposure paths across an entire urban area), sampling from a latent NP is required rather than evaluating isolated marginal variances.
* **Terms Introduced:** *Latent path, variational posterior over functions, Evidence Lower Bound (ELBO), functional sampling, global stochastic latent variable `z`.*

---

### Card 4: Kim et al. (2019) — *Attentive Neural Processes*
* **Citation:** Kim, H., Mnih, A., Schwarz, J., Garnelo, M., Eslami, S. M. A., Rosenbaum, D., Vinyals, O., & Teh, Y. W. (2019). *Attentive Neural Processes.* **International Conference on Learning Representations (ICLR 2019)**. [arXiv:1901.05761](https://arxiv.org/abs/1901.05761).
* **Problem:** Both CNPs and Latent NPs suffer from severe **underfitting**. The uniform average aggregation `(1)/(|C|) sum r_c` weights a context sensor `100 km` away identically to a context sensor `10 m` away from the target query. The decoder cannot resolve sharp spatial gradients or reconstruct the exact values at context locations.
* **Method:** Replaced uniform mean aggregation with **multi-head cross-attention** mechanisms. The target query `x_t` acts as the query (`Q = W_Q x_t`), while context coordinates act as keys (`K = W_K x_c`) and context representations act as values (`V = W_V r_c`). The model calculates target-specific context embeddings:
  `r_t = MultiHeadAttention(Q=x_t, K=x_c, V=r_c)`
  The architecture maintains two parallel paths: a deterministic attentive path (capturing high-frequency local structure) and a stochastic latent path (capturing global uncertainty and functional sample diversity).
* **Result:** In 1D GP regression, 2D image completion, and contextual multi-armed bandits:
  - Reconstructed sharp boundaries without underfitting, accurately recovering true function values at context points (training context MSE dropped by over `85%` compared to CNP).
  - Outperformed standard NPs on 2D image log-likelihood by `>0.15 nats/pixel`.
* **Limitation:** Cross-attention has computational complexity `O(N_t . N_c)`. While significantly faster than exact GP inversion for moderate datasets, it does not inherently exploit 2D spatial grid structures or translation equivariance.
* **For AEON-UP:** Explains why pure MLP-based CNPs fail on urban air quality (where roadside concentrations drop exponentially within `50 m`). Attention allows the network to dynamically weight adjacent roadside or background stations based on proximity and meteorological flow direction.
* **Terms Introduced:** *Cross-attention aggregation, query-key-value routing, deterministic vs. stochastic paths, underfitting bottleneck, attention weights over context points.*

---

### Card 5: Gordon et al. (2020) — *Convolutional Conditional Neural Processes*
* **Citation:** Gordon, J., Bruinsma, W. P., Foong, A. Y. K., Requeima, J., Dubois, Y., & Turner, R. E. (2020). *Convolutional Conditional Neural Processes.* **International Conference on Learning Representations (ICLR 2020)**. [arXiv:1910.13551](https://arxiv.org/abs/1910.13551).
* **Problem:** Physical processes in continuous Euclidean space possess **translation equivariance**: shifting the physical inputs in space shifts the resulting response identically. Standard MLPs and ANPs are not translation equivariant and cannot generalize (extrapolate) to unobserved spatial domains or train efficiently on large spatial fields without learning coordinate dependencies redundantly.
* **Method:** Embedded the principles of Convolutional Neural Networks into Conditional Neural Processes by formulating functional operations on continuous function spaces `H`:
  1. Context points `(x_c, y_c)` are mapped to a continuous functional representation `h_C(x)` via continuous kernel convolutions (SetConv layer with a radial basis function `psi(x - x_c)`):
     `h_C(x) = sum_c  in C y_c psi(x - x_c), \quad rho_C(x) = sum_c  in C psi(x - x_c)`
  2. Discretizes this continuous field onto a uniform internal grid.
  3. Applies a deep, translation-equivariant standard 2D CNN (or U-Net) with stationary convolutional filters over the internal grid.
  4. Reads out predictions at arbitrary target query locations `x_t` using a continuous interpolation kernel.
* **Result:** Achieved state-of-the-art performance on 1D/2D synthetic GP regression, simulated climate data, and spatial interpolation tasks. Demonstrated zero-shot spatial generalization: models trained on small coordinate windows generalized seamlessly to larger spatial domains without loss of calibration.
* **Limitation:** Discretization requires selecting an internal grid spacing `Delta x`. If `Delta x` is too coarse, sub-grid point features are blurred; if `Delta x` is too fine, 2D/3D CNN GPU memory scales quadratically/cubically.
* **For AEON-UP:** This paper provides the mathematical proof and architecture for embedding Eulerian CTM fields (EPISODE-CityChem) and Lagrangian point measurements (monitoring stations) into a single unified translation-equivariant deep learning pipeline.
* **Terms Introduced:** *Translation equivariance, continuous convolution layer (SetConv), density channel `rho(x)`, functional embedding, spatial extrapolation, discretization grid.*

---

### Card 6: Kendall & Gal (2017) — *Aleatoric vs. Epistemic Uncertainty in Deep Learning*
* **Citation:** Kendall, A., & Gal, Y. (2017). *What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?* **Advances in Neural Information Processing Systems (NeurIPS 2017)**, 30, 5574–5584. [arXiv:1703.04977](https://arxiv.org/abs/1703.04977).
* **Problem:** Classical deep learning outputs single point estimates. When uncertainty is computed, practitioners often conflate observation noise with model ignorance, making it impossible to diagnose whether a high-variance prediction requires more training data or reflects inherently noisy sensors.
* **Method:** Formulated an integrated framework separating uncertainty into two distinct mathematical components:
  1. **Aleatoric Uncertainty (Data Noise):** Heteroscedastic noise modeled by having the neural network output two heads: predicted mean `est {y}_i` and predicted observation variance `est {s}_i = log est {sigma}_i^2`. Trained via Gaussian negative log-likelihood loss:
     `L_NN(theta) = (1)/(N) sum_i=1^N (1)/(2) exp(-est {s}_i) \|y_i - est {y}_i\|^2 + (1)/(2) est {s}_i`
  2. **Epistemic Uncertainty (Model Ignorance):** Represented by placing a prior distribution over network weights `W ~ p(W)`, approximated via Monte Carlo Dropout (or deep ensembles). At inference, `T` stochastic forward passes are sampled:
     `sigma^2_total(x_*) = \underbrace{(1)/(T) sum_t=1^T est {sigma}_t^2(x_*)}_Aleatoric (Heteroscedastic) + \underbrace{(1)/(T) sum_t=1^T (est {y}_t(x_*) - mean {y})^2}_Epistemic (Model Deficit)`
* **Result:** Demonstrated on pixel-wise semantic segmentation (CamVid) and depth regression (NYUv2) that aleatoric uncertainty captures object boundaries and distant/reflective surfaces, whereas epistemic uncertainty spikes on unseen object classes, corrupted images, and data voids.
* **Limitation:** Monte Carlo Dropout requires heuristic tuning of dropout probabilities and does not always yield fully calibrated epistemic variances compared to full Markov Chain Monte Carlo (MCMC) or deep ensembles.
* **For AEON-UP:** The operational distinction is fundamental. Epistemic uncertainty dictates where Hereon or municipal partners should deploy new monitoring stations (information-gathering). Aleatoric uncertainty sets the theoretical error floor caused by microscale wind turbulence and sensor hardware noise.
* **Terms Introduced:** *Heteroscedastic aleatoric loss, epistemic parameter variance, Monte Carlo Dropout, predictive variance decomposition, total predictive uncertainty.*

---

### Card 7: Lakshminarayanan et al. (2017) — *Deep Ensembles for Uncertainty*
* **Citation:** Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). *Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles.* **Advances in Neural Information Processing Systems (NeurIPS 2017)**, 30, 6402–6413. [arXiv:1612.01474](https://arxiv.org/abs/1612.01474).
* **Problem:** Bayesian Neural Networks trained via variational inference (e.g., Bayes by Backprop) are computationally burdensome, difficult to optimize, sensitive to prior choices, and often underperform deterministic networks on raw predictive accuracy.
* **Method:** Proposed **Deep Ensembles** as a non-Bayesian (yet empirically superior) alternative for uncertainty quantification. The method:
  1. Trains `M` independent neural networks initialized with distinct random seeds, optimizing proper scoring rules (Gaussian NLL with heteroscedastic output heads).
  2. Employs adversarial training (Fast Gradient Sign Method, FGSM) to smooth predictive distributions in the vicinity of training points.
  3. Combines predictions at test time as a uniformly weighted Gaussian mixture:
     `u_*(x) = (1)/(M)sum_m=1^M u_m(x), \quad sigma_*^2(x) = (1)/(M)sum_m=1^M (sigma_m^2(x) + u_m^2(x)) - u_*^2(x)`
* **Result:** Evaluated across standard UCI regression benchmarks and ImageNet classification:
  - Consistently delivered better calibration (lower Expected Calibration Error, ECE) and proper scoring metrics (CRPS / NLL) than variational BNNs and MC Dropout.
  - Exhibited superior out-of-distribution (OOD) detection when tested on dataset distribution shifts.
* **Limitation:** Requires training and storing `M` distinct model checkpoints (typically `M = 5` to `10`) and running `M` forward passes at inference time, multiplying compute and memory requirements by factor `M`.
* **For AEON-UP:** Serves as the primary operational baseline for quantifying epistemic uncertainty in the neural process pipeline. Training an ensemble of 5 ConvCNPs provides a robust, highly calibrated uncertainty ceiling against which single-model latent NPs must be benchmarked.
* **Terms Introduced:** *Deep ensemble, Gaussian mixture reduction, scoring rule optimization, out-of-distribution detection, seed randomization.*

---

### Card 8: Gneiting & Raftery (2007) — *Strictly Proper Scoring Rules and CRPS*
* **Citation:** Gneiting, T., & Raftery, A. E. (2007). *Strictly Proper Scoring Rules, Prediction, and Estimation.* **Journal of the American Statistical Association**, 102(477), 359–378. DOI: [10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437).
* **Problem:** Evaluating probabilistic forecasts using point metrics (MAE, RMSE) completely ignores predictive variance. Conversely, optimizing arbitrary variance metrics can reward dishonest forecasters who artificially inflate or deflate uncertainty to manipulate scores.
* **Method:** Established the mathematical theory of **Strictly Proper Scoring Rules**. A scoring rule `S(P, y)` assigns a numerical loss to a predictive probability distribution `P` when observation `y` materializes. It is *strictly proper* if and only if the expected score is uniquely minimized when the forecaster issues the true data-generating distribution `Q`:
  `\mathbb{E}_y ~ Q[S(Q, y)] <= \mathbb{E}_y ~ Q[S(P, y)], \quad with equality iff P = Q`
  Detailed the **Continuous Ranked Probability Score (CRPS)**, which measures the integrated squared distance between the predictive cumulative distribution function `F(z)` and the empirical Heaviside step function `\mathbb{I}(z >= y)`:
  `CRPS(F, y) = integral_-inf^inf (F(z) - \mathbb{I}(z >= y))^2 dz`
  For a Gaussian prediction `N(u, sigma^2)`, CRPS reduces to a closed form:
  `CRPS(N(u, sigma^2), y) = sigma ( (y - u)/(sigma) (2\Phi((y - u)/(sigma)) - 1) + 2phi((y - u)/(sigma)) - (1)/(sqrt(\pi)) )`
* **Result:** Proved that CRPS is strictly proper, reports errors in the physical units of the pollutant (`ug/m^3`), generalizes Mean Absolute Error (as `sigma -> 0`, `CRPS -> |y - u|`), and directly penalizes both bias and miscalibrated spread.
* **Limitation:** Closed-form solutions exist for Gaussian and certain parametric distributions; non-parametric empirical ensembles require numerical sorting and integration `O(K log K)` across ensemble members.
* **For AEON-UP:** CRPS is the non-negotiable primary evaluation metric for AEON-UP. Benchmarking ConvCNP against EPISODE-CityChem, Land-Use Regression, and Gaussian Processes must be judged on CRPS and sharpness subject to calibration.
* **Terms Introduced:** *Strictly proper scoring rule, propriety, Continuous Ranked Probability Score (CRPS), calibration vs. sharpness, probability integral transform (PIT).*

---

### Card 9: Karl et al. (2019) — *The EPISODE-CityChem Chemistry Transport Model*
* **Citation:** Karl, M., Walker, S.-E., Solberg, S., & Ramacher, M. O. P. (2019). *The Eulerian urban dispersion model EPISODE – Part 2: Extensions to the source dispersion and photochemistry for EPISODE–CityChem v1.2 and its application to the city of Hamburg.* **Geoscientific Model Development**, 12(3), 3357–3385. DOI: [10.5194/gmd-12-3357-2019](https://doi.org/10.5194/gmd-12-3357-2019).
* **Problem:** Regional Chemistry Transport Models (e.g., CMAQ, EMEP) run at coarse grid resolutions (`1-10 km`), which cannot resolve steep pollutant gradients in urban street canyons or near major traffic arteries where human exposure is highest. Conversely, microscale CFD models are computationally intractable for entire cities over annual timescales.
* **Method:** Developed **EPISODE-CityChem v1.2**, an urban-scale Eulerian chemistry transport model system:
  1. Solves the 3D advection-diffusion-reaction equation on an Eulerian main grid (typically `100-1000 m` resolution) using terrain-following `sigma`-coordinates.
  2. Embeds sub-grid Lagrangian dispersion modules: the **Simplified Street Canyon Model (SSCM)** for road line sources and Gaussian puff modules (SEGMENT/WMPP) for industrial point sources.
  3. Integrates a specialized chemical mechanism (**CityChem-CABM**) with 22 chemical species and 32 reactions, explicitly solving photochemistry (`NO-NO_2-O_3` equilibrium and VOC oxidation) on both the Eulerian grid and within sub-grid street canyons.
* **Result:** Evaluated over the city of Hamburg (`30 x 30 km^2` domain at `100 m` resolution):
  - Achieved high agreement with municipal monitoring networks: Index of Agreement (IOA) of `0.85` for hourly `NO_2` and `0.78` for `O_3` at urban background stations.
  - Successfully captured localized concentration peaks in narrow street canyons that regional models smoothed out.
* **Limitation:** High computational cost: simulating an entire annual cycle for a single metropolis requires days of dedicated multi-core HPC compute. Model accuracy depends critically on bottom-up emissions inventories and hourly NWP meteorological boundary files.
* **For AEON-UP:** This is Dr. Matthias Karl’s flagship simulation engine. The operational objective of AEON-UP is not to replace EPISODE-CityChem, but to use machine learning surrogates (ConvCNPs) to accelerate, downscale, and fuse its physical outputs with real-time station measurements across multiple European cities.
* **Terms Introduced:** *EPISODE-CityChem, Eulerian main grid, sub-grid line source dispersion (SSCM), CityChem-CABM chemical mechanism, terrain-following sigma coordinates, boundary forcing.*

---

### Card 10: Lauenburg, Karl, Matthias, Quante, & Ramacher (2021) — *Ultrafine Particle Modeling*
* **Citation:** Lauenburg, M., Karl, M., Matthias, V., Quante, M., & Ramacher, M. O. P. (2021). *City Scale Modeling of Ultrafine Particles in Urban Areas with Special Focus on Passenger Ferryboat Emission Impact.* **Toxics**, 10(1), 3. DOI: [10.3390/toxics10010003](https://doi.org/10.3390/toxics10010003).
* **Problem:** Ultrafine particles (diameter `D_p < 100 nm`) pose severe public health risks due to deep pulmonary and systemic cardiovascular/neurological penetration. However, UFPs have negligible mass, rendering standard mass-based metrics (`PM_2.5`, `PM_10`) ineffective as proxies. UFPs are governed by rapid physical microphysics (nucleation, coagulation, condensation) that cause particle numbers to decay rapidly within tens of meters from sources.
* **Method:** Coupled the EPISODE-CityChem model with a detailed aerosol microphysics module (MONO32) to simulate Particle Number Concentrations (PNC) and size distributions (ranging from nucleation mode `10 nm` to accumulation mode) across the urban domain of Hamburg. Evaluated the specific spatial impact of marine and harbor line/point sources (passenger ferryboats and container shipping) alongside road traffic.
* **Result:** 
  - Demonstrated that shipping and ferryboat emissions contribute up to `30-40%` of local PNC in waterfront and harbor-adjacent urban zones, creating sharp spatial plumes with PNC `> 30,000 particles/cm^3`.
  - Quantified the rapid spatial decay of PNC away from waterways due to atmospheric dilution and coagulation.
* **Limitation:** In-situ measurement verification is constrained by extreme spatial sparsity: European cities rarely maintain more than 1–3 permanent PNC condensation particle counters (CPCs), making widespread model validation difficult.
* **For AEON-UP:** Direct confirmation of Dr. Karl and Dr. Ramacher's operational focus on UFPs. Highlights why probabilistic neural processes are mandatory for UFP modeling: because ground sensors are extremely sparse and microphysics are non-linear, the model must output wide, honest epistemic uncertainty bands in unmonitored neighborhoods.
* **Terms Introduced:** *Particle Number Concentration (PNC), ultrafine particles (UFP, `D_p < 100 nm`), aerosol microphysics, coagulation sink, condensation, condensation particle counter (CPC).*

---

### Card 11: Ramacher & Tang (2021) — *UrbEm High-Resolution Urban Emission Downscaling*
* **Citation:** Ramacher, M. O. P., & Tang, L. (2021). *UrbEm - A model to calculate high-resolution emission inventories of air pollutants and greenhouse gases in urban areas.* **Atmosphere**, 12(11), 1404. DOI: [10.3390/atmos12111404](https://doi.org/10.3390/atmos12111404).
* **Problem:** Running urban-scale CTMs across multiple European cities requires bottom-up emissions inventories. However, most cities lack high-resolution local bottom-up activity inventories; standard European inventories (CAMS-REG, EMEP) are gridded at `6-10 km`, which is too coarse for street-scale dispersion.
* **Method:** Created **UrbEm**, an open-source top-down emission downscaling framework:
  1. Ingests regional gridded inventories (e.g., CAMS-REG `0.05^deg x 0.1^deg`).
  2. Disaggregates emissions into GNFR source categories (transport, industry, domestic heating, shipping).
  3. Uses open-access spatial proxies (OpenStreetMap road network topologies, building volumes, Corine Land Cover, Urban Atlas, and Global Human Settlement population densities) to redistribute emissions onto `100-1000 m` urban grids and discrete road vector links.
* **Result:** Successfully generated standardized `100 m` resolution emission fields across Nordic and German cities. Provided the necessary hourly emission input files for EPISODE-CityChem, achieving cross-city comparability without requiring proprietary municipal traffic datasets.
* **Limitation:** Relies on proxy-based spatial disaggregation; cannot capture real-time traffic jams or temporal heating spikes unless driven by dynamic local proxy datasets.
* **For AEON-UP:** UrbEm is Dr. Martin Ramacher’s core emission downscaling system. In the AEON-UP data pipeline, UrbEm spatial emission proxies (OSM road densities, land-use fractions) serve directly as static and dynamic covariate channels for the ConvCNP spatial encoder.
* **Terms Introduced:** *UrbEm, spatial disaggregation, top-down emission downscaling, spatial proxies, GNFR source sectors, OpenStreetMap line proxies.*

---

### Card 12: Classical Baseline & ML Review
#### 12a. Hoek et al. (2008) — *Land-Use Regression (The Classical Baseline)*
* **Citation:** Hoek, G., Beelen, R., de Hoogh, K., Vienneau, D., Gulliver, J., Fischer, P., & Briggs, D. (2008). *A review of land-use regression models to assess spatial variation of outdoor air pollution.* **Atmospheric Environment**, 42(33), 7561–7578. DOI: [10.1016/j.atmosenv.2008.05.057](https://doi.org/10.1016/j.atmosenv.2008.05.057).
* **Problem:** Classical urban dispersion modeling requires massive computational infrastructure and detailed emission/meteorological inventories that were unavailable for epidemiological cohort studies covering thousands of subjects.
* **Method:** Reviewed **Land-Use Regression (LUR)**, the standard statistical baseline in environmental epidemiology. LUR fits a multiple linear regression predicting long-term average pollutant concentration at site `s`:
  `y(s) = beta_0 + sum_k=1^K beta_k X_k(s) + eps(s)`
  where `X_k(s)` are GIS-derived spatial predictors buffer-aggregated around station `s` (e.g., road length within `50-1000 m`, residential population, industrial area, altitude). Predictors are selected via supervised stepwise forward selection.
* **Result:** Across dozens of European and North American studies, LUR explained `50-80%` of spatial variance (`R^2 = 0.50-0.80`) for annual `NO_2` and `PM_2.5`.
* **Limitation:** Linear and stationary: assumes relationships between GIS predictors and concentrations are constant across an entire region. Completely ignores fluid advection-diffusion physics, cannot model hourly temporal dynamics, and fails when transferred to different cities with different urban typologies.
* **For AEON-UP:** LUR (and its non-linear tree-based successor, Spatial Random Forest / XGBoost) is the mandatory baseline. Any proposed deep neural process must demonstrate statistically significant improvements over regularized LUR on CRPS and out-of-station validation.

#### 12b. Cabaneros et al. (2019) — *Review of AI for Air Pollution*
* **Citation:** Cabaneros, S. M., Calautit, J. K., & Hughes, B. R. (2019). *A review of artificial neural network models for ambient air pollution prediction.* **Environmental Modelling & Software**, 119, 285-304. DOI: [10.1016/j.envsoft.2019.06.014](https://doi.org/10.1016/j.envsoft.2019.06.014).
* **Summary & Relevance:** Comprehensive review detailing the evolution of AI in air quality modeling from single-layer ANNs to deep LSTMs, Graph Neural Networks (GNNs), and hybrid physics-AI systems. The authors emphasize that pure data-driven models suffer from spatial overfitting, lack physical conservation guarantees, and fail catastrophically during extreme weather anomalies unless coupled with physical CTM boundary priors.

---

### Additional Selected Papers (3 Crucial Methodological Pillars)

---

### Card 13: Roberts et al. (2017) — *Spatial Cross-Validation & The Leakage Trap*
* **Citation:** Roberts, D. R., Bahn, V., Ciuti, S., Boyce, M. S., Elith, J., Guillera-Arroita, G., Hauenstein, S., Lahoz-Monfort, J. J., Schröder, B., Thuiller, W., Warton, D. I., Wintle, B. A., Hartig, F., & Dormann, C. F. (2017). *Cross-validation strategies for data with temporal, spatial, hierarchical or phylogenetic structure.* **Ecography**, 40(8), 913–929. DOI: [10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881).
* **Problem:** Standard random `k`-fold cross-validation randomly assigns individual observations to train and test folds. In spatio-temporal datasets, points close in space and time share strong spatial autocorrelation (Tobler's First Law). Random CV causes severe **data leakage**: the test fold contains observations whose immediate neighbors are in the training fold, yielding artificially inflated `R^2` scores and falsely overconfident models.
* **Method:** Systematic benchmarking of structured cross-validation strategies:
  - **Spatial Block Cross-Validation:** Partitioning geographical domains into spatial contiguous blocks/tiles larger than the spatial autocorrelation range.
  - **Leave-One-Station-Out (LOSO) CV:** Holding out entire monitoring stations across their entire time series to measure true spatial interpolation capability.
* **Result:** Showed that random CV underestimates true prediction error by `40-70%` under moderate-to-strong spatial autocorrelation. Blocked CV and LOSO provide honest, unbiased estimates of spatial transferability.
* **Limitation:** Blocked CV reduces the effective sample size in training folds and can introduce covariate shift between folds if blocks cover distinct geographic regimes.
* **For AEON-UP:** Non-negotiable evaluation protocol. Random splitting across hourly sensor measurements is forbidden; AEON-UP must evaluate on Leave-One-Station-Out (LOSO) and Spatial Block CV across urban districts.
* **Terms Introduced:** *Spatial autocorrelation, data leakage, spatial block cross-validation, leave-one-station-out (LOSO), effective sample size, Tobler's law.*

---

### Card 14: Andersson et al. (2023) — *Sensor Placement via Epistemic Neural Processes*
* **Citation:** Andersson, T. R., Hosking, J. S., Pérez-Ortiz, M., Paige, B., Elliott, A., Russell, C., Law, S., Jones, D. C., Browne, J., & Lu, H. (2023). *Environmental sensor placement with neural processes.* **Environmental Data Science**, 2, e32. [arXiv:2211.10381](https://arxiv.org/abs/2211.10381) | DOI: [10.1017/eds.2023.27](https://doi.org/10.1017/eds.2023.27).
* **Problem:** Deploying reference monitoring stations is expensive (€20k–€100k per station). Traditional sensor placement methods (e.g., maximizing mutual information on Gaussian Processes) scale poorly (`O(N^3)`) and cannot incorporate multi-modal environmental covariates across complex urban landscapes.
* **Method:** Utilized a trained Convolutional Conditional Neural Process to guide active learning sensor placement. The algorithm computes the model's epistemic uncertainty field across the unmonitored urban grid and iteratively places new candidate sensors at locations that maximize the expected reduction in domain-wide integrated predictive variance:
  `x_new = arg\max_x_*  in X_{candidate} [ Var_epistemic(f(x_*)) . PopulationDensity(x_*) ]`
* **Result:** Achieved superior domain-wide error reduction with `30%` fewer physical sensors compared to classical greedy entropy or random placement strategies across spatio-temporal environmental monitoring grids.
* **Limitation:** Requires an accurately calibrated epistemic uncertainty head; if the NP is overconfident, sensor placement will neglect severely under-sampled regimes.
* **For AEON-UP:** Directly fulfills the translational objective of AEON-UP: turning probabilistic uncertainty estimates into actionable guidance for urban environmental authorities planning sensor network expansions.
* **Terms Introduced:** *Active learning, sensor network design, epistemic variance reduction, acquisition function, population-weighted variance.*

---

### Card 15: Bruinsma et al. (2021) — *The Gaussian Neural Process*
* **Citation:** Bruinsma, W. P., Pervez, P., Foong, A. Y. K., Vaughan, A., Tebbutt, W., & Turner, R. E. (2021). *The Gaussian Neural Process.* **Advances in Neural Information Processing Systems (NeurIPS 2021)**, 34, 21430–21442. [arXiv:2101.03606](https://arxiv.org/abs/2101.03606).
* **Problem:** ConvCNPs output factorized Gaussian marginals `N(u(x_t), sigma^2(x_t))`, failing to model non-trivial joint covariance across target locations `Cov(y_i, y_j)`. Latent NPs model joint covariance via a global latent variable `z`, but suffer from severe training instability (ELBO variational optimization) and underfitting.
* **Method:** Developed the **Gaussian Neural Process (GNP)** and **ConvGNP**. The architecture outputs both a mean function `u(x_t)` and a low-rank plus diagonal parameterization of the full predictive covariance matrix `Sigma(x_T, x_T) = U(x_T) U(x_T)^T + D(x_T)` directly through deterministic neural networks, trained using exact multivariate Gaussian negative log-likelihood without variational approximations.
* **Result:** Enabled deterministic, highly stable training of full joint predictive covariances across arbitrary target query sets, achieving accurate joint trajectory sampling while maintaining translation equivariance.
* **Limitation:** Computing the multivariate Gaussian log-likelihood over `N_t` target points requires inverting an `N_t x N_t` target covariance matrix, scaling cubically `O(N_t^3)` in the number of target evaluation points per task.
* **For AEON-UP:** Represents the advanced frontier for Year 2 of the project if joint spatial realizations (simulating spatial exposure paths) are required without the instability of Latent NPs.
* **Terms Introduced:** *Joint covariance parameterization, ConvGNP, low-rank covariance factor, multivariate log-likelihood, deterministic joint sampling.*

---

# SECTION 2: THE BOTTLENECKS IN HIGH-RESOLUTION URBAN AIR QUALITY

To converse fluently with Dr. Ramacher and Dr. Karl, an applicant must understand why high-resolution urban air quality prediction is an active research bottleneck.

```
+----------------------------------------------------------------------------------------------------+
|                         THE FIVE CORE BOTTLENECKS IN URBAN AIR QUALITY                             |
+------------------------------------+---------------------------------------------------------------+
| BOTTLENECK                         | CORE OBSTACLE & AEON-UP ATTACK VECTOR                         |
+------------------------------------+---------------------------------------------------------------+
| 1. Spatial Sparsity & Sensor Bias  | Regulatory stations sit at expected hotspots (non-random).    |
|                                    | -> AEON-UP: ConvCNP off-grid context conditioning + CTM prior.|
+------------------------------------+---------------------------------------------------------------+
| 2. The Resolution Gap              | CTM grid (1-10 km) vs. exposure gradients (10-50 m).          |
|                                    | -> AEON-UP: SetConv discretization + multi-scale GIS layers.  |
+------------------------------------+---------------------------------------------------------------+
| 3. Non-Stationarity                | Roadside physics != urban background physics.                 |
|                                    | -> AEON-UP: Multi-channel convolutional filters + attention.  |
+------------------------------------+---------------------------------------------------------------+
| 4. Computational Cost of CTMs      | Days of HPC compute per annual city run.                      |
|                                    | -> AEON-UP: Fast neural surrogate (sub-second inference).     |
+------------------------------------+---------------------------------------------------------------+
| 5. Cross-City Transferability      | Urban morphology & emission regimes vary across Europe.       |
|                                    | -> AEON-UP: Meta-learning over episodic city-day tasks.       |
+------------------------------------+---------------------------------------------------------------+
```

---

### Bottleneck 1: Spatial Sparsity and Regulatory Placement Bias
* **The Obstacle:** Official air quality monitoring stations (EEA / AirBase) are extremely sparse. A major European metropolis rarely has more than 10–20 reference stations; for Ultrafine Particles (UFP), cities rarely have more than 1–3 stations. Furthermore, stations are **non-randomly placed**: EU Directives mandate placing stations where maximum concentrations and human exposure are anticipated (traffic hotspots) and at representative urban background sites.
* **Why It Is Hard:** Standard statistical learning assumes training data is independently and identically distributed (i.i.d.) across the geographical feature space. Training directly on regulatory stations introduces severe **selection bias**: the model over-samples polluted roadside environments and under-samples quiet residential micro-environments or suburban periphery, leading to systematic over-estimation of city-wide mean concentrations.
* **What Has Been Tried:** Land-Use Regression (LUR) attempts to regularize with GIS buffer proxies; low-cost sensor networks (e.g., citizen science sensor pods) provide higher density but suffer from severe sensor drift, cross-gas interference (humidity/ozone), and calibration decay.
* **What Remains Open:** Integrating dense, noisy low-cost sensors alongside sparse, high-fidelity reference stations with explicit heteroscedastic observation noise modeling.
* **How AEON-UP Attacks It:** *[Inference]* AEON-UP utilizes ConvCNP context conditioning. By supplying physics-based CTM output (EPISODE-CityChem) as a continuous background prior, the neural process does not rely solely on station interpolation; the stations act as sparse conditioning observations that correct local CTM bias while the CTM preserves domain-wide spatial balance.

---

### Bottleneck 2: The Resolution Gap (Downscaling vs. Emulation vs. Fusion)
* **The Obstacle:** Atmospheric dispersion models operate on grid cells ranging from `1 km x 1 km` (regional) down to `100 m x 100 m` (urban Eulerian). However, human exposure to toxic pollutants (`NO_2`, UFP) varies over distances of `5-20 meters` due to street canyon vortex traps, building wake turbulence, and sharp roadside vehicle exhaust decay curves.
* **The Three Methodological Paradigms:**
  1. **Downscaling:** Mapping a known low-resolution physical field `X_coarse  in \mathbb{R}^H x W` to a high-resolution field `Y_fine  in \mathbb{R}^sH x sW` using static high-resolution GIS covariates (road width, building height, canopy cover).
  2. **Emulation (Surrogate Modeling):** Replacing the expensive physical numerical differential equation solver entirely with a neural network that predicts state `S(t + Delta t)` given `S(t)`, meteorological boundary forcing, and emission rates.
  3. **Data Fusion:** Combining an existing numerical model output (imperfect physics, full spatial coverage) with physical observation stations (ground truth reality, sparse spatial coverage) to produce an optimal unbiased posterior estimate with calibrated uncertainty.
* **Why It Is Hard:** Pure statistical downscaling produces blurred spatial fields unless constrained by mass conservation and microscale flow physics.
* **How AEON-UP Attacks It:** *[Inference]* AEON-UP primarily operates as a **Probabilistic Data Fusion and Downscaling System**. It takes EPISODE-CityChem CTM grids, static spatial proxies (UrbEm, OpenStreetMap), and sparse monitoring stations, fusing them via continuous-to-discrete SetConv layers to output continuous street-level probabilistic predictions.

---

### Bottleneck 3: Spatial Non-Stationarity
* **The Obstacle:** The physical and chemical relationship between environmental predictors and pollutant concentrations is non-stationary across an urban domain. In a deep street canyon with high aspect ratio (`H/W > 1.5`), wind perpendicular to the street creates a helical recirculation vortex: concentrations on the leeward building facade can be `300%` higher than on the windward facade under identical vehicle traffic emissions. Conversely, in an open park or suburban green space, dispersion follows classical Gaussian boundary-layer plumes.
* **Why It Breaks Classical Models:** Standard Gaussian Processes assume a stationary covariance kernel `k(x, x') = k(\|x - x'\|)` (e.g., RBF or Matérn), which enforces a uniform spatial correlation length scale across the entire city. A single global length scale either oversmooths street canyons or introduces spurious oscillations in open areas. Standard linear Land-Use Regression similarly assumes a single global regression coefficient `beta_k` for road density across all neighborhoods.
* **How Convolutional Structure & Attention Help:** 
  - Convolutional layers in ConvCNPs apply localized, multi-scale receptive fields that learn different non-linear feature combinations in dense urban grids versus open suburban terrain.
  - Cross-attention mechanisms (Attentive NPs) dynamically assign variable weights to neighboring stations based on local flow regimes and directional orientation rather than isotropic Euclidean distance.

---

### Bottleneck 4: Computational Scaling and the European Generalization Goal
* **The Obstacle:** Running EPISODE-CityChem or WRF-Chem at `50 m` resolution over hundreds of European cities for multi-year historical periods or real-time operational forecasting is computationally impossible. A single annual city simulation at `100 m` resolution requires hundreds of CPU hours on HPC clusters.
* **Why a Learned Surrogate Matters:** Once trained, a deep convolutional neural process executes in **milliseconds on a single GPU**. A fast probabilistic surrogate enables:
  - Real-time hourly air quality forecasting with interactive municipal dashboards.
  - Monte Carlo policy scenario evaluation (e.g., simulating the city-wide air quality impact of establishing low-emission zones or rerouting diesel freight traffic in seconds rather than weeks).
* **How AEON-UP Attacks It:** *[Inference]* By training the ConvCNP on selected representative European cities with rich EPISODE-CityChem runs (e.g., Hamburg, Rostock, Barcelona), the model learns generalizable mappings from coarse regional CAMS data + UrbEm proxies to street-level concentrations, providing zero-shot downscaling for cities lacking local CTM runs.

---

### Bottleneck 5: Cross-City Transferability and Meta-Learning
* **The Obstacle:** A model trained exclusively on Hamburg fails when deployed to Madrid or Athens. The failure is driven by:
  - **Climatic & Meteorological Shift:** Mediterranean photochemical smog regimes (high solar radiation, intense ozone formation, biogenic VOCs) vs. Northern European advection-dominated regimes.
  - **Urban Morphology Shift:** Dense medieval European street networks vs. modern grid layouts.
  - **Fleet & Emission Shift:** Varying proportions of diesel, electric, wood-burning domestic heating, and industrial point sources.
* **Why Meta-Learning Over Tasks Is the Natural Framing:** Standard supervised learning trains a fixed model to minimize empirical risk on a single dataset. In contrast, **Neural Process Meta-Learning** treats each *city-day* (or *city-month*) as a distinct "task" `tau_i = (C_i, T_i) ~ p(T)`. By training across thousands of synthetic and historical city-day tasks, the network learns the meta-level ability to condition on whatever sparse context sensors `C` are available in a new, unseen city and immediately generate calibrated predictions.

---

### Bottleneck 6: Evaluation Methodology and the Spatial-Leakage Trap
* **The Obstacle:** Atmospheric concentration fields exhibit intense spatial and temporal autocorrelation. If an ML model is evaluated using random `k`-fold cross-validation, the model simply memorizes the temporal signal of adjacent sensors, producing artificially low RMSE and high `R^2` (`>0.90`) that collapse to `R^2 < 0.30` when deployed to a new location.
* **How AEON-UP Must Evaluate:**
  1. **Leave-One-Station-Out (LOSO) Cross-Validation:** Sequentially removing one entire physical monitoring station from the context set `C` and evaluating predictions at that station across the full annual test period.
  2. **Spatial Block Cross-Validation:** Dividing cities into geographic blocks (`5-10 km`) separated by spatial buffer zones to evaluate spatial extrapolation.
  3. **Zero-Shot City Transfer Validation:** Evaluating a model trained on German/Nordic cities directly on an unseen Mediterranean city (e.g., Barcelona) with no gradient parameter updates.

---

### Bottleneck 7: Ultrafine Particles (UFP) Specifically
* **The Unique Challenges:**
  1. **Metric:** UFPs are measured by **Particle Number Concentration (PNC, particles/`cm^3`)**, not mass (`ug/m^3`). A single `10 um` dust particle has the same mass as one billion `10 nm` ultrafine particles, but radically different toxicological and spatial dispersion properties.
  2. **Short Atmospheric Lifetime:** UFPs undergo rapid **coagulation** (small particles colliding to form larger particles) and **condensation/evaporation** within seconds to minutes, causing PNC to drop by an order of magnitude within `50-100 meters` from roadside exhaust pipes.
  3. **Monitoring Vacuum:** There are no legally binding EU ambient concentration limit values for UFP mass or number (only recent monitoring mandates under the revised EU Ambient Air Quality Directive). Consequently, permanent urban CPC stations are virtually non-existent outside specialized research campaigns.
* **How AEON-UP Attacks It:** *[Inference]* Probabilistic neural processes are uniquely suited for UFP because the severe data sparsity demands rigorous uncertainty quantification. Where PNC measurements are absent, the model must output wide epistemic variance reflecting its lack of direct observation, preventing false municipal security.

---

# SECTION 3: THE OPERATIONAL SCRIPT (PHASED WALKTHROUGH)

The following five phases outline the operational execution of the AEON-UP project over the first year.

```
+----------------------------------------------------------------------------------------------------+
|                                THE FIVE OPERATIONAL PHASES                                         |
+----------------------------------------------------------------------------------------------------+
| PHASE 1: Data Assembly, Harmonization, and Geospatial Audit (Months 1-3)                          |
|          Objective: Assemble, project, align, and quality-audit CTM, station, & GIS datasets.     |
+----------------------------------------------------------------------------------------------------+
| PHASE 2: Establishing Classical & Deterministic Baselines (Months 3-4)                             |
|          Objective: Implement non-deep baselines (LUR, Ordinary Kriging, Spatial XGBoost, raw CTM).|
+----------------------------------------------------------------------------------------------------+
| PHASE 3: First Neural Process Architecture & Pipeline Engineering (Months 5-7)                     |
|          Objective: Implement ConvCNP on city-day episodic tasks with translation-equivariant CNN. |
+----------------------------------------------------------------------------------------------------+
| PHASE 4: Uncertainty Quantification, Calibration, and Spatial Diagnostics (Months 8-9)             |
|          Objective: Separate aleatoric/epistemic variance; validate via CRPS, PICP, and LOSO CV.   |
+----------------------------------------------------------------------------------------------------+
| PHASE 5: Physics Coupling, Cross-City Transfer, and Sensor Placement (Months 10-12)                |
|          Objective: Couple CTM priors; evaluate zero-shot city transfer; active learning placement.|
+----------------------------------------------------------------------------------------------------+
```

---

## Phase 1: Data Assembly, Harmonization, and Geospatial Audit
* **Phase Objective in One Sentence:** Construct a unified, reproducible spatio-temporal data ingestion pipeline that harmonizes gridded physical CTM outputs, irregular in-situ monitoring station time series, and static/dynamic geospatial covariates across target European cities into standardized cloud-native formats.
* **What You Would Actually Do:**
  1. **Station Ingestion:** Pull hourly in-situ observations (`NO_2`, `O_3`, `PM_2.5`, `PM_10`, and available PNC/CPC records) from the European Environment Agency (EEA AirBase / E1a/E2a data streams) and Hereon campaign repositories using Python (`requests`, `pandas`).
  2. **CTM Harmonization:** Extract 3D Eulerian hourly netCDF4 files from EPISODE-CityChem and regional CAMS runs using `xarray` and `dask`. Extract surface concentration layers and vertical planetary boundary layer heights (PBLH).
  3. **Covariate Rasterization:** Ingest OpenStreetMap road networks (vector lines), Corine Land Cover / Urban Atlas (polygons), and Global Human Settlement population layers using `geopandas` and `rasterio`. Rasterize vector line sources into multi-scale density rasters (e.g., total road length and primary arterial length within `50 m`, `100 m`, `250 m`, `500 m`, and `1000 m` circular buffers).
  4. **Coordinate Reference System (CRS) Standardization:** Reproject all spatial datasets from geographic coordinates (WGS84, EPSG:4326) into local metric projected coordinate systems (Universal Transverse Mercator, UTM zones, e.g., UTM Zone 32N / EPSG:32632 for Hamburg) to ensure spatial convolutions operate on true Euclidean metric distances.
  5. **Storage:** Store processed, aligned arrays as chunked Zarr / NetCDF4 stores on HPC storage to allow high-throughput parallel data loading during PyTorch training.
* **Decisions Faced & Trade-offs:**
  - *Decision 1: Native Metric Grid Resolution vs. Memory Footprint.*
    - *Option A:* `10 m x 10 m` grid. Resolves narrow street canyons perfectly, but creates massive `3000 x 3000` spatial tensors per city, causing GPU Out-Of-Memory (OOM) errors during mini-batching.
    - *Option B:* `100 m x 100 m` grid. Fits easily in GPU memory, but averages across street canyon road links and building footprints.
    - *Trade-off / Reasonable Approach:* Use a multi-scale internal discretization grid (e.g., `50 m`) coupled with continuous SetConv coordinate queries for sub-grid off-grid stations, or utilize hierarchical patch-based convolutional processing.
  - *Decision 2: Handling Missing Sensor Data.*
    - *Option A:* Impute missing station timestamps using temporal spline interpolation or matrix completion.
    - *Option B:* Treat missingness natively within the Neural Process context set by simply omitting inactive stations from the context set `C` at that timestamp.
    - *Trade-off / Reasoning:* Option B is strongly preferred because Neural Processes are natively designed for variable-sized context sets `|C|`; artificial imputation risks introducing synthetic artifacts into the ground truth evaluation.
* **Technical Terms in Play:** *Coordinate Reference System (CRS), UTM projection, Zarr storage, NetCDF4, xarray chunking, vector rasterization, buffer aggregation, EEA AirBase.*
* **What Could Go Wrong & How It Shows Up:**
  - *Projection distortion:* Forgetting to reproject geographic EPSG:4326 (degrees) into UTM (meters) causes isotropic radial convolution kernels `psi(\|x - x_c\|)` to stretch into anisotropic ellipses, degrading spatial downscaling along north-south vs. east-west axes.
  - *Timestamp misalignment:* Mixing UTC timestamps from CTM/NWP models with local solar/daylight-saving time from municipal sensors causes a 1–2 hour phase shift, showing up as an immediate failure to predict the morning rush-hour traffic peak.
* **What He Would Need to Ask the Group:**
  - *"What are the exact spatial domains, grid projections, and output variable schemas used in your current EPISODE-CityChem and UrbEm production runs?"*
  - *"How are background boundary conditions currently forced at the lateral borders of the urban domain (e.g., CAMS regional vs. nesting)?"*

---

## Phase 2: Baselines Before Anything Clever
* **Phase Objective in One Sentence:** Implement and rigorously evaluate classical geostatistical, machine learning, and physical baseline models under strict spatial validation protocols to establish non-negotiable benchmark targets.
* **What You Would Actually Do:**
  1. **Raw CTM Interpolation:** Evaluate raw EPISODE-CityChem and CAMS outputs interpolated bicubically to ground station coordinates.
  2. **Geostatistical Baseline:** Implement Ordinary Kriging and Spatio-Temporal Kriging using `scikit-gstat` or `PyKrige`, fitting empirical variograms to sensor observations.
  3. **Classical Epidemiological Baseline:** Fit regularized Land-Use Regression (LUR) using ElasticNet regression on buffer-aggregated GIS proxies (road length, population, elevation, land-use fractions).
  4. **Non-Linear Tree Baseline:** Implement Spatial Random Forest and XGBoost regressors ingesting GIS proxies + hourly NWP meteorological vectors (wind speed, wind direction, temperature, PBLH, solar radiation).
  5. **Validation Infrastructure:** Execute all baselines across identical Leave-One-Station-Out (LOSO) folds, computing RMSE, MAE, `R^2`, and CRPS.
* **Decisions Faced & Trade-offs:**
  - *Decision 1: Static LUR vs. Dynamic Spatio-Temporal ML Baselines.*
    - *Option A:* Static LUR predicting annual/monthly means. Standard in epidemiological literature, but cannot be compared directly to hourly CTM runs.
    - *Option B:* Dynamic hourly XGBoost ingesting lagged time-series features + spatial coordinates.
    - *Trade-off / Reasoning:* Both must be built. Static LUR provides the spatial baseline for annual exposure; dynamic XGBoost provides the operational baseline for hourly forecasting.
* **Technical Terms in Play:** *Ordinary Kriging, empirical variogram, nugget-sill-range, Land-Use Regression (LUR), ElasticNet, XGBoost, Leave-One-Station-Out (LOSO), baseline benchmark.*
* **What Could Go Wrong & How It Shows Up:**
  - *Variogram failure in Kriging:* If variogram optimization fails on days with fewer than 5 active stations, Kriging defaults to a flat mean prediction with uninformative variance.
  - *Data leakage in tree models:* Including spatial coordinates `(x, y)` as raw features in XGBoost causes the decision trees to overfit to station latitude/longitude coordinates, scoring high on random CV but failing completely on LOSO validation.
* **What He Would Need to Ask the Group:**
  - *"What statistical or interpolation baselines have been previously benchmarked against EPISODE-CityChem in your published validation studies?"*
  - *"What are the agreed target performance thresholds (e.g., target CRPS or IOA improvements) that define success for the machine learning surrogate?"*

---

## Phase 3: First Neural Process Architecture & Pipeline Engineering
* **Phase Objective in One Sentence:** Design, implement, and train a Convolutional Conditional Neural Process (ConvCNP) in PyTorch that ingests multi-modal gridded physical outputs and irregular station observations to perform episodic downscaling.
* **What You Would Actually Do:**
  1. **Episodic Task Sampler:** Build a PyTorch `Dataset` and `DataLoader` that slices continuous spatio-temporal arrays into discrete "city-day" tasks `tau = (C, T)`. For each task, randomly partition available monitoring stations into context stations `C = ((x_c, y_c))_c=1^N_c` and target evaluation stations `T = ((x_t, y_t))_t=1^N_t`, varying `N_c` dynamically during training.
  2. **SetConv Discretization Layer:** Implement the continuous-to-discrete SetConv layer in PyTorch:
     ```python
     # Functional pseudo-code for SetConv discretization
     # x_context: (B, N_c, 2), y_context: (B, N_c, C_in), grid: (H, W, 2)
     # Computes Gaussian RBF distance between context points and internal grid nodes
     dists = torch.cdist(grid.view(-1, 2), x_context) # (H*W, N_c)
     weights = torch.exp(-0.5 * (dists / lengthscale)**2)
     density = weights.sum(dim=-1, keepdim=True) # (H*W, 1)
     signal = torch.matmul(weights, y_context)    # (H*W, C_in)
     grid_feat = torch.cat([signal / (density + 1e-6), density], dim=-1)
     grid_tensor = grid_feat.view(B, H, W, -1).permute(0, 3, 1, 2)
     ```
  3. **Covariate Concatenation:** Concatenate the discretized context tensor with gridded EPISODE-CityChem CTM concentration channels, UrbEm emission proxies, and meteorological raster fields along the channel dimension.
  4. **Convolutional Backbone:** Pass the unified feature map through a 2D U-Net or ResNet backbone with residual blocks and depthwise separable convolutions to capture multi-scale spatial dispersion.
  5. **Continuous Readout Decoder:** Read out continuous feature vectors at arbitrary target coordinates `x_t` using bilinear or SetConv interpolation, passing them through a shallow MLP head to output predictive Gaussian parameters `(u(x_t), log sigma^2(x_t))`.
  6. **Training Loss:** Train end-to-end using heteroscedastic Gaussian Negative Log-Likelihood (NLL) on the target set `T`.
* **Decisions Faced & Trade-offs:**
  - *Decision 1: Lengthscale Parameterization in SetConv.*
    - *Option A:* Fixed isotropic lengthscale `l` (e.g., `100 m`).
    - *Option B:* Learnable per-channel lengthscale optimized via backpropagation.
    - *Trade-off / Reasoning:* Learnable lengthscale (Option B) allows the network to learn different smoothing widths for different pollutants (narrower for roadside `NO_2`, broader for regional `PM_2.5`).
  - *Decision 2: CNP vs. ConvNP (Deterministic vs. Latent).*
    - *Option A:* Pure deterministic ConvCNP. Highly stable, fast training, exact loss calculation, but factorized marginal predictions.
    - *Option B:* Latent ConvNP with stochastic latent map `Z`. Can draw joint sample paths, but requires variational ELBO optimization and is prone to posterior collapse.
    - *Trade-off / Reasoning:* Start with deterministic ConvCNP (Phase 3); once the pipeline and baselines are rock-solid, evaluate ConvGNP or Latent ConvNP in Phase 5.
* **Technical Terms in Play:** *Episodic task sampling, SetConv layer, density channel, U-Net backbone, heteroscedastic NLL, translation equivariance, context-target split, continuous functional mapping.*
* **What Could Go Wrong & How It Shows Up:**
  - *Density channel gradient explosion:* If density `rho(x) -> 0` in large unmonitored zones, division `y(x) / rho(x)` produces `NaN` gradients. Must be stabilized with epsilon damping `(rho(x) + eps)` or normalized radial basis kernels.
  - *Oversmoothing near roads:* If the convolutional receptive field lacks high-resolution skip connections, the network acts as a low-pass filter, underpredicting sharp roadside spikes.
* **What He Would Need to Ask the Group:**
  - *"What HPC cluster architecture (e.g., Slurm, NVIDIA A100/H100 nodes, PyTorch DDP modules) is available at Hereon for large-scale multi-city neural process training?"*
  - *"What data loader formats are currently preferred within Hereon’s computational pipelines?"*

---

## Phase 4: Uncertainty Quantification, Calibration, and Spatial Diagnostics
* **Phase Objective in One Sentence:** Formulate a rigorous uncertainty decomposition framework separating aleatoric data noise from epistemic model ignorance, and establish full statistical calibration and spatial cross-validation diagnostics.
* **What You Would Actually Do:**
  1. **Uncertainty Decomposition:** Implement Deep Ensembles (`M = 5` randomly seeded ConvCNPs) to capture epistemic model uncertainty, combining ensemble spread with the model's internal heteroscedastic aleatoric head:
     `sigma^2_aleatoric(x_*) = (1)/(M)sum_m=1^M sigma_m^2(x_*), \quad sigma^2_epistemic(x_*) = (1)/(M)sum_m=1^M (u_m(x_*) - mean {u}(x_*))^2`
  2. **Calibration Diagnostics:** Generate **Reliability Diagrams** and **Probability Integral Transform (PIT) histograms** across all validation folds. Compute Prediction Interval Coverage Probability (PICP) and Mean Prediction Interval Width (MPIW) at nominal `50%`, `80%`, `90%`, and `95%` confidence levels.
  3. **Scoring Rule Benchmarking:** Compute Continuous Ranked Probability Scores (CRPS) across all models, evaluating whether the uncertainty estimates are *sharp subject to calibration*.
  4. **Spatial Error Mapping:** Plot 2D spatial maps of predicted concentration `u(x)`, aleatoric variance `sigma^2_aleatoric(x)`, and epistemic variance `sigma^2_epistemic(x)` across the entire urban domain.
* **Decisions Faced & Trade-offs:**
  - *Decision 1: Deep Ensembles vs. Monte Carlo Dropout for Epistemic Variance.*
    - *Option A:* MC Dropout (single model, dropout active at test time). Low storage, single training run, but often yields poor calibration.
    - *Option B:* Deep Ensembles (`M = 5`). Requires `5x` training compute, but consistently delivers state-of-the-art calibration and out-of-distribution detection.
    - *Trade-off / Reasoning:* Deep Ensembles (Option B) are the gold standard in atmospheric ML; use Deep Ensembles for primary evaluation and explore MC Dropout as an efficiency comparison.
* **Technical Terms in Play:** *Aleatoric uncertainty, epistemic uncertainty, Deep Ensembles, Reliability Diagram, PIT histogram, PICP, MPIW, sharpness, proper scoring rules, CRPS.*
* **What Could Go Wrong & How It Shows Up:**
  - *Overconfidence in extrapolation zones:* Epistemic uncertainty fails to increase in regions far from any monitoring station. Diagnosed via PIT histograms showing U-shaped distributions (under-dispersion / overconfidence).
  - *Variance misattribution:* The aleatoric head absorbs all error, leaving epistemic variance flat near zero. Requires regularizing the heteroscedastic loss or enforcing prior bounds.
* **What He Would Need to Ask the Group:**
  - *"How do municipal stakeholders and epidemiologists currently interpret uncertainty bounds in Hereon’s environmental reports?"*
  - *"Are specific coverage nominals (e.g., `95%` confidence intervals) required for regulatory compliance reporting?"*

---

## Phase 5: Coupling to Physics, Cross-City Transfer, and Sensor Placement
* **Phase Objective in One Sentence:** Seamlessly couple physics-based CTM priors into the neural process architecture, evaluate zero-shot and few-shot spatial generalization to unseen European metropolises, and deploy active learning for optimal sensor network expansion.
* **What You Would Actually Do:**
  1. **Physical Prior Integration:** Implement and compare three physical coupling paradigms:
     - *Coupling Mode A (Input Covariate):* Ingest CTM concentration fields as standard multi-channel input rasters.
     - *Coupling Mode B (Residual / Delta Learning):* Set the model's base prior mean `u_0(x)` equal to the CTM physical prediction, forcing the neural process to learn only the residual error `Delta(x) = y_observed(x) - y_CTM(x)`.
     - *Coupling Mode C (Physics-Informed Loss):* Incorporate soft physical constraints (e.g., 2D steady-state advection-diffusion mass conservation penalties) into the training loss:
       `L_total = L_NLL + lambda \|grad . (u C) - grad . (K grad C) + Sinks - Sources\|^2`
  2. **Cross-City Transfer Benchmark:** Evaluate model transferability:
     - *Zero-Shot Transfer:* Train on German cities (Hamburg, Rostock) and evaluate directly on an unseen European city (e.g., Barcelona) using only CTM priors and local UrbEm proxies (`N_c = 0`).
     - *Few-Shot Conditioning:* Sequentially add 1, 2, 5, and 10 local monitoring stations into context set `C` to quantify how rapidly the ConvCNP adapts to local city regimes without parameter retraining.
  3. **Active Learning Sensor Placement:** Implement an acquisition function based on integrated epistemic variance reduction to generate spatial heatmaps identifying optimal locations for deploying new physical monitoring stations or mobile sensor campaigns.
* **Decisions Faced & Trade-offs:**
  - *Decision 1: Direct Prediction vs. Residual / Bias-Correction Modeling.*
    - *Option A:* Direct prediction of absolute concentrations. Flexible, but can produce physically unrealistic fields if data is sparse.
    - *Option B:* Residual / Delta learning on top of EPISODE-CityChem. Preserves the physical transport structure of the CTM everywhere, learning only local systematic bias.
    - *Trade-off / Reasoning:* Residual learning (Option B) is heavily favored when high-quality CTM runs are available; direct prediction is necessary when transferring to cities where CTM runs do not exist.
* **Technical Terms in Play:** *Residual learning, physics-informed neural network (PINN), mass conservation loss, zero-shot transfer, few-shot meta-learning, active learning, sensor placement optimization, domain generalization.*
* **What Could Go Wrong & How It Shows Up:**
  - *Negative transfer on unseen cities:* When applied to a Mediterranean city, the model severely underpredicts ozone/NOx photochemistry due to unobserved solar radiation differences. Requires normalizing meteorological covariates across European climatic zones.
  - *Physical violation in residual learning:* Unconstrained residual learning predicting negative total concentrations in clean background zones. Requires passing predictions through a non-negative rectifier (e.g., Softplus activation).
* **What He Would Need to Ask the Group:**
  - *"Which European partner cities within AEON-UP are designated as primary testbeds for cross-city transferability?"*
  - *"Is the ultimate deployment intended as a standalone emulator for cities without CTMs, or as an operational data-assimilation layer on top of active EPISODE-CityChem runs?"*

---
