# MPI-NAT 15-26 — Requirements & Fit Analysis

## 1. Position snapshot
The role at the Max Planck Institute for Multidisciplinary Sciences is a highly technical operational position focused on Scientific IT and Research Software Engineering. Rather than conducting biological research or pure biostatistics, the focus is on maintaining IT systems, supporting and optimizing reproducible data pipelines, and assisting scientists with HPC and coding practices.
- **Institute**: Max Planck Institute for Multidisciplinary Sciences (MPI-NAT)
- **Facility**: Facility for Data Sciences and Biostatistics
- **Group leader**: Dr. Juliane Liepe
- **Contact email**: ausschreibung15-26@mpinat.mpg.de
- **Deadline**: 8 May 2026
- **Contract length**: Two years (initially limited, permanent possible)
- **Pay scale**: TVöD Bund

## 2. Muss-Anforderungen (hard requirements)
| Requirement | Evidence in candidate profile | Strength |
| :--- | :--- | :--- |
| Degree (MSc/PhD) in CS, bioinformatics, data science, or a related technical field | Ph.D. in Astrochemistry, M.Sc. in Physics, Bioinformatics/Biostatistics Weiterbildung. | Strong |
| Strong programming skills (Python/R/Bash) and Linux | R (pipeline refactoring, degirtools), Python (JAX/TPU port, Pandas), BASH scripting, Linux HPC experience. | Strong |
| Experience with workflows, version control (Git), and scientific computing | Nextflow (DSL2) pipelines, Git/GitHub, scientific modeling in Fortran/JAX. | Strong |
| Problem-solving mindset and good communication skills | Extracted 257 rules to CSVs, created teaching materials, tutoring experience. | Strong |
| Fluent in English | Fluent (C1), multiple English-language physics publications. | Strong |

## 3. Kann-Anforderungen (desired skills)
| Requirement | Evidence in candidate profile | Strength |
| :--- | :--- | :--- |
| HPC | JSC Jülich training, Google JAX/TPU/GPU parallelization for Fortran port. | Strong |
| Containers (Docker/Singularity) | "Docker concepts" listed on CV. | Partial |
| Workflow tools (Snakemake/Nextflow) | Developed reproducible Hepatitis Delta Virus Nextflow (DSL2) pipeline. | Strong |
| Cloud | Not explicitly present on the baseline CV. | Gap |
| CI/CD | Not explicitly present on the baseline CV. | Gap |
| Database systems and data storage solutions | SQL (bioinformatics databases), NetCDF/HDF5 pipeline processing. | Partial |

## 4. Key tasks → candidate assets
- **Maintain IT systems and research computing environments**: Hands-on experience working in Linux HPC environments to process large NetCDF datasets and scale models alongside foundational IT knowledge from BASH/Linux training.
- **Support and optimise data analysis workflows and pipelines**: Refactored the DeGIR monolithic R pipeline (1,834 lines) achieving a 26.5% code reduction with byte-identical output verified via `identical()`.
- **Install/configure scientific software**: Managed complex dependencies using Conda for the Hepatitis Delta Virus Nextflow pipeline.
- **Assist researchers with code, HPC usage, and reproducible practices**: Engineered a legacy Fortran model into a high-performance Python engine using Google JAX for TPU/GPU execution, setting up parallelized models for other scientists.
- **Provide on-site training and contribute to best practices in research software**: Authored Tidymodels teaching materials (Quarto/GitHub) that successfully replaced a legacy analytical framework, combined with years of direct tutoring experience.

## 5. Unique Selling Proposition (USP)
Thejus brings a rare intersection of heavy HPC computation (JAX/TPU, NetCDF) and rigorous production software engineering discipline (`identical()` pipeline refactoring, config-driven logic, `devtools::check()`). Unlike many academic applicants who prioritize novel research over maintainable code, his recent clinical data work proves an intrinsic dedication to reliability, testing, and documentation. His proven track record in developing teaching materials and coaching further establishes him as an ideal multiplier for research software best practices within the Facility.

## 6. Gap analysis
- **Cloud Infrastructure**: No major cloud vendors (AWS, GCP, Azure) are listed natively on the CV. *Strategy*: (b) Honest omission.
- **CI/CD Pipelines**: No explicit mention of tools like GitHub Actions or Jenkins. *Strategy*: (a) Foreground adjacent evidence highlighting readiness to adopt CI/CD, such as package building with `devtools::check()`, rigorous version control using Git, and strict test-driven verify-before-you-touch paradigms (`identical()`).
- **Containerization Depth**: The CV lists "Docker concepts" rather than complex production Swarm/K8s deployments. *Strategy*: (c) Forward-looking framing in the cover letter — articulate a keen interest in expanding the usage of Docker/Singularity to deliver universally reproducible research environments to MPI scientists.

## 7. CV re-weighting plan
- Remove the narrative "Profile" block entirely to comply with German tabular CV standards, relocating the availability and location preferences cleanly to the cover letter.
- Promote the "Bioinformatics & Reproducible Research" strength (highlighting Nextflow) to the absolute top of the Key Strengths sidebar, as this represents core RSE workflow requirements.
- Under the Uni Hamburg Post-doc section, emphasize the JAX/TPU porting, branchless logic, and Linux HPC usage over the marine-ecosystem modeling domain details.
- Expand the Tidymodels point in the HealthTwiSt job description to explicitly highlight "experience providing training to researchers on modern code practices."
- Reposition "High Performance Computing (HPC) Training (JSC)" to the top of the "Courses & Training" block to guarantee its immediate visibility for the desired HPC skills.
- Relabel the "Data Engineering" tech skills subsection to "Scientific IT & Data Engineering" to mirror the title of the position.

## 8. Cover letter skeleton (outline only)
1. **Hook**: Connect the rigor of refactoring the 143k-record DeGIR pipeline and scaling computational models via JAX/TPU directly to MPI-NAT's need for a robust, reproducible research IT environment.
2. **Fit**: Detail explicitly how the development of the `degirtools` R package, the DSL2 Nextflow pipeline, and daily Linux/BASH workflows map 1:1 to the Facility's required tech stack.
3. **Motivation**: Express enthusiasm for the Max Planck Society's interdisciplinary, data-driven life science mission and the specific opportunity to accelerate scientific discovery by supporting and training researchers.
4. **Close**: Confidently request an interview, confirming availability to start from mid-April 2026 and willingness to relocate to Göttingen.

## 9. Open questions for the human operator
- The CV currently lists "Docker concepts". Shall we retain this phrasing to be strictly honest, or have you gained enough practical experience recently to list "Docker (Containerization)" without the "concepts" caveat?
- Did your work on `degirtools` use GitHub Actions for automated `R CMD check`? If yes, we can legitimately add "GitHub Actions (CI/CD)" to your tech skills to fulfill that desired requirement.
- The job advert is in English but the location is German. The application language request says English, but should the formal cover letter headers and dates adhere strictly to DIN 5008 German postal norms, or a more international English letter format?
