# 07. Spaced Repetition Flashcards: Core Concepts and Active Recall

> **Instructions:** Review daily. Format is strictly: Question on one line (`Q:`), Answer on the very next line (`A:`).

---

Q: What is a Neural Process (NP) in simple terms?
A: A probabilistic deep learning framework that parameterizes stochastic processes using neural networks, combining the uncertainty estimation of Gaussian Processes with O(N_c + N_t) linear scaling.

Q: What fatal conceptual trap must be avoided regarding the term 'neural processes'?
A: Never confuse Neural Processes with mechanistic interpretability, transformer attention visualization, linear probes, or biological neurology; it is strictly a mathematical framework for approximating stochastic functions.

Q: What is the computational complexity of exact Gaussian Process regression and why does it fail for urban air quality?
A: O(N^3) time and O(N^2) memory due to matrix inversion of the kernel, which becomes intractable when evaluating hundreds of thousands of hourly urban sensor observations.

Q: How does a Conditional Neural Process (CNP) achieve O(N_c + N_t) linear time complexity?
A: By encoding each context point independently into R^d with an MLP, aggregating representations with a permutation-invariant mean, and decoding target locations alongside this mean vector.

Q: What is the primary cause of underfitting in standard Conditional Neural Processes (CNP)?
A: The mean aggregation bottleneck, which averages all context representations uniformly, washing out localized high-frequency peaks near specific active sensors.

Q: How did the Attentive Neural Process (ANP) solve the CNP underfitting problem?
A: By replacing uniform mean aggregation with a cross-attention mechanism, querying context keys using target location queries so the decoder focuses on nearby sensors.

Q: Why is Translation Equivariance essential for spatial atmospheric modeling?
A: Because physical dispersion fluid dynamics operate identically regardless of absolute spatial coordinates; shifting the emission source and wind vector shifts the resulting concentration plume by the exact same offset.

Q: How does the ConvCNP architecture ingest sparse, off-the-grid sensor data into a convolutional neural network?
A: Through a continuous discretization layer that maps sensor points onto an internal grid using kernel smoothing, creating a signal channel and a continuous density channel.

Q: What is the purpose of the 'density channel' d_0 in a ConvCNP?
A: It indicates where data was observed: high density tells the CNN that real measurements exist nearby (low epistemic variance), while zero density forces the model to rely on the physical CTM prior (high epistemic variance).

Q: What is EPISODE-CityChem?
A: An urban-scale Chemistry Transport Model developed at Hereon by Dr. Matthias Karl that embeds sub-grid Gaussian line/point source models and fast photochemistry into a 3D Eulerian main grid.

Q: Why does Nitrogen Dioxide (NO2) exhibit sharp 50-meter spatial gradients near roadways while PM2.5 is spatially smooth?
A: NO2 is directly emitted as NO and rapidly titrated by ozone within meters of vehicle tailpipes with a short chemical lifetime, whereas PM2.5 is dominated by long-lived regional secondary aerosols.

Q: What is the size definition of Ultrafine Particles (UFP) and what metric is used to measure them?
A: Particles with aerodynamic diameter under 100 nm (0.1 micrometers), measured by Particle Number Concentration (PNC in particles/cm3), not by mass.

Q: Why is mass concentration (micrograms/m3) useless for measuring Ultrafine Particles?
A: Because a single 10-micrometer particle has the mass of 1,000,000 UFP particles; UFP accounts for < 1% of particulate mass but > 80-90% of total particle numbers.

Q: Are Ultrafine Particles regulated by legally binding EU mass limit values under current directives?
A: No; current EU directives have no binding numerical limit values for UFP, though the revised 2024 directive introduces mandatory monitoring at urban supersites.

Q: What microphysical process causes high concentrations of UFP to decay extremely rapidly in the first minutes after emission?
A: Coagulation, which follows a second-order rate law proportional to N^2 (dN/dt = -K * N^2), causing particles to rapidly collide and merge into larger accumulation-mode particles.

Q: What is Aleatoric Uncertainty and can it be reduced by adding more monitoring stations?
A: Inherent, irreducible stochasticity from physical turbulence or sensor hardware noise; it cannot be reduced by adding more sensors.

Q: What is Epistemic Uncertainty and what is its operational consequence for sensor placement?
A: Model uncertainty caused by lack of spatial data or unseen regimes; it is reducible with more data, meaning new monitoring stations should be placed in areas of high epistemic uncertainty.

Q: What is a Strictly Proper Scoring Rule?
A: A loss or evaluation metric where the expected penalty is uniquely minimized if and only if the predicted probability distribution matches the true data-generating distribution.

Q: What are the units of Continuous Ranked Probability Score (CRPS) and what does it equal when predictive variance collapses to zero?
A: CRPS has the exact physical units of the target pollutant (e.g. ug/m3 or particles/cm3), and collapses exactly to Mean Absolute Error (|y - mu|) when variance reaches zero.

Q: What is the Prediction Interval Coverage Probability (PICP) for a well-calibrated 90% confidence interval?
A: Exactly 0.90 (90% of held-out observations fall within the predicted 5th and 95th percentiles).

Q: What does a U-shaped Probability Integral Transform (PIT) histogram indicate?
A: An overconfident (underdispersed) model where prediction intervals are too narrow and true values frequently fall in the extreme tails.

Q: Why is Random K-Fold Cross-Validation invalid for spatio-temporal air quality data?
A: It creates the spatial-leakage trap by allowing temporally adjacent measurements from the same physical monitoring station into both training and validation sets, inflating R^2 and underestimating epistemic uncertainty.

Q: What spatial cross-validation protocol must be used instead of random splitting?
A: Leave-One-Station-Out (LOSO) or Spatial Block Cross-Validation, which completely holds out entire physical monitoring stations across all time steps.

Q: What was the title and purpose of the 2024 ECMWF Code for Earth project mentored by Dr. Martin Ramacher?
A: 'Urban Air Quality View' - exploring machine learning models to downscale regional CAMS pollutant products to urban scale using open geospatial datasets in Barcelona.

Q: What was Thejus' exact role and accomplishment during the HealthTwiSt Praxisphase?
A: Refactored a production R/tidyverse pipeline for a national medical registry across 143,000 records from 300 clinics, verified byte-identical at every step, and externalized 257 hard-coded rules into configuration.

Q: How should Thejus answer when asked about his machine learning publication record?
A: Acknowledge openly that his peer-reviewed papers are in computational physical modeling and simulation, while highlighting his hands-on PyTorch engineering, HPC parallelization, and ability to build production ML pipelines from day one.
