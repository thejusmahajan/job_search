# AEON-UP Study Room: Start Here

> [!CAUTION]
> ### THE CORE CONCEPTUAL TRAP — READ THIS FIRST
> **"Neural processes" has NOTHING whatsoever to do with neural network interpretability, attention map inspection, linear probing, or mechanistic interpretability.**
>
> A **Neural Process (NP)** is a probabilistic deep learning framework that combines the mathematically rigorous uncertainty quantification of **Gaussian Processes (GPs)** with the computational scalability and representation learning of **deep neural networks**.
>
> In an interview with Dr. Martin Ramacher or Dr. Matthias Karl, any mention of "interpreting neural circuits" or conflating Neural Processes with transformer activation analysis will instantly signal a fundamental misunderstanding of the job. In this study room, Neural Processes are treated strictly as **stochastic process approximators for continuous spatio-temporal fields**.

---

## 1. Open Administrative Flag: Reference Number Discrepancy

> [!WARNING]
> **Open Item for Candidate Action:**
> Two distinct reference numbers are circulating for this vacancy:
> - **`1056`**: Listed in the primary Hereon posting URL (`.../1056-de_DE`).
> - **`030358`**: Cited in the internal research report documentation.
>
> **Action:** Check the live posting page before submitting the application to confirm which reference number the Hereon HR portal expects. Do not guess or silently select one.

---

## 2. Executive Positioning: The Spine of Your Preparation

The Helmholtz-Zentrum Hereon (Institute of Coastal Environmental Chemistry, Geesthacht) is seeking a Postdoctoral Researcher for **AEON-UP** (*Probabilistic Deep Learning for Urban Air Quality*).

### The Strategic Reality
- **Dr. Matthias Karl** is a world-class expert in physics-based Chemistry Transport Models (CTMs), specifically the author and maintainer of **EPISODE-CityChem**. His focus is aerosol dynamics, chemistry, dispersion, and exposure. He has no published machine learning track record.
- **Dr. Martin Ramacher** is an expert in regional/urban emission inventories (UrbEm, CMAQ) and exposure modeling. His primary turn toward ML was co-mentoring the 2024 ECMWF *Code for Earth* project ("Urban Air Quality View"), which explored downscaling regional atmospheric products to urban scale.
- **The Group's Need:** The PIs are physics and atmospheric chemistry modelers. They are **hiring a capability they do not yet possess in depth**.
- **Your Positioning:** You are not competing to out-publish theoretical ML professors. You are positioning yourself as the computational scientist who understands large-scale numerical grids, Linux HPC, NetCDF workflows, and PyTorch pipeline engineering who can **build and validate the learned half inside a physics-based research group**.

---

## 3. Study Room Architecture & Reading Sequence

Every document in this directory is self-contained, written in plain text (no unrendered LaTeX), with hand-checkable formulas and concrete worked examples.

```
study_room/
  |-- 00_START_HERE.md           [This file: 5 min]
  |-- 01_domain.md               [Domain guide: CTMs, EPISODE-CityChem, UFP: 25 min]
  |-- 02_methods.md              [Methods lineage: GP -> CNP -> NP -> ANP -> ConvCNP: 35 min]
  |-- 03_uncertainty.md          [Aleatoric/Epistemic, CRPS, Calibration, Spatial CV: 30 min]
  |-- 04_the_bridge.md           [Thejus' background mapped to AEON-UP: 20 min]
  |-- 05_interview_questions.md  [17 Q&As across 5 Bands + questions to ask them: 45 min]
  |-- 06_do_not_claim.md         [Strict boundaries and deflection scripts: 10 min]
  |-- 07_flashcards.md           [Spaced repetition Q&A bank: 20 min/session]
  |-- 08_study_plan.md           [Dated timeline to interview + HLRS alignment: 10 min]
  +-- STUDY_ROOM_REPORT.md       [Synthesis, bibliography, and verified claims report]
```

### Recommended Study Path & Time Budget

| Step | File | Focus | Time Budget |
|---|---|---|---|
| **Phase 1** | `06_do_not_claim.md`<br>`04_the_bridge.md` | Establish your defensive perimeter and articulate your grounded story. | **30 min** |
| **Phase 2** | `01_domain.md` | Master the atmospheric physics, EPISODE-CityChem, and Ultrafine Particles (UFP). | **25 min** |
| **Phase 3** | `02_methods.md`<br>`03_uncertainty.md` | Grasp the mathematical mechanics of ConvCNP, CRPS, calibration, and spatial validation. | **65 min** |
| **Phase 4** | `05_interview_questions.md` | Rehearse Bands A through E aloud using model answers grounded strictly in your CV. | **45 min** |
| **Phase 5** | `07_flashcards.md`<br>`08_study_plan.md` | Daily active recall and schedule tracking through the HLRS course window. | **20 min/day** |

**Total Initial Read Time:** ~3 hours.
