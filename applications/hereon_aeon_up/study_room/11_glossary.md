# 11. The AEON-UP Comprehensive Technical Glossary

> **Document Purpose:** A complete, rapid-review lexicon of all technical terms across the study room and operational blueprints.
> **How to Use:** Skim on the morning of the interview. 
> - `[ACTIVE USE]` indicates terms Thejus should speak aloud and integrate naturally into his explanations.
> - `[RECOGNITION ONLY]` indicates terms he should understand when spoken by Dr. Ramacher or Dr. Karl without necessarily initiating them.

---

## 1. Atmospheric Science & Environmental Chemistry

* **Chemistry Transport Model (CTM)** `[ACTIVE USE]`  
  A numerical simulation system that solves the 3D advection-diffusion-reaction equations to simulate the transport, physical mixing, chemical transformation, and deposition of atmospheric pollutants.
* **EPISODE-CityChem** `[ACTIVE USE]`  
  An urban-scale Eulerian chemistry transport model developed at Hereon that couples grid-based advection-diffusion with sub-grid street canyon and point source dispersion models to predict city-scale air quality at `100-1000 m` resolution.
* **Ultrafine Particles (UFP)** `[ACTIVE USE]`  
  Aerosol particles with an aerodynamic diameter smaller than `100 nanometers` (`D_p < 0.1 um`), characterized by negligible mass but immense particle number concentration and high pulmonary penetration.
* **Particle Number Concentration (PNC)** `[ACTIVE USE]`  
  The total number of aerosol particles per unit volume of air (typically reported in `particles/cm^3`), which serves as the primary metric for ultrafine particles rather than mass concentration (`ug/m^3`).
* **Condensation Particle Counter (CPC)** `[RECOGNITION ONLY]`  
  An optical instrument that grows ultrafine particles through supersaturated vapor condensation until they reach detectable sizes for laser counting.
* **Planetary Boundary Layer Height (PBLH)** `[ACTIVE USE]`  
  The vertical altitude of the turbulent lower troposphere directly influenced by the Earth's surface; a low PBLH severely restricts vertical mixing and traps surface emissions near ground level.
* **Temperature Inversion** `[ACTIVE USE]`  
  A meteorological condition where atmospheric temperature increases with altitude, suppressing vertical convective turbulence (`K_z -> 0`) and causing severe, prolonged winter pollution episodes.
* **Street Canyon Effect** `[ACTIVE USE]`  
  The microscale aerodynamic trapping of vehicle exhaust between continuous tall buildings, forming a recirculation vortex that creates extreme concentration discrepancies between windward and leeward facades.
* **Simplified Street Canyon Model (SSCM)** `[RECOGNITION ONLY]`  
  The sub-grid parameterized dispersion module within EPISODE-CityChem used to compute localized line-source concentrations inside urban street canyons.
* **Photostationary State (`NO-NO_2-O_3`)** `[ACTIVE USE]`  
  The rapid daytime chemical equilibrium established between nitric oxide (`NO`), nitrogen dioxide (`NO_2`), and ozone (`O_3`) driven by solar ultraviolet photolysis and ozone titration.
* **Secondary Organic Aerosols (SOA)** `[RECOGNITION ONLY]`  
  Particulate matter formed in the atmosphere through the oxidation of volatile organic compounds (VOCs) followed by gas-to-particle condensation.
* **Aerosol Coagulation** `[ACTIVE USE]`  
  The physical microphysical process whereby colliding ultrafine particles adhere to form larger particles, rapidly reducing total particle number concentration while conserving total mass.
* **Dry / Wet Deposition** `[ACTIVE USE]`  
  The removal of atmospheric pollutants at the Earth's surface via turbulent impaction/absorption on vegetation/soil (dry) or scavenging by precipitation (wet).
* **Advection-Diffusion-Reaction Equation** `[ACTIVE USE]`  
  The partial differential equation governing the conservation of mass for a pollutant species under mean wind transport, turbulent eddy diffusion, and chemical kinetics.
* **K-Theory (Eddy Diffusivity)** `[ACTIVE USE]`  
  The first-order atmospheric turbulence closure model assuming turbulent pollutant fluxes are linearly proportional to the local mean concentration gradient.
* **Operator Splitting** `[ACTIVE USE]`  
  A numerical method in CTMs that separates the stiff coupled differential equations into sequential discrete steps: advection, diffusion, chemistry, and deposition.
* **CAMS-REG / EMEP** `[ACTIVE USE]`  
  Copernicus Atmosphere Monitoring Service Regional and European Monitoring and Evaluation Programme regional emission inventories gridded across Europe at `6-10 km` resolution.
* **UrbEm** `[ACTIVE USE]`  
  An open-source top-down emission downscaling model developed by Dr. Martin Ramacher that uses high-resolution spatial proxies (OSM, Urban Atlas) to disaggregate regional emissions onto street-level urban grids.
* **GNFR Sectors** `[RECOGNITION ONLY]`  
  Gridded Nomenclature for Reporting: standardized source activity classifications (e.g., transport, public power, residential heating) used in European emission inventories.
* **Land-Use Regression (LUR)** `[ACTIVE USE]`  
  A classical spatial statistical modeling technique in environmental epidemiology that predicts ambient pollutant concentrations using multivariable linear regression on buffer-aggregated GIS predictor variables.

---

## 2. Statistics & Uncertainty Quantification

* **Aleatoric Uncertainty** `[ACTIVE USE]`  
  Inherent, irreducible stochastic noise in data generated by physical turbulence, microscale weather variations, or hardware measurement error, which cannot be reduced by collecting more training data.
* **Epistemic Uncertainty** `[ACTIVE USE]`  
  Reducible uncertainty stemming from the model's lack of knowledge or data in unobserved spatial regions, which directly indicates where new monitoring stations should be deployed.
* **Heteroscedastic Loss** `[ACTIVE USE]`  
  A loss formulation where the predictive variance is modeled as an explicit function of the input coordinates `sigma^2(x)` rather than assumed constant across the entire domain.
* **Continuous Ranked Probability Score (CRPS)** `[ACTIVE USE]`  
  A strictly proper scoring rule that measures the integrated squared distance between a predictive cumulative distribution function and the empirical Heaviside step function of the observation, reported in physical units (`ug/m^3`).
* **Proper Scoring Rule** `[ACTIVE USE]`  
  A statistical evaluation loss function that is uniquely minimized when the forecaster issues the true underlying probability distribution of the data, penalizing overconfidence and miscalibrated spread.
* **Reliability Diagram** `[ACTIVE USE]`  
  A calibration diagnostic plot comparing nominal prediction interval confidence levels (e.g., `50%, 80%, 95%`) against the empirical percentage of true observations contained within those intervals.
* **Prediction Interval Coverage Probability (PICP)** `[ACTIVE USE]`  
  The empirical percentage of true test observations that fall within a specified `(1 - alpha)` predictive interval.
* **Mean Prediction Interval Width (MPIW)** `[ACTIVE USE]`  
  The average spatial width of predictive confidence intervals, used alongside PICP to assess whether uncertainty estimates are sharp (narrow) while maintaining nominal coverage.
* **Probability Integral Transform (PIT) Histogram** `[ACTIVE USE]`  
  A diagnostic tool for continuous probabilistic forecasts; a perfectly calibrated model yields a flat, uniform PIT histogram, while U-shaped histograms signal under-dispersion (overconfidence).
* **Sharpness** `[ACTIVE USE]`  
  The property of a probabilistic forecast describing the concentration or tightness of the predictive distribution; forecasters seek maximum sharpness subject to statistical calibration.
* **Deep Ensembles** `[ACTIVE USE]`  
  A scalable, highly competitive uncertainty estimation method that trains `M` independent neural networks initialized with different random seeds and combines their predictive distributions into a Gaussian mixture.
* **Monte Carlo (MC) Dropout** `[ACTIVE USE]`  
  An epistemic uncertainty approximation technique that keeps dropout layers active during test time, generating empirical predictive distributions across multiple stochastic forward passes.
* **Spatial Autocorrelation** `[ACTIVE USE]`  
  The statistical correlation of a variable with itself across geographical space (Tobler's First Law: near things are more related than distant things).
* **Spatial Data Leakage** `[ACTIVE USE]`  
  The artificial inflation of model validation scores occurring when training and test sets are split randomly across spatially autocorrelated sensor data.
* **Leave-One-Station-Out (LOSO) Cross-Validation** `[ACTIVE USE]`  
  A rigorous spatial validation protocol where entire monitoring stations are sequentially held out from training to evaluate the model's true spatial interpolation capability.
* **Spatial Block Cross-Validation** `[ACTIVE USE]`  
  A validation strategy that partitions the geographic study domain into contiguous spatial blocks or tiles separated by buffer zones to test spatial extrapolation.
* **Variogram (Semivariogram)** `[RECOGNITION ONLY]`  
  A geostatistical function describing the degree of spatial dependence between two observation points as a function of the distance separating them.
* **Ordinary Kriging** `[ACTIVE USE]`  
  The classical linear spatial interpolation method that calculates best linear unbiased predictions (BLUP) based on an empirical variogram model; mathematically equivalent to a Gaussian Process with a fixed kernel.

---

## 3. Machine Learning & Neural Processes

* **Gaussian Process (GP)** `[ACTIVE USE]`  
  A non-parametric Bayesian framework that defines a prior distribution over continuous functions, providing exact closed-form conditioning but suffering from `O(N^3)` computational scaling.
* **Conditional Neural Process (CNP)** `[ACTIVE USE]`  
  A deterministic neural network architecture that approximates Gaussian Process conditioning in `O(N_c + N_t)` linear time using independent context encoders, permutation-invariant mean aggregation, and target decoders.
* **Neural Process (NP / Latent NP)** `[ACTIVE USE]`  
  A probabilistic extension of CNPs that introduces a global stochastic latent variable `z ~ q(z|C)` trained via variational ELBO, enabling the generation of globally correlated functional sample paths.
* **Attentive Neural Process (ANP)** `[ACTIVE USE]`  
  A Neural Process architecture that replaces uniform mean aggregation with multi-head cross-attention over context points, resolving the severe underfitting failure mode of standard CNPs near sensors.
* **Convolutional Conditional Neural Process (ConvCNP)** `[ACTIVE USE]`  
  A Neural Process architecture that maps off-grid context data onto an internal grid via continuous SetConv layers, applies deep translation-equivariant 2D CNNs, and decodes to continuous coordinates.
* **Translation Equivariance** `[ACTIVE USE]`  
  A mathematical property of operators where shifting the input coordinates in space produces an identically shifted output field (`f(T_v x) = T_v f(x)`), fundamental for spatial geospatial modeling.
* **SetConv Layer (Continuous Convolution)** `[ACTIVE USE]`  
  A continuous-to-discrete neural layer that projects irregular off-the-grid context observations `(x_c, y_c)` onto an internal regular grid using radial basis smoothing kernels, outputting both signal and density channels.
* **Density Channel `rho(x)`** `[ACTIVE USE]`  
  A normalized spatial channel in SetConv that encodes the local geographical density and proximity of context observation points, allowing the network to modulate confidence and detect extrapolation voids.
* **Context Set `C`** `[ACTIVE USE]`  
  The subset of known observation pairs `C = ((x_c, y_c))_c=1^N_c` available to condition the model at inference time.
* **Target Set `T`** `[ACTIVE USE]`  
  The query coordinate locations `T = (x_t)_t=1^N_t` where the model is evaluated or required to make probabilistic predictions.
* **Episodic Task Training** `[ACTIVE USE]`  
  The meta-learning training protocol where data is sampled as discrete tasks `tau = (C, T)` with randomly varying context sizes, training the model to generalize across arbitrary sensor configurations.
* **Evidence Lower Bound (ELBO)** `[ACTIVE USE]`  
  The objective function maximized in variational Bayesian inference and Latent Neural Processes, balancing target data likelihood against the KL divergence between posterior and prior latent distributions.
* **Posterior Collapse** `[ACTIVE USE]`  
  A common failure mode in variational generative models and Latent NPs where the decoder ignores the stochastic latent variable `z`, causing the variational posterior to collapse to the uninformative prior.
* **Gaussian Neural Process (GNP / ConvGNP)** `[ACTIVE USE]`  
  A Neural Process architecture that outputs deterministic, low-rank parameterizations of the full joint predictive covariance matrix across target points, avoiding variational ELBO instability.
* **Residual / Delta Learning** `[ACTIVE USE]`  
  A hybrid modeling paradigm where the neural network is trained to predict only the error residual `Delta = y_observed - y_CTM` on top of a physics-based base model rather than predicting absolute values.
* **Physics-Informed Neural Network (PINN)** `[ACTIVE USE]`  
  A neural network trained with a composite loss function containing terms that penalize violations of governing physical partial differential equations (such as mass conservation).
* **Zero-Shot / Few-Shot Spatial Transfer** `[ACTIVE USE]`  
  Evaluating a trained model on a completely unseen city without updating parameters (`N_c = 0`, zero-shot) or updating predictions solely by feeding 1–5 local context sensors (`N_c > 0`, few-shot).
* **Active Learning / Sensor Placement** `[ACTIVE USE]`  
  A Bayesian experimental design technique that uses the model's spatial epistemic uncertainty field as an acquisition function to identify optimal coordinates for deploying new physical sensors.

---

## 4. High-Performance Computing & Geospatial Data

* **NetCDF4 / HDF5** `[ACTIVE USE]`  
  Hierarchical, self-describing scientific array data formats universally used in atmospheric and ocean modeling to store multi-dimensional spatio-temporal variables.
* **Zarr** `[ACTIVE USE]`  
  A modern, cloud-optimized chunked, compressed, N-dimensional array storage format designed for parallel, high-throughput I/O in Python and PyTorch.
* **xarray & Dask** `[ACTIVE USE]`  
  Python libraries for labeled multi-dimensional array manipulation and out-of-core distributed computation across HPC clusters.
* **Coordinate Reference System (CRS)** `[ACTIVE USE]`  
  A standardized coordinate framework (e.g., EPSG codes) that defines how two-dimensional projected maps relate to real locations on the Earth's curved surface.
* **Universal Transverse Mercator (UTM)** `[ACTIVE USE]`  
  A conformal metric map projection system that divides the Earth into 60 zones, providing local Euclidean distance measurements in meters with minimal distortion.
* **WGS84 (EPSG:4326)** `[ACTIVE USE]`  
  The standard unprojected spherical latitude/longitude coordinate reference system in angular degrees.
* **Rasterio & GeoPandas** `[ACTIVE USE]`  
  Geospatial Python libraries used for manipulating gridded raster imagery (GeoTIFFs) and vector GIS polygons/lines (Shapefiles, GeoJSON).
* **PyTorch Distributed Data Parallel (DDP)** `[ACTIVE USE]`  
  The standard multi-GPU training paradigm in PyTorch that replicates model instances across GPU ranks and synchronizes gradients via ring-AllReduce communication.
* **Slurm Workload Manager** `[ACTIVE USE]`  
  The standard open-source job scheduler used on high-performance computing clusters to allocate GPU compute nodes, CPUs, and memory.

---
