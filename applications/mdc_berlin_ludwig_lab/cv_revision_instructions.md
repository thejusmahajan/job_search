# CV Revision Instructions for MDC Berlin / Ludwig Lab Application

**Target file**: `cv_mdc.tex`
**Target position**: Computational Bioinformatician at the Ludwig Lab, MDC Berlin
**Lab focus**: Single-cell multi-omics (mtscATAC-seq, ASAP-seq, DOGMA-seq), stem cell biology, hematopoiesis, leukemia, mitochondrial genome biology
**Reference**: `requirements.md` in the same directory
**Class file**: `thejus_cv.cls` (do NOT modify; available macros: `\cvsection`, `\cvexperience`, `\cvskills`, `\cvstrength`, `\cvlanguage`, `\cvheader`)

### Applicant's actual bioinformatics experience (DO NOT overstate)
- **Nextflow pipeline (DSL2)**: Built a Hepatitis Delta Virus sequence analysis pipeline using MAFFT, trimAl, and NCBI Entrez Direct. GitHub: thinkcommonsense/hepatitis-delta-pipeline. This is a multiple sequence alignment pipeline on pre-assembled FASTA sequences, NOT an NGS read-processing pipeline.
- **CQ Beratung training**: Coursework in NGS analysis pipelines (Nextflow, Galaxy), sequence analysis, Biopython, SQL, biostatistics (R/Bioconductor).
- **No first-hand experience** with: scRNA-seq, scATAC-seq, Scanpy, Seurat, single-cell workflows, or multi-omics integration. Do NOT list these as skills.

---

## INSTRUCTION 1: Remove the "Strengths" section entirely

**File**: `cv_mdc.tex`, right column (after `\switchcolumn`)
**Action**: Delete the entire `\cvsection{Strengths}` block (lines 142-154), including all three `\cvstrength{...}{...}{...}` entries.
**Reason**: Redundant with Experience; unusual for academic/research CVs. The space is better used for Publications and Technical Skills.

---

## INSTRUCTION 2: Restructure the right column section order

After removing Strengths, reorder the right-column sections to:

1. `\cvsection{Technical Skills}` (revised per Instruction 4)
2. `\cvsection{Publications}` (moved up from bottom)
3. `\cvsection{Training / Courses}`
4. `\cvsection{Languages}`

---

## INSTRUCTION 3: Reorder left column sections and move Education up

Rearrange the left column to this order:

1. `\cvsection{Career Interests}` (revised per Instruction 5)
2. `\cvsection{Education}` — **move before Experience**
3. `\cvsection{Experience}` (revised per Instruction 6)
4. `\cvsection{References}` (keep at bottom of left column)

The `\newpage` command (currently line 69, before "Job search") should be repositioned as needed for clean page breaks after restructuring. Test the compiled output and adjust placement.

---

## INSTRUCTION 4: Rewrite the Technical Skills section

Replace the current six `\cvskills` entries with the following five. Use only the `\cvskills{Category}{Content}` macro.

```latex
\cvsection{Technical Skills}

\cvskills{Programming}
         {Python (Pandas, NumPy, Scikit-learn, Biopython), R (Bioconductor, Tidymodels, ggplot2), SQL, BASH}

\cvskills{Bioinformatics}
         {Nextflow (DSL2), NGS Analysis, Multiple Sequence Alignment (MAFFT), Sequence Trimming (trimAl), NCBI Databases / Entrez}

\cvskills{Biostatistics \& ML}
         {Multivariate Analysis, PCA, ANOVA, Dimensionality Reduction, Clustering, Scikit-learn, Tidymodels}

\cvskills{Data Engineering}
         {Large dataset processing (HDF5, NetCDF), Pipeline development, Data visualization}

\cvskills{Tools}
         {Linux/Unix, Git, HPC clusters, Conda}
```

**Key changes explained**:
- **Added** Biopython to Programming (covered in CQ training).
- **Added** specific real tools to Bioinformatics: MAFFT, trimAl, NCBI/Entrez (from the hepatitis-delta-pipeline project), Nextflow (DSL2) promoted to first position.
- **Removed** Fortran (irrelevant to this role).
- **Removed** Structural Bioinformatics (irrelevant to this lab).
- **Removed** Galaxy (too basic for this context; Nextflow is the stronger signal).
- **Removed** LaTeX from Tools (does not strengthen a genomics application).
- **Added** Conda to Tools (used for dependency management in the Nextflow pipeline).
- **Merged** AI/ML into Biostatistics & ML (cleaner; removed the Coursera reference from skills — it already appears under Training/Courses).
- **Added** Clustering to Biostatistics (relevant to single-cell analysis context and covered in training).
- **Renamed** "Data Analysis" to "Data Engineering" (better reflects pipeline work).
- **Kept** both HDF5 and NetCDF in Data Engineering (HDF5 is relevant to genomics formats like AnnData/h5ad; NetCDF demonstrates large-scale data handling).
- **Did NOT add** Scanpy, Seurat, scRNA-seq, scATAC-seq, or multi-omics integration — the applicant has no hands-on experience with these.

---

## INSTRUCTION 5: Revise the Career Interests text

Replace the current `\cvsection{Career Interests}` paragraph with:

```latex
\cvsection{Career Interests}
Computational Scientist (PhD) with 5+ years of experience in \textbf{large-scale data analysis}, \textbf{statistical modeling}, and \textbf{pipeline development}. Trained in \textbf{R (Bioconductor, Tidymodels)} and \textbf{Python (Pandas, NumPy, Scikit-learn)} for high-dimensional data analysis. Built a viral genomics pipeline using \textbf{Nextflow (DSL2)}. Currently deepening skills in \textbf{genomics}, AI/machine learning, and NGS analysis through specialized training and an industry internship. Eager to develop expertise in \textbf{single-cell multi-omics} and apply computational and data science skills to advance research in \textbf{stem cell biology and genomics}.
```

**Key changes**:
- Added mention of the **Nextflow pipeline** as concrete evidence of bioinformatics pipeline skills.
- Changed "clinical bioinformatics" to **"genomics"** (more relevant to this lab).
- Changed "Seeking to apply..." to **"Eager to develop expertise in single-cell multi-omics and apply..."** — this honestly signals strong interest and willingness to learn without claiming existing experience.
- Final phrase now ends with **"stem cell biology and genomics"** — directly relevant to the Ludwig Lab.

---

## INSTRUCTION 6: Clean up the Experience section

### 6a. Delete the "Job search" entry entirely
Remove lines 70-76 (the `\cvexperience{Job search}` block and the `\newpage` before it). This entry adds no value and signals a gap negatively.

### 6b. Condense "Physics Subject Matter Expert" and "Physics Trainer and Chess Coach"
Merge these two entries into a single entry:

```latex
\cvexperience{Physics Educator}
             {Tutorwaves Solutions Inc / Freelance}
             {10/2018 - 03/2021}
             {Kerala, India}
             {Prepared physics content for competitive examinations and coached state-level chess teams.}
```

This saves space (currently ~17 lines down to ~6) and moves non-relevant roles into the background.

---

## INSTRUCTION 7: Verify and compile

After all edits:
1. Compile with `pdflatex cv_mdc.tex` (run twice for proper layout).
2. Verify the PDF renders correctly with no overflow, missing text, or broken layout.
3. Ensure page breaks fall cleanly — no orphaned section headings at the bottom of page 1.
4. If the right column overflows or is too tight after adding Publications higher, consider reducing `\vspace` between language entries or trimming one language (Hindi is the least critical).

---

## Summary of section order after all changes

**Left column** (60%):
1. Career Interests
2. Education
3. Experience (Internship → CQ Training → Guest Scientist → Post-doc → Physics Educator → Ph.D. Researcher)
4. References

**Right column** (40%):
1. Technical Skills
2. Publications
3. Training / Courses
4. Languages
