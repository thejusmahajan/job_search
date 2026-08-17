# 08. Dated Study and Preparation Plan: August 17 to Interview Window

> **Application Deadline:** 3 September 2026  
> **Anticipated Interview Window:** 14 September – 30 September 2026  
> **Position Start Date:** 1 October 2026  
> **HLRS Supercomputing Course:** 6 September – 7 October 2026 (80% Online)

---

## 1. Timeline Overview and Synchronized Milestones

```
+-----------------------------------------------------------------------------------------+
| Phase 1: Application Submission & Grounding     (17 Aug – 3 Sep 2026)                   |
| - Verify Reference number (1056 vs 030358) and submit application                      |
| - Daily Flashcard drill + Deep dive into Domain (01) and Methods (02)                   |
+-----------------------------------------------------------------------------------------+
| Phase 2: HLRS Course Kickoff & Core Methods     (4 Sep – 13 Sep 2026)                   |
| - HLRS Supercomputing-Akademie begins (6 Sep)                                           |
| - Code walkthrough of 1D/2D ConvCNP implementation in PyTorch                           |
| - Rehearse Band A and Band B interview questions aloud                                  |
+-----------------------------------------------------------------------------------------+
| Phase 3: Applied Scenarios & Mock Interviews    (14 Sep – 23 Sep 2026)                  |
| - Rehearse Band C, Band D, and Band E questions with voice recordings                   |
| - Deep dive into EPISODE-CityChem NetCDF structure and UFP microphysics                 |
+-----------------------------------------------------------------------------------------+
| Phase 4: Final Polish & Interview Readiness     (24 Sep – 30 Sep 2026)                  |
| - Review Strategic Questions to ask PIs (Dr. Ramacher & Dr. Karl)                       |
| - Rapid-fire Flashcard mastery (100% recall on 07_flashcards.md)                        |
+-----------------------------------------------------------------------------------------+
```

---

## 2. Weekly Dated Schedule

### Week 1: August 17 – August 23, 2026 (Foundations & Grounding)
- **Goal:** Lock down the defensive boundaries and master the core domain mechanics.
- **Mon 17 Aug:** Read `00_START_HERE.md` and `06_do_not_claim.md`. Memorize the five forbidden claims.
- **Tue 18 Aug:** Read `01_domain.md`. Understand CTM operator splitting and EPISODE-CityChem's sub-grid Gaussian modules.
- **Wed 19 Aug:** Study Ultrafine Particles (UFP) section in `01_domain.md`. Learn why PNC (particles/cm3) is used instead of mass, and why UFP lacks binding EU mass limit values.
- **Thu 20 Aug:** Read `04_the_bridge.md`. Practice delivering the 60-second elevator pitch aloud three times.
- **Fri 21 Aug:** Begin daily flashcard sessions with `07_flashcards.md` (20 minutes).
- **Sat 22 Aug – Sun 23 Aug:** Review Karl et al. (2019) GMD paper on EPISODE-CityChem.

### Week 2: August 24 – August 30, 2026 (Algorithmic Lineage & Math)
- **Goal:** Master the step-by-step mechanics from GP to ConvCNP.
- **Mon 24 Aug:** Read `02_methods.md` (GP cubic bottleneck, CNP encoder-aggregator-decoder forward pass).
- **Tue 25 Aug:** Study ANP cross-attention and why mean aggregation causes underfitting near sensor spikes.
- **Wed 26 Aug:** Deep dive into ConvCNP: translation equivariance, continuous discretization, and density channel `d_0`.
- **Thu 27 Aug:** Read Vaughan et al. (2021) arXiv:2101.07950 (*ConvCNP for local climate downscaling*).
- **Fri 28 Aug:** Read `03_uncertainty.md`. Master aleatoric vs epistemic operational definitions and CRPS formula.
- **Sat 29 Aug – Sun 30 Aug:** Review the Spatial Leakage Trap in `03_uncertainty.md` and why Leave-One-Station-Out (LOSO) is required.

### Week 3: August 31 – September 6, 2026 (Application Submission & HLRS Launch)
- **Goal:** Confirm reference number, submit application, and start HLRS HPC training.
- **Mon 31 Aug:** Double-check live Hereon posting URL for Reference Number (`1056` vs `030358`). Finalize application package.
- **Tue 1 Sep:** Rehearse Band A and Band B questions in `05_interview_questions.md`.
- **Wed 2 Sep:** Final review of submission package.
- **Thu 3 Sep (DEADLINE):** **Submit Application to Hereon HR Portal.**
- **Fri 4 Sep:** Self-test on `07_flashcards.md`.
- **Sat 5 Sep:** Rest and mental reset before intensive course phase.
- **Sun 6 Sep:** **HLRS Course Begins** (*Deployable Data Analysis & AI Pipelines with HPC*, 80% online).

### Week 4: September 7 – September 13, 2026 (Applied Design & HLRS Parallelism)
- **Goal:** Connect HLRS distributed computing principles directly to PyTorch ConvCNP scaling.
- **Mon 7 Sep – Wed 9 Sep:** HLRS coursework (AI pipeline deployment on HPC clusters). Connect GPU memory optimization to ConvCNP multi-scale feature maps.
- **Thu 10 Sep:** Rehearse Band C (Applied & Design) questions in `05_interview_questions.md` aloud.
- **Fri 11 Sep:** Rehearse the 3-station city scenario (Question 11) and the NO2 vs PM2.5 multi-scale question (Question 12).
- **Sat 12 Sep – Sun 13 Sep:** Mock oral rehearsal: record yourself answering Questions 1 through 12. Listen back and eliminate hesitation.

### Week 5: September 14 – September 20, 2026 (The Hard Questions & Behavioural Polish)
- **Goal:** Master Band D and Band E without flinching.
- **Mon 14 Sep:** Study Band D in `05_interview_questions.md`. Rehearse the two silent pipeline errors story and HealthTwiSt bug escalation.
- **Tue 15 Sep:** Rehearse Band E (Question 15: *"No ML publications"*). Practice delivering the answer with calm authority.
- **Wed 16 Sep:** Rehearse Question 16 (*"German B1"*), Question 17 (*"Astro/Marine -> Atmospheric"*), and Question 18 (*"What do you not know"*).
- **Thu 17 Sep:** Rehearse the 4 Strategic Questions to ask the PIs (Section 4 of `05_interview_questions.md`).
- **Fri 18 Sep – Sun 20 Sep:** Continue HLRS course modules; daily 15-minute flashcard drill.

### Week 6: September 21 – September 30, 2026 (Interview Window & Final Drill)
- **Goal:** Peak interview readiness, crisp delivery, zero cognitive lag.
- **Mon 21 Sep – Wed 23 Sep:** Full mock interview simulation: 45 minutes answering randomized questions from `05_interview_questions.md`.
- **Thu 24 Sep – Fri 25 Sep:** Review Hereon institutional notes (Geesthacht campus, Dr. Ramacher's ECMWF Code for Earth 2024 project, Dr. Karl's EPISODE-CityChem releases).
- **Sat 26 Sep – Mon 28 Sep:** Daily rapid-fire flashcards with `07_flashcards.md`.
- **Day Before Interview:** Review `00_START_HERE.md`, `04_the_bridge.md`, and `06_do_not_claim.md`. Rest well.
