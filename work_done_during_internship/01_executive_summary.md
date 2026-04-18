# Comprehensive Work Report — Internship at HealthTwiSt GmbH

**Author:** Thejus Mahajan
**Position:** Bioinformatics Intern (MSc Bioinformatics)
**Organization:** HealthTwiSt GmbH, Berlin, Germany
**Supervisor:** Dr. Andreas Busjahn (CEO, HealthTwiSt GmbH)
**Period:** February 2 – April 15, 2026 (10.5 weeks, 40 hours/week)
**Arranged via:** CQ Beratung+Bildung GmbH (vocational training provider)
**Formal contract subject:** "Implementation of Machine Learning Workflows using the Tidymodels Framework in R"
**Actual scope:** Tidymodels introduction + production medical data pipeline refactoring + interactive Shiny dashboard
**Report generated:** 2026-04-18

---

## Purpose of This Document

This is a **complete, factual inventory** of all work performed, skills gained, tools used, and professional competencies demonstrated during the internship. It is designed for **job search agents** to extract relevant achievements and tailor CVs and cover letters to specific job requirements.

**Instructions for job search agents:**
- Every claim in this document has corresponding evidence (commits, files, emails, meeting notes).
- Map entries from this report to the target job's requirements. Do not invent skills not listed here.
- Use the keyword index (file 20) for rapid matching against job descriptions.
- The quantitative metrics section provides concrete numbers for CVs.
- The week-by-week timeline shows progression and growth for cover letter narratives.
- Prior background: Fortran, Python. **No prior R experience** — learned R/tidyverse from scratch during this internship. German B1, progressing to B2.

---

## Executive Summary

During a 10.5-week internship at HealthTwiSt GmbH in Berlin, I completed **three projects** spanning data engineering, software refactoring, R package development, interactive web application development, and machine learning pedagogy — all within the healthcare/clinical data domain under EU GDPR compliance.

### Project 1: DeGIR radioDB Pipeline Refactoring (Primary — 9 weeks)
Refactored a production data pipeline for the **DeGIR Quality Registry** (Deutsche Gesellschaft für Interventionelle Radiologie — German Society of Interventional Radiology). The pipeline processes **~143,000 interventional radiology patient records per year** from **~300 German clinics** into annual PDF quality reports for the DeGIR board. Implemented and verified **4 refactoring directives** independently:
- Externalized **257 hardcoded rules** into **8 CSV config files**
- Consolidated **21 copy-pasted code blocks** into **1 parameterized function**
- Replaced **360 deprecated function calls** across **4 files**
- Extracted **9 utility functions** into a standalone **R package (degirtools)**
- Reduced the main script from **1,834 to 1,349 lines (−26.5%)** with **byte-identical output** verified after every change
- Discovered and documented **2 pre-existing bugs** through systematic code review

### Project 2: DeGIR Dashboard (Supplementary — 1 week)
Built an **interactive bilingual (German/English) R Shiny web application** with **6 modules** for exploring interventional radiology clinical data. Deployed to **shinyapps.io** as a live portfolio piece. **1,468 lines of R code** across **10 files**.

### Project 3: Introduction to Tidymodels (Initial — 1 week)
Wrote a **Quarto teaching document** introducing the tidymodels machine learning framework in R, replacing the older caret-based material in HealthTwiSt's training curriculum. Published on GitHub. Dr. Busjahn: "ready for the next batch."
