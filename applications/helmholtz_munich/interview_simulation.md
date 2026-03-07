# Interview Simulation: IDM Tübingen

## Part 1: Internal Discussion Before Interview

**Setting:** Conference room at IDM Tübingen. Prof. Preissl (contact for position), Prof. Birkenfeld (Prevention Dept Head), and Dr. Martin Heni (Senior Researcher, metabolism) reviewing applications.

---

**Prof. Preissl:** Let's discuss Dr. Thejus Mahajan's application. Unusual background—PhD in astrochemistry, then marine ecosystem modeling, now transitioning to bioinformatics.

**Prof. Birkenfeld:** I noticed that too. What's the connection to our clinical work?

**Prof. Preissl:** Look at the recent training—CQ Beratung in Berlin. Biostatistics, R/Bioconductor, NGS analysis. And there's an internship at HealthTwiSt starting next month on machine learning with Tidymodels.

**Dr. Heni:** The modeling background could be valuable. We have complex multi-organ data—brain, liver, pancreas. Someone who thinks in systems terms...

**Prof. Birkenfeld:** But he's never worked with patient data. Environmental datasets are different.

**Prof. Preissl:** True, but the training mentions "real and simulated patient datasets." And the supervisor—Dr. Andreas Busjahn from HealthTwiSt—is his first reference. That's a health tech company in Berlin.

**Dr. Heni:** The Python and R skills look solid. Pandas, NumPy, Bioconductor. And he knows Fortran—that's actually useful for some of our older analysis code.

**Prof. Birkenfeld:** What about the PhD-to-BSc-level concern? He's overqualified on paper.

**Prof. Preissl:** His cover letter addresses it directly. He calls it a "deliberate career transition." Says he wants to apply computational skills to human health research. It's honest.

**Dr. Heni:** Five publications. Experience with terabytes of data. If he can adapt to clinical contexts, the analytical foundation is there.

**Prof. Birkenfeld:** Let's interview him. I want to understand: Can he handle our actual data challenges? Does he understand prediabetes research? And is this commitment genuine?

---

## Part 2: Mock Interview Questions

### Opening / Background

**Prof. Preissl:** "Dr. Mahajan, thank you for coming. Your application is interesting, but I must admit—astrochemistry to diabetes research is quite a journey. Can you walk us through your thinking?"

> **Your Answer Points:**
> - Started in physics/astrochemistry—developed strong computational and data analysis skills
> - PostDoc in marine modeling: learned to work with complex biological systems, ecological time-series data
> - Realized my passion is applying these skills to research that directly impacts human health
> - Made a deliberate choice to retrain through CQ bioinformatics program
> - The HealthTwiSt internship connects directly to clinical ML applications
> - This isn't stepping down—it's redirecting my expertise toward meaningful work

---

### Technical Skills

**Dr. Heni:** "We work primarily with R and Python. Can you give me a specific example of statistical analysis you've done in R?"

> **Your Answer Points:**
> - PostDoc: Used R for ecological time-series analysis, ggplot2 for visualization
> - CQ Training: Learned Bioconductor for biological data, applied ANOVA, PCA, hierarchical clustering
> - Worked with patient datasets (real and simulated) during biostatistics training
> - Currently learning Tidymodels framework for ML—will apply this in HealthTwiSt internship
> - Comfortable with multivariate analysis, dimensionality reduction—directly applicable to sub-phenotype characterization

**Prof. Birkenfeld:** "What about handling large clinical datasets? We have data from thousands of patients with multiple measurements per visit."

> **Your Answer Points:**
> - PhD: Processed terabytes of collision experiment data
> - PostDoc: Analyzed multi-dimensional NetCDF environmental datasets
> - Experience with data pipelines, cleaning, transformation
> - Understand the importance of data quality, missing value handling
> - Know SQL for database queries (learned at CQ)
> - Ready to learn clinical data formats (CDISC, HL7 if needed)

---

### Research Understanding

**Prof. Preissl:** "What do you know about our work on prediabetes sub-phenotypes?"

> **Your Answer Points:**
> - Read that IDM described sub-phenotypes in prediabetes—led to new clinical studies
> - Understanding: Not all prediabetics progress the same way to diabetes
> - Sub-phenotyping involves clustering patients based on multiple biomarkers
> - This requires multivariate analysis, which aligns with my training in PCA, clustering
> - Mentioned mechanisms of remission in prediabetes—I'd be interested to learn more
> - Organ crosstalk (brain, liver, pancreas) suggests systems-level thinking needed

**Dr. Heni:** "We also work with neuroimaging data. Have you worked with imaging data before?"

> **Your Answer Points:**
> - Honest: No direct neuroimaging experience (MRI, fMEG)
> - But: Handled multi-dimensional array data (NetCDF similar structure to NIfTI)
> - Understand signal processing concepts from physics background
> - Willing to learn tools like FSL, SPM, or Python neuroimaging libraries
> - The analytical thinking transfers—it's about extracting patterns from complex data

---

### Pipeline Development

**Prof. Birkenfeld:** "The job mentions developing analysis pipelines. Can you describe a pipeline you've built?"

> **Your Answer Points:**
> - PostDoc: Built the Cyanobacteria Life Cycle model within ERGOM framework
> - Created analysis workflows: data ingestion → preprocessing → model runs → visualization
> - Used BASH scripting to automate batch processing
> - Currently learning Nextflow at CQ—industry-standard workflow management
> - Understand reproducibility: version control (Git), documentation
> - Would be excited to develop standardized pipelines for IDM research groups

---

### Grant Writing & Publications

**Prof. Preissl:** "You'd be supporting grant applications and publications. What's your experience with academic writing?"

> **Your Answer Points:**
> - 5 peer-reviewed publications from PhD
> - Contributed to methodology sections, results interpretation
> - Understand the structure of scientific papers
> - PhD required grant awareness—funding proposals for beam time at accelerator facilities
> - Clear communication: Presented at conferences (KIDA2017, IMAMPC)
> - Native-level English writing proficiency

---

### Career Transition Concern

**Prof. Birkenfeld:** "Let me be direct. You have a PhD. This position is E10 level—typically for BSc/MSc. Why would you take this step?"

> **Your Answer Points:**
> - Appreciate the directness
> - This is a strategic career move, not a desperate one
> - I'm entering a new field—I need to build domain expertise
> - Value: Access to unique clinical data, learning from experts like your team
> - Long-term: Want to grow in clinical bioinformatics, eventually independent research
> - I bring extra value: broader perspective, proven research capability
> - Two-year position gives time to demonstrate my contribution

---

### Cultural Fit

**Dr. Heni:** "You'd be working with multiple research groups. How do you handle collaborating across teams?"

> **Your Answer Points:**
> - PostDoc: Worked between marine biology and modeling groups
> - Had to translate between experimentalists and modelers
> - PhD: French lab, international team—adapted to different working styles
> - At CQ: Learning in mixed cohort—biologists, IT people, career changers
> - Enjoy the interface role—helping researchers answer their questions with data
> - German B1 certified—committed to integration

---

### Practical Questions

**Prof. Preissl:** "When could you start?"

> **Your Answer:**
> - Current CQ training ends in April 2026
> - HealthTwiSt internship: Feb-April 2026
> - Could potentially start May/June 2026
> - Flexible if earlier start needed—can discuss with CQ

**Prof. Preissl:** "Any questions for us?"

> **Questions to Ask:**
> 1. "What does a typical day look like for the bioinformatician here?"
> 2. "Which research groups would I primarily support?"
> 3. "What's the current data infrastructure—are there existing pipelines I'd extend?"
> 4. "How does the DZD network collaborate across sites?"
> 5. "What would success look like in the first 6 months?"

---

## Part 3: Post-Interview Discussion (Internal)

**Prof. Preissl:** So, impressions?

**Dr. Heni:** Stronger than expected. The modeling experience is actually an asset—he thinks systematically. And he's honest about gaps.

**Prof. Birkenfeld:** I was skeptical about the career change, but his reasoning is coherent. The CQ training shows commitment—it's not cheap or easy.

**Prof. Preissl:** The R and Python skills are there. He'd need to learn our specific data structures, but the foundation is solid.

**Dr. Heni:** And having someone who can actually write—grant support would be valuable. His English is excellent.

**Prof. Birkenfeld:** Shall we make an offer pending the ZAB evaluation for his foreign degrees?

**Prof. Preissl:** Let's. He's a calculated risk, but the upside is high.

---

## Key Preparation Points

| Topic | Key Points to Remember |
|-------|----------------------|
| **Prediabetes sub-phenotypes** | Patients cluster differently based on metabolic markers; not one-size-fits-all progression to diabetes |
| **Organ crosstalk** | Brain, liver, pancreas, fat—interconnected metabolic signals |
| **Prof. Preissl's work** | Metabolic Neuroimaging, brain insulin action, fMEG in fetuses |
| **Prof. Birkenfeld's department** | Prevention—how to stop diabetes before it develops |
| **Your unique value** | Systems thinking from modeling, processing large data, proven research output, commitment to transition |
| **Acknowledge gaps** | No direct clinical/neuroimaging experience—but transferable skills and active training |
