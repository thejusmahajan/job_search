# Changelog and Session Log

Records chronological significant changes, refactoring decisions, and state updates for the job search repository, in accordance with Principle 11 and 21.

## [2026-03-10] Robert Bosch Hospital Setup
- **Documentation**: Added new entry to `APPLICATION_LOG.md`. Created `requirements.md` for the Robert Bosch Institute of Clinical Pharmacology role.
- **Artifacts**: Drafted `cover_letter_robert_bosch.tex` and updated `cv_robert_bosch.tex` emphasizing spatial transcriptomics, single-cell RNA sequencing, oncology (renal cell carcinoma), and multi-omics integration in R/Python. Compiled PDFs successfully.

## [2026-03-10] Helmholtz Munich Staff Scientist Setup
- **Documentation**: 
  - Added new entry to `APPLICATION_LOG.md` for Job ID 102868.
  - Created `requirements.md` in the new feature folder.
- **Artifacts**: 
  - Drafted `cover_letter_helmholtz_munich.tex` focusing on mentoring, reproducible workflows, and JAX/PyTorch.
  - Adapted `cv_helmholtz_munich.tex` and compiled both.

## [2026-03-10] Core Qualifications Extraction
- **Documentation**: Created `CORE_QUALIFICATIONS.md` to centralize reusable, standardized modules of high-impact experience (specifically the JAX/TPU/Fortran-to-Python deep learning porting experience) to ensure consistency across future PyTorch/TensorFlow deep learning applications.

## [2026-03-10] Universitätsklinikum Erlangen Setup
- **Web Research**: Discovered specific details about Dr. Pooja Gupta's project (BMFTR-funded, titled "AI-Driven Multi-Omics Integration for Predicting IBD-PD Comorbidity Progression").
- **Documentation**: 
  - Added new entry to `APPLICATION_LOG.md`.
  - Created `research_notes.md` in the new feature folder.
- **Artifacts**: 
  - Drafted `cover_letter_erlangen.tex` specifically highlighting the gut-brain axis, graph neural networks, and system-level modeling translation.
  - Adapted `cv_erlangen.tex` and compiled both.

## [2026-04-21] MPI-NAT Scientific IT Specialist / RSE Setup (Job Code 15-26)
- **Scaffold**: Created `applications/mpinat_scientific_it_specialist/` with baseline CV stem, cover letter stem, class file, signature, advertisement transcript, `requirements.md`, and `submission/` subfolder.
- **Requirements analysis**: Produced `requirements.md` mapping Muss/Kann-Anforderungen to candidate evidence; identified cloud + CI/CD as honest gaps; chose forward-looking framing for containerization depth.
- **CV (`cv_mpinat.tex`)**: Re-weighted for RSE/HPC fit — promoted Bioinformatics & Reproducible Research to top of Key Strengths, promoted JAX/TPU bullet in Uni Hamburg postdoc block, relabeled "Scientific IT & Data Engineering" subsection, set "Immediately available" and dropped all location restrictions from the Open-to line. 2 pages.
- **Cover letter (`cover_letter_mpinat.tex`)**: Addressed to Dr. Liepe with a tailored, highly autobiographical narrative style stripped of AI footprints (no em-dashes). Explicitly maps the 1,834-to-1,349 line DeGIR refactor, HPC scaling, and includes the wife's DESY postdoc status to solidly frame the dual-career relocation mandate to Göttingen. 2 pages.
- **Stem audit**: Discovered location constraint ("Hamburg, Berlin, or remote DACH") had silently contaminated `cv_clinical_data_science{,_de}.tex` baselines and the already-submitted Roche CV (Penzberg is in Bavaria — genuine oversight). Root cause traced to 2026-04-18 regression when clinical_data_science_general forked from cleaner reference/cv_baseline/. Patched both stems to drop location restriction and added "Research Software Engineering" to Open-to line.
- **Submission**: Merged cover letter + CV + Praktikumsbestätigung + Zeugnisse into `submission/Mahajan_Thejus_MPINAT_15-26.pdf` via pdfunite. 16 pages, submitted successfully via email.
- **Documentation**: Updated `APPLICATION_LOG.md` to status Submitted and added `reference/writing_style/PERSONAL_WRITING_STYLE.md` to properly log the user's authentic voice.

## [2026-04-20] Roche Diagnostics Penzberg Setup & Zeugnisse Rebuild
- **Artifacts**: Rebuilt `Mahajan_Thejus_Zeugnisse.pdf` bundle using chronological strict ordering (9 pages, compressed to ~2.3 MB). 
- **Documentation**: 
  - Updated `VERIFICATION_REPORT.md` with SHA-256 hashes and fulfillment checklist.
  - Updated `APPLICATION_LOG.md` recording the submission for Roche Biostatistician position.
