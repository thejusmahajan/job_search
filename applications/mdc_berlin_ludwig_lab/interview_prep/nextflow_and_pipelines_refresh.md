# Nextflow & Pipeline Engineering Refresh

## 1. Nextflow (DSL2) Core Concepts
Nextflow is a workflow manager that combines a domain-specific language (DSL) for defining pipelines with a powerful executor that handles parallelization on HPCs or the cloud.

### Processes
The basic unit of execution. A process contains the command to be executed (often bash/python/R).
```groovy
process ALIGN_READS {
    input:
    path reads
    
    output:
    path "aligned.bam"
    
    script:
    """
    minimap2 -a ref.fa $reads > aligned.sam
    samtools view -bS aligned.sam > aligned.bam
    """
}
```

### Channels
The conduits that pass data between processes. They handle the asynchronous execution.
There are two main types:
- **Queue channels:** Data flows through them (like an assembly line). Think of the actual FASTQ files.
- **Value channels:** A single value bound to the channel, passed to every execution.

### Workflows (DSL2 specific)
In DSL2 (Nextflow 20.07+), processes are completely separated from the workflow definition, allowing them to be imported as modules.
```groovy
include { ALIGN_READS } from './modules/align.nf'

workflow {
    reads_ch = Channel.fromPath( '*.fastq' )
    ALIGN_READS(reads_ch)
}
```

## 2. Your Highlighted Experiences to Mention

### The Hepatitis Delta Pipeline
- **What you built:** An automated Nextflow pipeline.
- **Steps:** 
  1. Used **NCBI Entrez** (Biopython) to fetch reference sequences.
  2. Performed Multiple Sequence Alignment (MSA) using **MAFFT**.
  3. Trimmed the alignments using **trimAl** to remove noisy gap regions.
- **Dependency Management:** You used **Conda** integration within Nextflow (`conda 'bioconda::mafft'`) to ensure the pipeline is 100% reproducible anywhere without manual software installation.

### The HealthTwiSt Medical Pipeline Refactoring (DeGIR)
*This is your strongest proof of pipeline engineering maturity.*
- **The Scale:** 143,000 patient records × 1,920 variables.
- **The Achievement:** You didn't just write code; you *refactored* a massive production pipeline (1,834 lines of R/tidyverse).
- **The Method:** 
  - Externalized hardcoded rules into configuration files (reduced 257 rules to 8 configs).
  - Achieved a 26.5% code reduction.
  - **Crucial point:** Emphasize the **Byte-level verification (`identical()`)**. You verified that your refactored code produced the *exact same outputs* as the old code. This shows discipline and safety, which PIs love.

## 3. Interview Talking Points
- **Reproducibility:** You understand that computational biology requires absolute reproducibility. That's why you use Nextflow and Conda/Docker.
- **Scale:** You are comfortable working on HPCs (Jülich training) and processing terabytes of data (Paris-Saclay PhD).
- **Resilience:** Your ability to refactor the DeGIR pipeline demonstrates that you can take messy, academic "spaghetti code" and turn it into professional, maintainable software.
