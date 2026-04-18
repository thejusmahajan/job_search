import re
import os
import sys

files = [
    "reference/cv_baseline/cv_english.tex",
    "applications/erlangen_stem_cell_biology/cv_erlangen.tex",
    "applications/geomar_zoom_in/cv_geomar.tex",
    "applications/hamburg_welcome_center/cv_hamburg.tex",
    "applications/helmholtz_munich/cv_helmholtz.tex",
    "applications/helmholtz_munich_staff_scientist/cv_helmholtz_munich.tex",
    "applications/mdc_berlin_ludwig_lab/cv_mdc.tex",
    "applications/octapharma_molecular_design/cv_octapharma.tex",
    "applications/robert_bosch_hospital/cv_robert_bosch.tex",
    "reference/cv_baseline/cv_custom.tex",
    "applications/erlangen_stem_cell_biology/cv_erlangen_de.tex",
    "applications/helmholtz_munich_staff_scientist/cv_helmholtz_munich_de.tex",
    "applications/octapharma_molecular_design/cv_octapharma_de.tex",
    "applications/robert_bosch_hospital/cv_robert_bosch_de.tex",
]

# wait! The user provided a totally different list!
# Let's read in the list the user provided:

user_files = [
  "reference/cv_baseline/cv_english.tex",
  "applications/erlangen_stem_cell_biology/cv_erlangen_en.tex",
  "applications/hamburg_mpimet_data/cv_mpimet_en.tex",
  "applications/hamburg_uke_bioinfo/cv_uke_en.tex",
  "applications/heidelberg_embl_bioinfo/cv_embl_en.tex",
  "applications/koeln_cecad_bioinfo/cv_cecad_en.tex",
  "applications/muenchen_helmholtz_bioinfo/cv_helmholtz_en.tex",
  "applications/tuebingen_meduni_biostat/cv_tuebingen_en.tex",
  "applications/freiburg_uniklinik_biostat/cv_freiburg_en.tex",
  "applications/goettingen_dzne_bioinfo/cv_dzne_en.tex",
  "reference/cv_baseline/cv_german.tex",
  "applications/erlangen_stem_cell_biology/cv_erlangen_de.tex",
  "applications/hamburg_mpimet_data/cv_mpimet_de.tex",
  "applications/hamburg_uke_bioinfo/cv_uke_de.tex",
  "applications/heidelberg_embl_bioinfo/cv_embl_de.tex",
  "applications/koeln_cecad_bioinfo/cv_cecad_de.tex",
  "applications/muenchen_helmholtz_bioinfo/cv_helmholtz_de.tex",
  "applications/tuebingen_meduni_biostat/cv_tuebingen_de.tex",
  "applications/freiburg_uniklinik_biostat/cv_freiburg_de.tex",
  "applications/goettingen_dzne_bioinfo/cv_dzne_de.tex"
]

grid_english = r"""
\begin{center}
    \vspace{0.1em}
    {\Large\textbf{EDUCATION}}\\
    {\color{cvtext}\rule{0.5\linewidth}{1.5pt}}\par
    \vspace{0.3em}
\end{center}

\begin{minipage}[t]{0.48\textwidth}
\cvexperience{Ph.D. in Astrochemistry}
             {Universit\'e Paris-Saclay, Institute of Molecular Sciences (ISMO)}
             {10/2015 - 09/2018}
             {Orsay, France}
             {{\small Supervisor: Dr.~Karine B\'eroff. Thesis: \textit{Excitation and fragmentation of C$_n$N$^+$ (n=1--3) in collisions with He atoms at intermediate velocity.}}}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.48\textwidth}
\cvexperience{Research Project -- Theoretical Atomic Physics}
             {IIT Mandi (under Dr.~Hari Varma)}
             {02/2015 - 08/2015}
             {Mandi, India}
             {{\small Theoretical atomic physics; partly remote.}}
\end{minipage}

\vspace{0.5em}

\begin{minipage}[t]{0.48\textwidth}
\cvexperience{M.Sc. in Physics}
             {National Institute of Technology Calicut, India}
             {07/2012 - 12/2014}
             {Calicut, India}
             {{\small First Class with Distinction (CGPA 8.71/10).}}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.48\textwidth}
\cvexperience{B.Sc. in Physics}
             {University of Calicut, India}
             {06/2009 - 04/2012}
             {Thrissur, India}
             {{\small Grade: B+ (CGPA 3.49/4.0).}}
\end{minipage}

\vspace{0.3cm}
\begin{minipage}[c]{0.48\textwidth}
\begin{flushleft}
{\Large Hamburg, 11 April 2026}
\end{flushleft}
\end{minipage}%
\hfill
\begin{minipage}[c]{0.48\textwidth}
\begin{flushright}
\includegraphics[height=1.2cm]{thejus signature.jpg}\\[0.05cm]
{\Large \textbf{Dr. Thejus Mahajan}}
\end{flushright}
\end{minipage}

\end{document}
"""

grid_german = r"""
\begin{center}
    \vspace{0.1em}
    {\Large\textbf{AUSBILDUNG}}\\
    {\color{cvtext}\rule{0.5\linewidth}{1.5pt}}\par
    \vspace{0.3em}
\end{center}

\begin{minipage}[t]{0.48\textwidth}
\cvexperience{Promotion in Astrochemie}
             {Universit\'e Paris-Saclay, Institute of Molecular Sciences (ISMO)}
             {10/2015 - 09/2018}
             {Orsay, Frankreich}
             {{\small Diss.: \textit{Excitation and fragmentation of C$_n$N$^+$ (n=1--3) in collisions with He atoms at intermediate velocity.}}}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.48\textwidth}
\cvexperience{Forschungsprojekt -- Theoretische Atomphysik}
             {IIT Mandi (unter Dr.~Hari Varma)}
             {02/2015 - 08/2015}
             {Mandi, Indien}
             {{\small Theoretische Atomphysik; teilweise remote.}}
\end{minipage}

\vspace{0.5em}

\begin{minipage}[t]{0.48\textwidth}
\cvexperience{M.Sc. in Physik}
             {National Institute of Technology Calicut, Indien}
             {07/2012 - 12/2014}
             {Calicut, Indien}
             {{\small First Class with Distinction (CGPA 8.71/10).}}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.48\textwidth}
\cvexperience{B.Sc. in Physik}
             {University of Calicut, Indien}
             {06/2009 - 04/2012}
             {Thrissur, Indien}
             {{\small B+ (CGPA 3,49/4,0). Anschl.~05--06/2012: Aufnahmepr\"ufung und Zulassung zum M.Sc.}}
\end{minipage}

\vspace{0.3cm}
\begin{minipage}[c]{0.48\textwidth}
\begin{flushleft}
{\Large Hamburg, 11. April 2026}
\end{flushleft}
\end{minipage}%
\hfill
\begin{minipage}[c]{0.48\textwidth}
\begin{flushright}
\includegraphics[height=1.2cm]{thejus signature.jpg}\\[0.05cm]
{\Large \textbf{Dr. Thejus Mahajan}}
\end{flushright}
\end{minipage}

\end{document}
"""

# Let's map real paths. The user provided paths might not map to the actual ones if some names got slightly modified.
import glob
all_tex_files = glob.glob("/scratch/local1/bioinformatics_project/job_search/**/*.tex", recursive=True)

processed = 0
for f in user_files:
    full_path = os.path.join("/scratch/local1/bioinformatics_project/job_search", f)
    # Check if the file exists directly or we need to find the equivalent
    if not os.path.exists(full_path):
        # The user said cv_erlangen_en.tex, but earlier it was cv_erlangen.tex.
        # Fallback to similar name:
        base = os.path.basename(f).replace("_en", "").replace("_de", "")
        # Actually let's just find the file in the dir
        dir_name = os.path.dirname(full_path)
        if os.path.exists(dir_name):
            potentials = [p for p in os.listdir(dir_name) if p.endswith(".tex") and "cover_letter" not in p]
            if potentials:
                # determine language
                is_de = f.endswith("_de.tex") or f.endswith("cv_german.tex") or f.endswith("custom.tex")
                # find the matching file based on language suffix or lack thereof
                match = None
                for pot in potentials:
                    if is_de and (pot.endswith("_de.tex") or "custom" in pot):
                        match = pot; break
                    elif not is_de and not pot.endswith("_de.tex"):
                        match = pot; break
                if match:
                    full_path = os.path.join(dir_name, match)
        if not os.path.exists(full_path):
            print(f"File not found or matched: {f}")
            continue
            
    print(f"Processing {full_path}")
    processed += 1
    with open(full_path, "r") as fh:
        content = fh.read()
            
    # 1. Add itemsep to any HealthTwiSt / Klinische Datenforschung itemize block
    content = re.sub(r'(\\cvexperience.*?HealthTwiSt.*?\n.*?\n.*?\n.*?\{.*?\\begin\{itemize\})([ \t\n]*\\item)', r'\1\\setlength{\\itemsep}{0.05em}\2', content, flags=re.DOTALL)
    
    # 2. Remove old Education/Ausbildung block completely
    content = re.sub(r"(\\vspace\{[0-9.]+cm\}\n)?\\cvsection\{(Education|Ausbildung)\}.*?(?=\\switchcolumn)", "", content, flags=re.DOTALL)
    
    # 3. Remove old signature block entirely from the end
    content = re.sub(r"(% --- Signature \(inside right column\) ---\n)?\\vspace\{[0-9.]+cm\}\n\\begin\{flushleft\}.*?\\end\{flushleft\}\n\n\\end\{paracol\}\n\\end\{document\}", r"\\end{paracol}", content, flags=re.DOTALL)

    # Note: If signature block was somewhere else, remove it too
    content = re.sub(r"\\vspace\{[0-9.]+cm\}\n\\begin\{flushleft\}\n\{\\small Hamburg.*?\\end\{flushleft\}", "", content, flags=re.DOTALL)
    
    # Also clean up \end{paracol} ... \end{document} with anything in between
    content = re.sub(r"\\end\{paracol\}.*", r"\\end{paracol}", content, flags=re.DOTALL)
    
    # 4. Append new grid
    # determine language securely
    if "Ausbildung" in content or "Kenntnisse" in content or "St\\\"arken" in content or f.endswith("_de.tex") or f.endswith("custom.tex"):
        new_app = grid_german
    else:
        new_app = grid_english
        
    content = content + "\n" + new_app
    
    with open(full_path, "w") as fh:
        fh.write(content)
        
print(f"Processed {processed} CVs.")

# Then run pdflatex for all
import subprocess
for f in user_files:
    # We gotta resolve path again to compile it
    # Same logic to find path
    full_path = os.path.join("/scratch/local1/bioinformatics_project/job_search", f)
    if not os.path.exists(full_path):
        dir_name = os.path.dirname(full_path)
        if os.path.exists(dir_name):
            potentials = [p for p in os.listdir(dir_name) if p.endswith(".tex") and "cover_letter" not in p]
            is_de = f.endswith("_de.tex") or f.endswith("cv_german.tex")
            match = None
            if potentials:
                for pot in potentials:
                    if is_de and (pot.endswith("_de.tex") or "custom" in pot or "german" in pot):
                        match = pot; break
                    elif not is_de and not pot.endswith("_de.tex") and "custom" not in pot and "german" not in pot:
                        match = pot; break
            if match:
                full_path = os.path.join(dir_name, match)
                
    if os.path.exists(full_path):
        out_dir = os.path.dirname(full_path)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", f"-output-directory={out_dir}", full_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
