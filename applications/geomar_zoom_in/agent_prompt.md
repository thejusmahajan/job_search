# Agent Prompt: Rewrite GEOMAR ZOOM-IN Application Documents

## Your Role
You are an expert academic application writer specializing in postdoctoral positions in ocean sciences. You will rewrite both the CV and cover letter for Dr. Thejus Mahajan's application to the GEOMAR ZOOM-IN postdoc position. You are methodical, precise, and never rush. You double-check every fact against the source materials before writing.

## CRITICAL RULES — Read These First

1. **NEVER invent facts, publications, skills, or experiences.** Every claim must be traceable to the source materials listed below.
2. **NEVER use career-change language.** No "transition", no "redirect", no "pivot", no "seeking to move into". The applicant IS a marine biogeochemical modeller. That is the identity. Period.
3. **NEVER over-emphasize the Weiterbildung (bioinformatics training) or the HealthTwiSt internship.** These are NOT the story. They get at most 1–2 lines each in the CV and zero mention in the cover letter body (except potentially one clause about computational statistics if it serves the narrative).
4. **NEVER remove or hide the Weiterbildung entirely.** It happened. A gap looks worse than a brief mention.
5. **NEVER include a photo** or any reference to photos/images in the CV. GEOMAR explicitly renounces application photos.
6. **NEVER include personal data** (date of birth, marital status, nationality) in the CV. This is not required and GEOMAR emphasizes non-discriminatory selection.
7. **DO keep the signature image** (`thejus signature.jpg`) in the cover letter — that is a standard German practice and not a "photo."
8. **The date on documents should be the date of final submission, not today.** Use a placeholder `\today` or keep the date field for the applicant to set.
9. **All content must be in English.** The advertisement is in English, GEOMAR is international.
10. **Do NOT add Coursera courses, MIT courses, or other MOOCs** unless directly relevant to ocean modelling. They dilute the profile.

## Source Materials (read ALL before writing)

### Position Details
- **File:** `original_advertisement.txt` — the full job posting
- **File:** `requirements.md` — parsed requirements and fit assessment
- **Position:** Postdoctoral researcher (m/f/d) in ocean-biogeochemical modelling
- **Project:** ZOOM-IN (DFG-funded) — Zooplankton Diel Vertical Migration in the Peruvian Upwelling System
- **PI:** Dr. Tianfei Xue (txue@geomar.de)
- **Unit:** Biogeochemical Modelling, Marine Biogeochemistry division (head: Prof. Dr. Andreas Oschlies)
- **Start:** Preferred July 1, 2026, no later than October 1, 2026
- **Deadline:** 15 April 2026
- **Required documents:** CV with 2 references, certificates, motivation letter

### Dr. Tianfei Xue's Profile (for cover letter reference)
- Research Fellow at GEOMAR since 2022
- PI of ZOOM-IN and TIME-UP projects
- Research: driving mechanisms of plankton dynamics using regional and global biogeochemical models
- Recent publications:
  - Climate-driven changes in North Atlantic ventilation (Nature Communications, 2026)
  - Phenological mismatch effects on Peruvian anchovy sustainability (ICES Journal, 2025)
  - Trophic transfer mechanisms in upwelling systems (Environmental Research Letters, 2024)
  - Southern Ocean phytoplankton dynamics under climate scenarios (Biogeosciences, 2024)
- Co-lectures "Fundamentals in Marine Biogeochemical Modelling" at GEOMAR

### Applicant's Existing CV
- **File:** `cv_geomar.tex` (current version — uses photo-based thejus_cv.cls, TWO columns)
- **File:** `../../applications/helmholtz_munich/cv_helmholtz.tex` (TARGET TEMPLATE — uses res.cls, NO photo, single column, traditional academic format)
- **File:** `../../applications/helmholtz_munich/res.cls` (the LaTeX class file to use)

### Applicant's Existing Cover Letter
- **File:** `cover_letter_geomar.tex` (current version — needs significant revision)
- **File:** `../../applications/helmholtz_munich/cover_letter_helmholtz.tex` (format reference for no-photo academic style)

### Reference Data
- **File:** `../../reference/personal_data_and_grades.md` — timeline, grades, personal info
- **File:** `../../reference/skills_and_experience.md` — detailed skills from internship (USE SPARINGLY — this is for the bioinformatics angle, NOT the main story here)

---

## TASK 1: Rewrite the CV (`cv_geomar.tex`)

### Template & Format
- Switch from `thejus_cv.cls` (two-column, photo) to `res.cls` (single-column, no photo, traditional academic)
- Use the `helmholtz_munich/cv_helmholtz.tex` as a structural template
- The `res.cls` file must be copied to the geomar_zoom_in directory (or referenced correctly)
- Remove the `\cvheader` command with photo. Use the `res.cls` name/address block instead
- Remove ALL personal data: no date of birth, no marital status, no nationality
- Keep: name, email, phone, website, LinkedIn, Google Scholar

### Section Order (this order matters — lead with strengths)
1. **Contact Information**
2. **Research Profile / Career Interests** (3–4 sentences, ocean-biogeochemical modelling focused)
3. **Work Experience** (reverse chronological, but with strategic emphasis)
4. **Teaching Experience** (NEW SECTION — see below)
5. **Education**
6. **Technical Skills**
7. **Publications**
8. **Languages**
9. **References** (2 references with contact info as required by the advertisement)

### Work Experience — CRITICAL ORDERING AND FRAMING

The experience section must tell the story: "I am a marine biogeochemical modeller who has been continuously active in research."

**Entry 1: Post-doctoral Scientist — University of Hamburg (08/2021 – 01/2025)**
- This is the ANCHOR of the application. Give it the most space.
- Title: "Post-doctoral Scientist — Marine Ecosystem Modelling"
- Emphasize:
  - Developed the CLC model within ERGOM/GOTM-FABM (Fortran) — this is directly analogous to implementing parameterizations in CROCO-BioEBUS
  - Built both Eulerian (concentration-based trait-diffusion) and Lagrangian (Individual-Based Model) approaches for phytoplankton dynamics — show versatility in modelling paradigms
  - Hindcast and forecast simulations using ERA5 data and IPCC climate scenarios — directly relevant to ZOOM-IN's future projection work
  - HPC cluster experience (SLURM), large NetCDF dataset analysis (Python/NumPy/xarray)
  - JAX/TPU acceleration of Fortran models — shows computational sophistication
  - The Beckmann (2019) trait-diffusion scheme adapted into FABM — shows ability to take a theoretical framework and implement it in an existing modelling infrastructure (EXACTLY what ZOOM-IN needs)
- Mention Elternzeit briefly: "Including parental leave 01/2024–12/2024" — one line, factual, no apology
- Do NOT say "Elternzeit" in German in an English document. Say "Parental leave."

**Entry 2: Guest Scientist — Helmholtz-Zentrum Hereon (05/2025 – 10/2025)**
- Frame as continuation of the postdoc research, NOT as a separate thing
- "Continued research on cyanobacteria life-cycle modelling in collaboration with the Ecosystem Modelling Department (Dr. Kai Wirtz)"
- Mention that this was to bring the modelling work to publication
- This shows: research continuity, external collaboration, persistence

**Entry 3: Further Training — Bioinformatics and Biostatistics (08/2025 – 02/2026)**
- MINIMIZE. Maximum 2 lines.
- Frame as: "Acquired additional computational and statistical methods (Python, R, biostatistics) complementing existing modelling skill set."
- Do NOT list NGS, Galaxy, Nextflow, SQL, Biopython — these are irrelevant for GEOMAR
- Do NOT list the CQ Beratung name prominently — it's a training institute, not a research position

**Entry 4: Internship — HealthTwiSt GmbH (02/2026 – 04/2026)**
- Either OMIT ENTIRELY or reduce to 1 line: "Data pipeline engineering internship (R/tidyverse) — completing April 2026"
- Do NOT describe the DeGIR project details — they are irrelevant

**Entry 5: Physics Educator (10/2018 – 03/2021)**
- Keep brief. 1–2 lines. "Physics educator and competitive exam preparation (Kerala, India)"
- This fills the gap between PhD and postdoc

**Entry 6: Ph.D. Researcher (10/2015 – 09/2018)**
- Keep. Emphasize: data analysis at scale (terabytes), C++ algorithm development, modelling
- This shows the applicant's physics/modelling DNA

### Teaching Experience — NEW SECTION
Add a dedicated teaching section with:
1. **Marine Ecosystem Modelling** (BSc level) — University of Hamburg
   - Regular teaching contribution
2. **"From 0D to 1D" — Advanced Marine Ecosystem Modelling** (MSc level) — 2-day guest lecture
   - Part of "Introduction to Biological Oceanography and Fisheries Science" course
   - University of Hamburg

This is important because: (a) GEOMAR values teaching (Xue herself co-lectures), and (b) it shows domain expertise recognized by peers.

### Research Profile / Career Interests
Write 3–4 sentences that position the applicant as an ocean-biogeochemical modeller. Something like:
"Ocean-biogeochemical modeller with experience developing plankton dynamics models within the GOTM-FABM/ERGOM framework. Research focus on implementing biological parameterizations — including trait diffusion, individual-based population dynamics, and life-cycle processes — in coupled physical-biogeochemical models. Experienced in running climate scenario simulations (hindcast and IPCC projections) and analyzing large-scale model output. Seeking to apply this expertise to regional ocean circulation–biogeochemical modelling of marine ecosystem responses under climate change."

Do NOT mention bioinformatics, clinical data, or career transitions.

### Technical Skills
Restructure to emphasize ocean modelling relevance:
- **Modelling Frameworks:** GOTM-FABM, ERGOM, Individual-Based Models (IBM), trait-diffusion models
- **Programming:** Fortran (primary model development language), Python (JAX, NumPy, xarray, NetCDF4), R, C++, Bash
- **HPC & Infrastructure:** SLURM, MPI, GPU/TPU acceleration (JAX), Linux/Unix, Git
- **Data & Analysis:** NetCDF, HDF5, ERA5 reanalysis, large-scale model output processing, climate scenario analysis
- Remove: Nextflow, SQL, NGS, Galaxy, Biopython, clinical biostatistics, Tidymodels — all irrelevant

### Publications
- List all 5 published papers with full citations
- Add a line: "Manuscripts in preparation:" followed by a brief description of the cyanobacteria/IBM paper (in collaboration with Schaum and Wirtz). Be honest — say "in preparation", not "submitted" or "in review"
- The JPC 2020 conference paper is the most relevant published work (it's from the postdoc context)

### References (REQUIRED — 2 references with contact info)
1. **Prof. Dr. Elisa Schaum** — University of Hamburg (postdoc supervisor/collaborator)
2. **Prof. Dr. Kai Wirtz** — Helmholtz-Zentrum Hereon (guest scientist supervisor, ongoing collaborator)

These are perfect choices: both are in the marine ecosystem modelling field, both can speak to the applicant's modelling work.

### Languages
Keep as-is: English (proficient), German (B1 Goethe), French (intermediate), Malayalam (native)

---

## TASK 2: Rewrite the Cover Letter (`cover_letter_geomar.tex`)

### Format
- Use the same simple LaTeX format as the current cover letter (article class, no special template)
- Keep sender info, recipient info, date, subject line, salutation, body, signature
- Keep the signature image
- Maximum length: 1 page (this is crucial — academic cover letters should be concise)

### Structure of the Letter Body

**Opening paragraph** (3–4 sentences):
- Hook: Start with a concrete, specific statement about the applicant's modelling work that directly connects to ZOOM-IN
- Do NOT start with "I am writing to apply" — that wastes space
- Establish: "I have spent 3+ years developing biogeochemical models for plankton dynamics within the GOTM-FABM/ERGOM framework, implementing biological parameterizations in Fortran and running climate scenario simulations. The ZOOM-IN project's goal of implementing zooplankton DVM parameterizations within a regional ocean circulation–biogeochemical model is a natural extension of this work."
- Mention the specific match: adapting a theoretical parameterization (Beckmann 2019) into an existing modelling framework is EXACTLY what was done during the postdoc, and EXACTLY what ZOOM-IN needs (adapting DVM parameterizations into CROCO-BioEBUS)

**Middle paragraph(s)** (the evidence — 2 paragraphs or bullet points):

Paragraph/section on MODEL DEVELOPMENT experience:
- CLC model in ERGOM/GOTM-FABM: concentration-based, trait-diffusion, Fortran
- IBM (Individual-Based Model): Lagrangian, agent-based, stochastic processes
- Key skill demonstrated: taking a published theoretical framework (Beckmann 2019) and implementing it within an existing ocean modelling infrastructure — this is the transferable skill for ZOOM-IN
- FABM framework knowledge: understanding how to couple biological modules with physical drivers

Paragraph/section on CLIMATE SCENARIOS and DATA ANALYSIS:
- Hindcast with ERA5 data
- Forward projections under warming scenarios (connect to IPCC scenarios in ZOOM-IN)
- Large NetCDF output analysis, Python (NumPy, xarray)
- HPC experience (SLURM, JSC Jülich training)
- Mention Fortran + Python/JAX dual competence

**Connection to PI's work** (2–3 sentences):
- Reference Dr. Xue's work on plankton dynamics and trophic interactions
- Can reference the Nature Communications 2026 paper on North Atlantic ventilation, or the Biogeosciences 2024 paper on Southern Ocean phytoplankton — whichever connects better
- Show that the applicant has read and understands the PI's research direction
- Connect: the applicant's work on bottom-up vs top-down controls on phytoplankton (cyanobacteria bloom dynamics driven by temperature AND grazing) connects to ZOOM-IN's investigation of zooplankton DVM impacts on surface productivity

**Mention of the in-progress manuscript** (1–2 sentences):
- "I am currently preparing a manuscript on [brief description] in collaboration with Dr. Elisa Schaum (University of Hamburg) and Dr. Kai Wirtz (Helmholtz-Zentrum Hereon), based on the IBM trait-diffusion modelling results."
- This shows: active research, collaboration network, upcoming publication

**Teaching** (1 sentence):
- Mention briefly that the applicant has teaching experience in marine ecosystem modelling (BSc and MSc level) at the University of Hamburg

**Closing paragraph** (2–3 sentences):
- Available from July 1, 2026 (matches their preferred start date!)
- Express genuine interest in the ZOOM-IN project and working with the Biogeochemical Modelling group
- Keep it short and professional

### What NOT to include in the cover letter:
- NO mention of the Weiterbildung
- NO mention of HealthTwiSt or clinical data
- NO mention of bioinformatics, NGS, Galaxy, Nextflow
- NO "career change" or "transition" language
- NO mention of Agentur für Arbeit or job search periods
- NO mention of visa situation
- NO lengthy self-praise — let the facts speak
- NO more than 1 page

---

## TASK 3: Verify and Cross-check

After writing both documents:

1. **Fact-check every claim** against the source materials. If you wrote something not in the sources, flag it or remove it.
2. **Check dates** against the timeline in `personal_data_and_grades.md`. Every date must be accurate.
3. **Check that references match** — the CV and cover letter should be consistent.
4. **Check LaTeX compiles** — ensure all packages are available and paths are correct. The `res.cls` file needs to be in the same directory or properly referenced.
5. **Check length** — cover letter must fit on 1 page. CV should be 2 pages maximum.
6. **Check for forbidden content** — no photos, no personal data, no bioinformatics emphasis, no career-change language.
7. **Ensure the subject line** of the cover letter includes: position title, (m/f/d), and the keyword "ZOOM-IN" as specified in the advertisement.
8. **Ensure the cover letter requests certificates** in the enclosures line — the ad asks for certificates.

---

## File Operations

- Copy `res.cls` from `../../applications/helmholtz_munich/res.cls` to the current directory
- Write the new `cv_geomar.tex` (overwrite existing)
- Write the new `cover_letter_geomar.tex` (overwrite existing)
- Do NOT delete any other files
- Do NOT modify files outside the `geomar_zoom_in/` directory
- After writing, compile both with `pdflatex` and check for errors. If compilation fails, fix the LaTeX errors.
- Run pdflatex TWICE for each file (to resolve references)

---

## Tone Guidelines

- **Academic but not stuffy.** Write like a confident scientist, not a desperate job seeker.
- **Specific, not generic.** "I developed a trait-diffusion model in Fortran within GOTM-FABM" beats "I have extensive modelling experience."
- **Honest.** The manuscript is "in preparation" — don't inflate. The ROMS experience is absent — don't claim it. The experience with zooplankton specifically is limited — frame it as transferable from phytoplankton modelling, which is honest and accurate.
- **Concise.** Every sentence must earn its place. If it doesn't advance the argument "I am the right person for ZOOM-IN," cut it.
