# FZJ IBG-4 FAIRagro — Requirements & Fit Analysis

## 1. Position snapshot
- **Institute**: Forschungszentrum Jülich (FZJ), Institute of Bio- and Geosciences, Department of Bioinformatics (IBG-4)
- **Group leader**: Prof. Dr. Björn Usadel
- **Project**: FAIRagro (NFDI consortium — FAIR research data infrastructure for agrosystems, DFG-funded, 2023–2028)
- **Tasks**: Implement central search services and an inventory service for FAIRagro's distributed research data infrastructure
- **Contract**: 1.5 years, TVöD-Bund E10-11 or E13 (depending on qualification)
- **Location**: Jülich
- **Language**: English (ad is English, Jülich is international campus)
- **Deadline**: Open until filled

## 2. Muss-Anforderungen (hard requirements)
| Requirement | Evidence | Strength |
|:---|:---|:---|
| Degree (BSc/MSc) in CS, bioinformatics, or equivalent | PhD Astrochemistry, MSc Physics, Bioinformatics/Biostatistics Weiterbildung | Strong |
| Practical web development experience | R Shiny dashboard (6 modules, plotly, DT, bslib, deployed to shinyapps.io); GitHub Pages website; Nextflow pipeline with NCBI API integration | Partial |
| Database design & applications | SQL (bioinformatics databases, NCBI), config-driven CSV architecture for 143K-record pipeline, NetCDF/HDF5 data management | Partial |
| Team/communication/organizational skills | Authored teaching materials (Quarto/GitHub), physics tutoring (2018–2021), collaborative pipeline refactoring, conference presentations | Strong |
| English C1+ | Fluent C1, 5 peer-reviewed publications in English | Strong |

## 3. Kann-Anforderungen (desired)
| Requirement | Evidence | Strength |
|:---|:---|:---|
| Agricultural/plant sciences domain data | Not present | Gap |
| German language | B1 (Goethe-Zertifikat), B2 in preparation | Bonus met |

## 4. Key tasks → candidate assets
- **Implement central search services**: Built an interactive R Shiny search dashboard (6 modules) with full-text search, filtering, and dynamic visualizations — directly analogous to building discovery portals for research data.
- **Develop inventory service**: Created a config-driven data architecture (257 rules → 8 CSVs) providing a searchable overview of business rules for ~300 clinics — demonstrates experience building registry/inventory systems.
- **Research data management collaboration**: Collaborated closely with Dr. Busjahn on data pipeline refactoring, maintaining reproducibility (byte-identical output via `identical()`); built Nextflow DSL2 pipeline with FAIR-compatible reproducibility principles (Conda dependencies, automated NCBI download).
- **Present results at conferences/publish**: 5 peer-reviewed publications, conference presentations, authored teaching materials published on GitHub.

## 5. Unique Selling Proposition (USP)
Thejus bridges the gap between scientific computing and research data infrastructure. His pipeline work demonstrates the core RDM discipline: externalized metadata (257 correction rules into CSV configs), reproducible workflows (Nextflow DSL2 + Conda), automated data retrieval from public APIs (NCBI), and interactive data discovery (R Shiny). Unlike purely front-end web developers, he brings deep domain understanding of scientific data formats (NetCDF, HDF5), sequence analysis databases, and HPC — including training at JSC Jülich itself. This makes him uniquely suited to building search services that scientists actually find useful.

## 6. Gap analysis
- **Full-stack web development**: The candidate's web development is R Shiny + static sites, not React/Django/Node.js. *Strategy*: Foreground the Shiny dashboard as a "user-oriented web application" (which it is), and express willingness to learn additional web frameworks.
- **Agricultural/plant sciences**: No direct domain experience. *Strategy*: Honest omission. Highlight transferability from ecological modeling (marine ecosystems → plant/environmental systems: both deal with climate data, time-series environmental datasets, NetCDF, species data).

## 7. CV re-weighting plan
- **Title subtitle**: Change to "Software Developer | Research Data Management · Bioinformatics · Data Pipelines"
- **Key Strengths (sidebar)**: Reorder to (1) Research Data Management & FAIR Principles, (2) Data Pipeline Engineering, (3) Bioinformatics & Reproducible Research
- **Technical Skills**: Rename "Data Engineering" → "RDM & Data Infrastructure"; promote FAIR, metadata, web services
- **Profile bullets**: Re-frame around RDM/search services/FAIR principles
- **HealthTwiSt bullets**: Emphasize config-driven metadata architecture and Shiny dashboard as web application
- **All dates, facts, publication entries**: Unchanged from baseline ground truth

## 8. Cover letter skeleton
1. **Hook**: Connect pipeline reproducibility work and R Shiny search dashboard to FAIRagro's mission of making agricultural research data FAIR
2. **Qualification**: DeGIR pipeline (config-driven architecture, 143K records), R Shiny dashboard (user-oriented web app), Nextflow DSL2 pipeline (reproducible workflows), SQL/database skills, HPC training at JSC Jülich
3. **Motivation**: FAIRagro's vision of connecting distributed research repositories resonates with candidate's proven commitment to reproducible, searchable, interoperable data infrastructure
4. **Close**: Immediately available, look forward to interview, enclosures
