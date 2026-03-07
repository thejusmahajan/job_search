# Ludwig Lab Domain Knowledge: A Primer

## 1. The Core Focus: Single-Cell Genomics
Traditional sequencing (bulk RNA-seq) averages out the signals from thousands of cells, like mixing a smoothie. **Single-cell sequencing** isolates individual cells before measuring, giving you the exact readout per cell, like looking at the individual fruits in the bowl.

The Ludwig Lab focuses on **hematopoiesis** (how blood stem cells differentiate into all blood cell types) and how mitochondrial mutations affect this process and cause diseases like leukemia.

## 2. Key Modalities
A "modality" is just a type of biological molecule you are measuring.
- **DNA (Genomics):** The stable blueprint.
- **Chromatin Accessibility (ATAC-seq):** DNA is normally wrapped tightly. When a gene needs to be read, the DNA opens up. ATAC-seq measures *where* the genome is open. Open chromatin = active regulatory regions.
- **RNA (Transcriptomics / RNA-seq):** The "read out" messages from the DNA. Measures which genes are actually being expressed.
- **Proteins (Proteomics):** The functional machines built from the RNA.

## 3. The Lab's Proprietary Technologies (Multi-omics)
"Multi-omics" means measuring more than one modality in the *exact same single cell* at the same time. This is technically very difficult but computationally very powerful.

### mtscATAC-seq (Mitochondrial single-cell ATAC-seq)
Developed by Leif Ludwig. 
- **What it does:** It measures chromatin accessibility (ATAC) AND detects mutations in mitochondrial DNA (mtDNA) simultaneously in single cells.
- **Why it matters:** mtDNA mutations act as natural "barcodes". Because they are passed down as cells divide, you can use these mutations to build a family tree of the cells (clonal lineage tracing) while simultaneously seeing what those cells are doing (epigenetic state via ATAC).

### DOGMA-seq (Dogma of biology)
- **What it does:** Measures chromatin accessibility (DNA), gene expression (RNA), and surface proteins simultaneously in the exact same cell.
- **Why it matters:** It captures the entire "Central Dogma" of biology (DNA -> RNA -> Protein) at once, allowing researchers to see exactly how changes in chromatin lead to changes in RNA and ultimately protein levels.

### PERFF-seq
- **What it does:** Similar to DOGMA-seq, but optimized for fixed cells or specific permeabilization states, allowing for robust multi-omic profiling (e.g., protein and RNA) under challenging conditions.

## 4. Why They Need You (The Computational Bottleneck)
These technologies produce massive, sparse (lots of zeroes), and noisy data matrices. 
1. **Pipelines (Your Strength):** Before any analysis happens, raw sequencer data (FASTQ files) must be aligned, demultiplexed, and quantified. This requires massive HPC pipelines (like Nextflow).
2. **Integration (ML Need):** If you have RNA data, ATAC data, and Protein data for the same 10,000 cells, how do you mathematically combine them to define "cell states"? Standard statistics fail here. You need Machine Learning (dimensionality reduction like PCA/UMAP, multimodal clustering) to integrate these sparse matrices.
