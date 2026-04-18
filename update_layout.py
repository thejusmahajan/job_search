import re

cv_path = "/scratch/local1/bioinformatics_project/job_search/reference/cv_baseline/cv_english.tex"

with open(cv_path, "r") as f:
    content = f.read()

# 1. Extract and remove the Education block
ed_pattern = re.compile(
    r"(\\vspace\{[0-9.]+cm\}\n)?\\cvsection\{Education\}.*?(?=\\switchcolumn)",
    re.DOTALL
)
m_ed = ed_pattern.search(content)

if not m_ed:
    print("Education block not found!")
    exit(1)

ed_block = m_ed.group(0)
content = content.replace(ed_block, "")

# 2. Extract and remove the signature block
sig_pattern = re.compile(
    r"(% --- Signature \(inside right column\) ---\n)?\\vspace\{[0-9.]+cm\}\n\\begin\{flushleft\}.*?\\end\{flushleft\}\n",
    re.DOTALL
)
m_sig = sig_pattern.search(content)

if not m_sig:
    print("Signature block not found!")
    exit(1)

sig_block = m_sig.group(0)
content = content.replace(sig_block, "")

# We need to construct the new Education block from the raw ed_block.
# We will just write it explicitly since we know the content.

new_ed_grid = r"""
\begin{center}
    \vspace{0.4em}
    {\Large\textbf{EDUCATION}}\\
    {\color{cvtext}\rule{0.5\linewidth}{1.5pt}}\par
    \vspace{0.8em}
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

\vspace{1.5em}

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
"""

# Insert perfectly right after \end{paracol}
# Make sure we clean up multiple empty lines
content = re.sub(r"\\end\{paracol\}\s*\\end\{document\}", "\\\\end{paracol}\n", content)

content += new_ed_grid + "\n\n" + "\\vspace{0.8cm}\n\\begin{flushleft}\n{\\small Hamburg, 11 April 2026}\\\\[0.15cm]\n\\includegraphics[height=0.7cm]{thejus signature.jpg}\\\\[0.05cm]\n{\\small \\textbf{Dr. Thejus Mahajan}}\n\\end{flushleft}\n\n\\end{document}\n"

with open(cv_path, "w") as f:
    f.write(content)

print("Updated cv_english.tex")
