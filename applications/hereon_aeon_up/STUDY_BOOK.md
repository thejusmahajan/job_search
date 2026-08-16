# Study book — AEON-UP, Probabilistic Deep Learning for Urban Air Quality

For the Hereon postdoc (ref. 1056, deadline 3 Sept 2026, start 1 Oct 2026).
Written to get you from "I can defend my own project" to "I can hold a technical
conversation about theirs."

**Honest framing of the gap.** You are strong on the physical modelling, the
spatio-temporal data and the HPC. You are strong on PyTorch as of this year. The
gap is *probabilistic* deep learning — specifically **neural processes**, which
the advert names explicitly. That is what this document is for. Nothing here
should be claimed as experience; it is reading, so that you can ask good
questions and not be lost when they explain the project.

---

## 1. What the project actually is

> "Combining physics-based chemistry transport models with probabilistic deep
> learning methods, in particular **neural processes**, to generate high-resolution
> predictions of NO₂, particulate matter and ultrafine particles across European
> cities, **alongside uncertainty estimates**."

Decoded, that is four separate things:

1. **A physics model** (a chemistry transport model, CTM) that simulates emission,
   advection, chemistry and deposition on a grid. Hereon's coastal chemistry
   institute runs **CMAQ** (Community Multiscale Air Quality, originally US EPA) —
   an Eulerian grid model — over the North Sea and European domains.
2. **Observations** from monitoring stations: sparse, irregularly placed, accurate.
3. **A learned model** that fuses (1) and (2) to produce predictions at a resolution
   the CTM alone cannot reach — city-scale, street-scale.
4. **Calibrated uncertainty** on every prediction.

The reason this is hard, and interesting: the CTM is physically consistent but
coarse and biased; the stations are accurate but almost everywhere absent. You need
something that interpolates between stations *conditioned on* the physics, and that
knows how much to trust itself far from a station.

---

## 2. Why neural processes, and not something else

### The lineage: Gaussian processes → neural processes

A **Gaussian process (GP)** is the classical answer to "interpolate from scattered
observations and give me error bars." It defines a distribution over functions; you
condition on observed points and read off a mean and variance anywhere else. In
geoscience you have met this as **kriging**.

GPs have two problems at this scale:
- Cost is **O(n³)** in the number of observations — prohibitive for large datasets.
- You must choose a kernel, which hard-codes your assumptions about smoothness and
  correlation structure. Air pollution near a road is not smooth.

A **neural process (NP)** keeps what you want from a GP — condition on a context
set, predict with uncertainty at arbitrary target locations — but *learns* the
mapping with neural networks instead of specifying a kernel, and runs in **O(n)**.

### The mechanism, in one paragraph

An NP has an **encoder** that maps each observed (input, output) pair to a
representation, **aggregates** those representations (typically by averaging, which
makes the model invariant to the order of observations — an important property), and
a **decoder** that takes the aggregate plus a target location and outputs a
predictive distribution, usually a Gaussian mean and variance. Training is
**meta-learning**: each training example is not a data point but a *task* — a random
split of a field into context and target points. The model learns "how to
interpolate this kind of field," not "this particular field."

That last point is why NPs suit AEON-UP. Trained across many cities and time
windows, the model learns the general structure of urban pollution fields, then
adapts to a new city or day from whatever handful of stations exist there.

### The three you should be able to distinguish

| Model | Idea | Weakness |
|---|---|---|
| **Conditional NP (CNP)** — Garnelo et al., 2018 | Deterministic encoding; decoder outputs a Gaussian per target point | Predictions at different targets are independent given the context; cannot produce coherent function samples |
| **Neural Process (NP)** — Garnelo et al., 2018 | Adds a **latent variable** for global uncertainty; trained with a variational bound | Underfits; tends to produce blurry means |
| **Attentive NP (ANP)** — Kim et al., 2019 | Replaces mean-aggregation with **attention**, so a target point attends to the context points relevant to it | More expensive; still the usual default |

**The underfitting problem of vanilla NPs, and why ANP exists, is the single best
thing to understand.** Mean-aggregation forces every target to see the same summary
of the context; attention lets a target near a station weight that station heavily.
For air quality — where a prediction 200 m from a monitor should look very different
from one 5 km away — this matters enormously.

Also worth knowing by name: **ConvCNP** (Gordon et al., 2020), which builds in
translation equivariance and is a natural fit for gridded spatial data, and
**Transformer Neural Processes**. If they are working on gridded CTM output, ConvCNP
is likely in the conversation.

> **Your entry point.** You have just spent months inside attention mechanisms in a
> transformer. The ANP is attention applied to exactly this problem. That is not a
> stretch to claim — it is a genuine, specific connection, and it is the thing to say
> in an interview.

---

## 3. Uncertainty: the vocabulary you must have exactly right

This is the part where being imprecise will be noticed.

**Aleatoric uncertainty** — irreducible noise in the data itself. Sensor error,
turbulent fluctuation. More data does not reduce it. Can be *homoscedastic*
(constant) or *heteroscedastic* (input-dependent — near a busy road, variance is
higher). In air quality it is largely heteroscedastic, which matters.

**Epistemic uncertainty** — uncertainty in the model, from having seen limited data.
It *is* reducible with more data, and it is what should grow as you move away from a
monitoring station. If your model is confident in a district with no sensors,
something is wrong.

**A good AEON-UP model must separate these.** "The uncertainty is high here" is much
less useful than "the uncertainty is high here *because we have no measurements
nearby*" versus "*because this location is intrinsically noisy*". The first is an
argument for placing a sensor; the second is not.

### How uncertainty is obtained in practice

- **Deep ensembles** (Lakshminarayanan et al., 2017) — train N models with different
  initialisations; spread of predictions estimates epistemic uncertainty. Simple,
  strong, embarrassingly parallel, and a natural fit for HPC. Often the baseline to
  beat.
- **MC dropout** (Gal & Ghahramani, 2016) — keep dropout on at inference and sample.
  Cheap; theoretically contested; still widely used.
- **Bayesian neural networks / variational inference** — place distributions over
  weights. Principled, harder to scale.
- **Heteroscedastic regression** — have the network output both μ and σ² and train
  with the Gaussian negative log-likelihood. This is the aleatoric half, and it is
  what an NP decoder does.

---

## 4. Evaluation — how you prove the uncertainty is any good

A model can have well-shaped uncertainty that is *wrong*. Know these:

**Proper scoring rules.** A scoring rule is *proper* if it is optimised by reporting
your true belief — it cannot be gamed by over- or under-confidence.
- **CRPS** (Continuous Ranked Probability Score) — the standard for probabilistic
  forecasts of a continuous variable; generalises MAE to distributions. Learn this
  one properly, it will come up.
- **Negative log-likelihood** — proper, but punishes tail errors harshly.
- Reference: Gneiting & Raftery (2007), *Strictly Proper Scoring Rules, Prediction,
  and Estimation* — the canonical paper.

**Calibration.** If you issue 90% prediction intervals, do 90% of observations fall
inside them? Assess with a **reliability diagram** or a calibration/PIT plot. A model
can be sharp and miscalibrated, or calibrated and useless (predicting the climatology
with huge intervals). You want **sharpness subject to calibration** — Gneiting's
formulation, and a phrase worth using.

**Spatial cross-validation.** Ordinary random k-fold leaks: neighbouring points are
correlated, so a random split puts near-duplicates in train and test and flatters
the model. Use **leave-one-station-out** or spatially blocked CV. *This is exactly
the kind of silent methodological error you have made a habit of catching — say so.*

---

## 5. The domain: enough air quality to be credible

**The pollutants**
- **NO₂** — traffic-dominated, very sharp spatial gradients (roadside vs background
  differs within tens of metres). The hardest to downscale, and the reason
  high-resolution prediction matters.
- **PM₂.₅ / PM₁₀** — particulate matter by aerodynamic diameter in μm. Mixed local
  and long-range transported; smoother fields; substantial secondary formation
  (sulfate, nitrate, organics) which is why the chemistry in a CTM matters.
- **Ultrafine particles (UFP, < 100 nm)** — measured by *number* not mass, very
  short-lived, extremely local, sparsely monitored, and **not currently regulated by
  EU limit values**. This is the frontier pollutant, and the fact that AEON-UP names
  it tells you the project is aimed at where the science is thin. Hereon has a
  particular interest here.

**The physical drivers** to be able to name: emissions (traffic, shipping, domestic
heating, industry); meteorology (wind speed and direction, boundary-layer height,
temperature inversions — which trap pollution); chemistry (NOₓ–O₃ titration, secondary
aerosol formation); deposition. **Boundary-layer height** and **inversions** are the
meteorological terms that most explain why concentrations spike.

**The scale problem, which is the heart of the project.** A CTM run at, say, 1–4 km
grid spacing cannot resolve a street canyon. Urban exposure varies over metres.
Bridging that gap is *downscaling*, and the ML options are:
- **Bias correction** — learn the CTM's systematic error against observations
- **Emulation** — learn a fast surrogate of the expensive CTM
- **Data fusion / statistical downscaling** — combine CTM fields with station data and
  covariates (land use, road density, population, satellite NO₂) at high resolution

Also know **land-use regression (LUR)**, the classical statistical approach to urban
air quality mapping — it is the baseline any ML method will be compared against.

**Why coastal is a Hereon speciality:** sea-breeze circulation, shipping emissions,
and sharp land–sea contrasts in boundary-layer structure. Your marine background is
not incidental here.

---

## 6. What you already have (do not undersell this)

| They want | You have |
|---|---|
| Spatio-temporal / geospatial data | ERGOM, GOTM-FABM, NetCDF, gridded model output, hindcasts and projections — daily, for years |
| HPC | JSC Jülich training, HLRS course from September, Fortran→JAX/TPU port, Linux clusters |
| PyTorch | Forward hooks, ONNX→PyTorch conversion, batched inference on a 15-layer transformer |
| Physics-based models | You have *built* one, inside a community framework, and validated it |
| Attention mechanisms | Months of extracting and correcting them |
| Rigour about model output | Two silent errors found, one after publication, corrected publicly |

The rare combination is the first and third rows together. Most ML postdocs have
never run a transport model; most environmental modellers have never registered a
forward hook.

---

## 7. Reading order — about 8–10 hours

**Do this before writing the final letter (2–3 h)**
1. Garnelo et al. (2018), *Conditional Neural Processes* — the short one, read fully.
2. Kim et al. (2019), *Attentive Neural Processes* — read the introduction and the
   underfitting argument carefully; skim the rest.
3. Skim a CMAQ overview and one Hereon chemistry-transport-modelling paper from
   https://www.hereon.de/institutes/coastal_environmental_chemistry/chemistry_transport_modelling/publications/

**Before an interview (5–7 h)**
4. Kendall & Gal (2017), *What Uncertainties Do We Need in Bayesian Deep Learning?* —
   the aleatoric/epistemic distinction, stated cleanly.
5. Lakshminarayanan et al. (2017), *Deep Ensembles* — the baseline.
6. Gneiting & Raftery (2007) — CRPS and propriety; read the first sections.
7. Rasmussen & Williams, *Gaussian Processes for Machine Learning*, chapters 1–2 —
   free online; enough to see what NPs are replacing.
8. Gordon et al. (2020), *Convolutional Conditional Neural Processes* — skim, for the
   gridded-data connection.

**Practical, worth more than one more paper (3–4 h)**
9. Implement a CNP in PyTorch on 1-D synthetic data. There are compact reference
   implementations; write your own encoder/aggregator/decoder. Then sample a sparse
   "monitoring network" from a 2-D field and interpolate it. You will understand
   context/target splits in an afternoon, and you will be able to say you have
   implemented one — which is true and much better than saying you have read about it.

---

## 8. Questions to be ready for

- *Why a neural process rather than a Gaussian process?* → O(n) vs O(n³); learned
  rather than hand-specified covariance structure; amortised across tasks so a new
  city needs no refitting.
- *Why not just a CNN or a plain MLP on the grid?* → They do not take a variable-size
  context set, and they give no principled predictive distribution.
- *What is the difference between aleatoric and epistemic uncertainty here, and why
  do you care?* → §3. Answer with the sensor-placement consequence; that shows you
  understand why it matters operationally.
- *How would you evaluate whether the uncertainty is trustworthy?* → CRPS, calibration
  and reliability diagrams, sharpness subject to calibration, and
  **leave-one-station-out** rather than random CV.
- *How would you couple the CTM and the network?* → State the options (bias
  correction, emulation, fusion with covariates), say which you would try first and
  why, and say what you would need to see in the data first. Do not pretend to a
  settled answer — this is their research question, not a solved problem.
- *What is your deep learning experience?* → Be exact. Months, self-directed, PyTorch,
  activation extraction, no publications. Then the two bugs. Honesty plus a real
  demonstration of judgement beats a padded claim, and they will check.

---

## 9. What not to claim

- ❌ Bayesian deep learning experience. You have reading, and soon an implementation.
- ❌ Neural process experience — unless you do §7.9, in which case "I have implemented
  a conditional neural process on synthetic data" is exactly true and worth saying.
- ❌ Air quality modelling experience. You have *environmental* modelling; the
  transferable claim is gridded spatio-temporal simulation and validation, not
  atmospheric chemistry.
- ❌ Anything about CMAQ beyond having read their papers.

The letter already states the gap plainly. Keep that consistent in interview — a
candidate who marks the boundary of their knowledge precisely is more trustworthy
about everything inside it.
