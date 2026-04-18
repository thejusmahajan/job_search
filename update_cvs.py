import os
import re
import glob

base_dir = "/scratch/local1/bioinformatics_project/job_search"

# Find all .tex files
tex_files = glob.glob(os.path.join(base_dir, "**", "*.tex"), recursive=True)

# Filter out cover_letters and motivation_letters
cv_files = [f for f in tex_files if not os.path.basename(f).startswith("cover_letter") and not os.path.basename(f).startswith("motivation_letter")]

english_items = r"""\begin{itemize}
                   \item Refactored a monolithic 1,834-line R data pipeline (tidyverse) for Germany's interventional radiology quality registry (DeGIR); 143,000+ patient records from \textasciitilde300 clinics. Reduced to 1,348 lines ($-$26.5\%) with byte-identical output verified via \texttt{identical()}.
                   \item Externalised 257 hard-coded correction rules into 8 configuration CSV files, enabling non-programmer editing of business rules.
                   \item Replaced 357 deprecated function calls across 4 pipeline files, modernising the codebase to current tidyverse standards.
                   \item Created the \texttt{degirtools} R package (9 exported functions, roxygen2 docs, \texttt{devtools::check()} passing) by extracting reusable logic from a 767-line helper file.
                   \item Discovered 2 pre-existing bugs through systematic code analysis; documented both and preserved original behaviour for supervisor review --- demonstrating production-code discipline.
                   \item Built an interactive R Shiny dashboard (6 modules: overview, interventions, complications, radiation doses, success rates, about) using plotly, DT, and bslib. Deployed to shinyapps.io with GDPR-safe synthetic data.
                   \item Wrote Tidymodels teaching materials (Quarto/GitHub) replacing the legacy caret framework for ML workflows in R.
               \end{itemize}"""

german_items = r"""\begin{itemize}
                   \item Refactoring einer monolithischen 1.834-Zeilen R-Datenpipeline (tidyverse) f\"ur das interventionell-radiologische Qualit\"atsregister Deutschlands (DeGIR); 143.000+ Patientendatens\"atze von \textasciitilde300 Kliniken. Reduktion auf 1.348 Zeilen ($-$26,5\%) mit byte-identischer Ausgabe, verifiziert via \texttt{identical()}.
                   \item Externalisierung von 257 hardcodierten Korrekturregeln in 8 Konfigurations-CSV-Dateien; erm\"oglicht Bearbeitung durch Nicht-Programmierer.
                   \item Ersetzung von 357 veralteten Funktionsaufrufen in 4 Pipeline-Dateien; Modernisierung auf aktuelle tidyverse-Standards.
                   \item Erstellung des R-Pakets \texttt{degirtools} (9 exportierte Funktionen, roxygen2-Dokumentation, \texttt{devtools::check()} bestanden) durch Extraktion wiederverwendbarer Logik aus einer 767-Zeilen-Hilfsdatei.
                   \item Entdeckung von 2 vorbestehenden Fehlern durch systematische Codeanalyse; dokumentiert und originales Verhalten f\"ur Supervisor-Review beibehalten --- Demonstration von Produktionscode-Disziplin.
                   \item Aufbau eines interaktiven R-Shiny-Dashboards (6 Module: \"Ubersicht, Interventionen, Komplikationen, Strahlendosen, Erfolgsraten, Info) mit plotly, DT und bslib. Deployment auf shinyapps.io mit DSGVO-konformen synthetischen Daten.
                   \item Erstellung von Tidymodels-Lehrmaterialien (Quarto/GitHub) als Ersatz f\"ur das veraltete caret-Framework f\"ur ML-Workflows in R.
               \end{itemize}"""

for cv_file in cv_files:
    if "cv_custom.log" in cv_file or "BEWERBUNG" in cv_file:
        continue
        
    with open(cv_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    orig_content = content
    
    is_german = "_de.tex" in cv_file
    
    # 1. Update Internship Items
    # Find {HealthTwiSt GmbH} and the next \begin{itemize} ... \end{itemize}
    start_idx = content.find('{HealthTwiSt GmbH}')
    if start_idx != -1:
        itemize_start = content.find('\\begin{itemize}', start_idx)
        itemize_end = content.find('\\end{itemize}', itemize_start)
        if itemize_start != -1 and itemize_end != -1:
            items_to_replace = content[itemize_start:itemize_end+13]
            if is_german:
                content = content[:itemize_start] + german_items + content[itemize_end+13:]
            else:
                content = content[:itemize_start] + english_items + content[itemize_end+13:]

    # 2. Update Profile
    en_profile_old = r"Currently: Internship in clinical data research at HealthTwiSt GmbH (medical data pipeline, 143K+ records)."
    en_profile_new = r"Internship at HealthTwiSt GmbH: refactored a production R pipeline (DeGIR registry, 143K+ records, \textasciitilde300 clinics), built an R Shiny dashboard, and created the degirtools R package."
    
    de_profile_old1 = r"Zurzeit: Praktikum in der klinischen Datenforschung bei HealthTwiSt GmbH (medizinische Datenpipeline, 143K+ Datens\"atze)."
    de_profile_old2 = r"Zurzeit: Praktikum in der klinischen Datenforschung bei HealthTwiSt GmbH (medizinische Datenpipeline, 143K+ Datens\"atze)."
    de_profile_new = r"Praktikum bei HealthTwiSt GmbH: Refactoring einer Produktions-R-Pipeline (DeGIR-Register, 143K+ Datens\"atze, \textasciitilde300 Kliniken), Aufbau eines R-Shiny-Dashboards und Erstellung des R-Pakets degirtools."
    
    # Simple replace
    content = content.replace("Currently: Internship in clinical data research at HealthTwiSt GmbH (medical data pipeline, 143K+ records).", en_profile_new)
    # the parenthesis might need escaping in regex, but replace is exact match.
    content = content.replace('Zurzeit: Praktikum in der klinischen Datenforschung bei HealthTwiSt GmbH (medizinische Datenpipeline, 143K+ Datens\\"atze).', de_profile_new)
    # sometimes the string can have different line breaks etc, let's use regex for safer match
    if is_german:
        # Just in case
        content = re.sub(r'Zurzeit:\s*Praktikum\s*in\s*der\s*klinischen\s*Datenforschung\s*bei\s*HealthTwiSt\s*GmbH[^.]+\.', de_profile_new, content)
    else:
        content = re.sub(r'Currently:\s*Internship\s*in\s*clinical\s*data\s*research\s*at\s*HealthTwiSt\s*GmbH[^.]+\.', en_profile_new, content)

    # 3. Key Strengths
    if is_german:
        # Find \cvstrength{\faStar}{Datenpipeline-Engineering}{...}
        pattern = r'(\\cvstrength\{\\faStar\}\s*\{Datenpipeline-Engineering\}\s*)\{.*?\}'
        repl = r'\g<1>{Refactoring einer Produktions-Datenpipeline (1.834 Zeilen, 143K Datens\\"atze, \\textasciitilde300 Kliniken) mit 26,5\\% Codereduktion. Erstellung des R-Pakets degirtools. Byte-Level-Verifizierung nach jeder \\"Anderung via \\texttt{identical()}.}'
        content = re.sub(pattern, repl, content, flags=re.DOTALL)
    else:
        pattern = r'(\\cvstrength\{\\faStar\}\s*\{Data Pipeline Engineering\}\s*)\{.*?\}'
        repl = r'\g<1>{Refactored a production data pipeline (1,834 lines, 143K records, \\textasciitilde300 clinics) with 26.5\\% code reduction. Built degirtools R package. Byte-level verification after every change via \\texttt{identical()}.}'
        content = re.sub(pattern, repl, content, flags=re.DOTALL)

    # 4. Technical Skills
    # Add R Shiny and devtools/roxygen2 to "Data Engineering / Dateningenieurwesen"
    if is_german:
        # Find Dateningenieurwesen section
        m = re.search(r'\\cvskills\{Dateningenieurwesen\}\s*\{(.*?)\}', content, flags=re.DOTALL)
        if m:
            skills = m.group(1)
            # check if R Shiny is there
            if "R Shiny" not in skills:
                new_skills = skills + ", R Shiny, devtools/roxygen2"
                content = content.replace(m.group(0), f"\\cvskills{{Dateningenieurwesen}}\n         {{{new_skills}}}")
    else:
        m = re.search(r'\\cvskills\{Data Engineering\}\s*\{(.*?)\}', content, flags=re.DOTALL)
        if m:
            skills = m.group(1)
            if "R Shiny" not in skills:
                new_skills = skills + ", R Shiny, devtools/roxygen2"
                content = content.replace(m.group(0), f"\\cvskills{{Data Engineering}}\n         {{{new_skills}}}")

    # 5. Date
    content = content.replace("11 March 2026", "11 April 2026")
    content = content.replace("10 March 2026", "11 April 2026")
    content = content.replace("10. März 2026", "11. April 2026")
    content = content.replace("11. März 2026", "11. April 2026")
    content = content.replace('10. M\\"arz 2026', '11. April 2026')
    content = content.replace('11. M\\"arz 2026', '11. April 2026')

    if content != orig_content:
        with open(cv_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {cv_file}")

print("Done.")
