# Domain Knowledge — Healthcare, Clinical Data & Compliance

## Interventional Radiology

| Topic | Knowledge Acquired |
|---|---|
| **DeGIR modules** | A/E = vascular opening (body/brain), B/F = vascular blocking (body/brain), C = non-vascular, D = oncology. Mirror pairs: body (A/B/C/D) and brain (E/F). |
| **Intervention types** | ~33 types including catheter insertions, tumor ablations (RFA, MWA, TACE), stroke thrombectomy, embolization, stenting (carotid, aortic), port implantation, PICC lines, foreign body retrieval, prostate artery embolization (PAE), TIPSS |
| **Complication grading** | SIR standard: 7-grade severity scale (kein_T=none, A–B=minor, C–F=major, Tod=death). Applied across 3 slots (K1, K2, K3). |
| **Success criteria** | Per-intervention Erfolg/Teilerfolg/Misserfolg — some single-column, some multi-condition with regex |
| **Quality registry operations** | ~300 German clinics submitting via samedi platform. Annual reports for DeGIR board. |
| **Radiation dose metrics** | DLP (Dose Length Product), DAP (Dose Area Product), CTDI (CT Dose Index), fluoroscopy time |

## Clinical Data Management

| Skill | Application |
|---|---|
| **GDPR/DSGVO compliance** | Real patient data: birth dates anonymized, doctor names stripped, no patient data in version control, local processing only |
| **BDSG** (Bundesdatenschutzgesetz) | German federal data protection law — additional requirements beyond GDPR |
| **Ärztliche Schweigepflicht** | Medical confidentiality law — governs data handling beyond GDPR |
| **Data quality issues** | Non-standardized physician entries, missing values, duplicated columns, inconsistent module assignments |
| **Multi-site data harmonization** | Standardizing intervention labels and module assignments across ~300 independently-managed clinics |
| **Registry data lifecycle** | Collection → curation → quality assurance → statistical reporting → delivery to clinical governance boards |

## Statistical Reporting for Clinical Governance

| Area | What I Worked With |
|---|---|
| Descriptive statistics | Median, quartiles, frequency tables, intervention counts per clinic |
| Complication rates | Minor vs. major complication rates by module, intervention, clinic |
| Benchmarking | Individual clinic metrics vs. national averages |
| Report generation | LaTeX PDF reports via R Markdown/knitr with kableExtra tables |
| Data visualization | Interactive Plotly charts, publication-quality ggplot2 figures |
