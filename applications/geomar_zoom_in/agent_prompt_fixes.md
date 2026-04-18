# Agent Prompt: Fix GEOMAR ZOOM-IN Application Documents (Round 2)

## Your Role
You are an expert academic application writer. You are fixing specific issues in the CV and cover letter for Dr. Thejus Mahajan's GEOMAR ZOOM-IN postdoc application. The documents already exist and are mostly good — you are making targeted corrections, NOT a full rewrite.

## CRITICAL RULES

1. **Do NOT rewrite sections that are working well.** Only change what is listed below.
2. **Do NOT introduce new content** beyond what is specified in these fixes.
3. **Do NOT change the overall structure or ordering** — it is correct.
4. **After every edit, re-read the file to make sure you haven't broken LaTeX syntax.**
5. **Compile both files with pdflatex (run twice each) after all edits are done.**
6. **Verify page counts after compilation:** Cover letter = 1 page. CV = 2–3 pages (academic CVs of 3 pages are perfectly acceptable).

## Working Directory
`/scratch/local1/bioinformatics_project/job_search/applications/geomar_zoom_in/`

---

## COVER LETTER FIXES (`cover_letter_geomar.tex`)

### Fix 1: Must fit on exactly 1 page
The current cover letter spills onto page 2 — the signature, name, and enclosures line are on a blank second page. This is unacceptable. Apply these changes IN ORDER until it fits on 1 page:

- **Step A:** Tighten the geometry. Try: `\usepackage[margin=2.0cm, top=2.0cm, bottom=1.5cm]{geometry}`
- **Step B:** Reduce `\vspace` values between sender/date/recipient blocks (e.g., 0.1cm → 0.05cm or remove entirely where possible)
- **Step C:** If still overflowing, reduce font from 9pt to 8.5pt or try `\usepackage[10pt]{type1cm}` with `\fontsize{9}{10.5}\selectfont`
- **Step D:** As a last resort, shorten the body text as described in Fix 2 below

**The signature image, "Dr. Thejus Mahajan" name, and the "Enclosures:" line MUST all appear on page 1.** Do NOT remove the signature or enclosures — compress the content to fit.

### Fix 2: Split and tighten paragraph 4
The current paragraph 4 is overloaded — it mixes (a) connection to Xue's research, (b) teaching, and (c) manuscript in preparation into one dense block. Fix as follows:

**Replace the current paragraph 4 with TWO shorter segments:**

Segment A (connection to PI's work + OMZ motivation):
> Your recent work on the interplay between bottom-up and top-down controls on phytoplankton (e.g., Xue et al., *Biogeosciences*, 2024), particularly how changes in the physical environment impact zooplankton grazing pressure, strongly resonates with my own findings on phytoplankton responses to environmental drivers. I am eager to extend this perspective to the Peruvian upwelling system, investigating how zooplankton DVM connects surface productivity with nitrogen loss in the oxygen minimum zone.

Segment B (manuscript + teaching — concise, 1–2 sentences):
> I am currently preparing a manuscript on my IBM trait-diffusion modelling results in collaboration with Prof. Dr. Elisa Schaum (University of Hamburg) and Prof. Dr. Kai Wirtz (Helmholtz-Zentrum Hereon). I also contributed to teaching Marine Ecosystem Modelling at BSc and MSc level at the University of Hamburg.

**Key changes from original:**
- Removed "Furthermore" bridge that awkwardly connected Xue's research to teaching
- "co-instructing" → "contributed to teaching" (more accurate — the user taught part of the BSc course and gave a 2-day MSc guest lecture; "co-instructing" overstates the role)
- Teaching is now a clean factual sentence, not wedged between the OMZ discussion and the manuscript

**IMPORTANT:** After this restructuring, verify the letter still fits on 1 page. If the two segments make it longer, compress language. Every sentence must earn its place.

### Fix 3: Date
Keep `\today` — that is fine. The applicant will set the final date at submission time.

---

## CV FIXES (`cv_geomar.tex`)

### Fix 4: CV page length — RELAXED constraint
Academic CVs of 3 pages are perfectly normal for a postdoc application. Do NOT aggressively compress. However, do apply these sensible tidying steps:

- **Step A:** Compact Languages into a single line or inline format:
```latex
\section{\sc Languages}
English (proficient), German (B1 -- Goethe Certified), French (intermediate), Malayalam (native)
```
- **Step B:** Reduce excessive `\vspace*{.05in}` between entries to `\vspace*{.03in}` for consistency — but do NOT remove spacing entirely. The CV should breathe.
- **Step C:** Avoid a nearly-empty final page. If page 3 has only a few lines, tighten spacing so that either the content fills page 3 reasonably or everything fits on 2. Use your judgment — do NOT leave a page with 3 lonely lines.

### Fix 5: Remove website from Contact Information
The website (thejusmahajan.github.io) showcases data science skills that are not relevant to this application. **Remove the website line entirely** from the Contact Information section. Keep: address, email, phone, LinkedIn, Google Scholar.

**Replace the current Contact Information tabular with:**
```latex
\section{\sc Contact Information}

\vspace{.05in}
\begin{tabular}{@{}p{3.75in}p{2in}}
 Reventlowstra{\ss}e 17 & Email: \verb+thejus.mahajan@uni-hamburg.de+\\
 22605 Hamburg & Ph: +49-15259697629 \\
 Germany & \\
 \url{https://www.linkedin.com/in/thejusmahajan/} & \url{https://scholar.google.com/citations?user=PJkZwAwAAAAJ}
\end{tabular}
```

### Fix 6: Fill the Feb–Apr 2025 gap
Between the postdoc ending (January 2025) and Hereon starting (May 2025), there is a 4-month unexplained gap. Add a minimal entry:

```latex
\begin{itemize}
\item {\bf German Language Studies}\\
\vspace*{-.2in}
\item[] Goethe B1 Certification\\
February 2025 -- April 2025
\end{itemize}
\vspace*{.03in}
```

Place this AFTER the postdoc entry and BEFORE the Hereon Guest Scientist entry. Keep it to exactly this — no bullet points, no description beyond the certification name.

### Fix 7: Reframe HealthTwiSt under data analysis
The job advertisement explicitly requires: "A background in analyzing large datasets and visualizing data using Python, MATLAB, or equivalent."

The HealthTwiSt internship involved processing a 143,000-row × 1,920-column dataset and refactoring a data pipeline. This IS large-scale data analysis experience — frame it that way without mentioning medical/clinical context.

**Replace the current HealthTwiSt entry:**
```
Internship – Data Pipeline Engineering
February 2026 – April 2026
- Data pipeline engineering internship (R/tidyverse) — completing April 2026.
```

**With:**
```
Internship – Large-Scale Data Analysis & Pipeline Engineering
February 2026 – April 2026
- Refactored and optimized a data processing pipeline (R/tidyverse) for a 143,000-row dataset; automated quality assurance and validation workflows.
```

This frames it as data analysis competence (which the ad asks for) without mentioning clinical/medical context (which is irrelevant to GEOMAR).

### Fix 8: Move manuscript in preparation to FIRST item in Publications
The manuscript in preparation should appear FIRST in the publications section, before the numbered list of published papers, with a clear "In preparation" tag.

**Replace the entire Publications section with:**
```latex
\section{\sc Publications}

Google Scholar: \url{https://scholar.google.com/citations?hl=en&user=PJkZwAwAAAAJ}

\textbf{In preparation:}
\begin{list2}
\item T. Mahajan, E. Schaum, K. Wirtz. \textit{Cyanobacteria life-cycle modelling and individual-based model trait-diffusion results.} In preparation.
\end{list2}

\textbf{Peer-reviewed (5 articles):}
\begin{enumerate}
\item T. Mahajan, et al. \textit{Journal of Physics: Conference Series}, 1412:142026, 2020.
\item T. Idbarkach, et al. \textit{Astronomy \& Astrophysics}, 628:A75, 2019.
\item T. Mahajan, et al. \textit{Journal of Physics B}, 2019.
\item T. Idbarkach, et al. \textit{Journal of Physics B}, 51(24):245201, 2018.
\item T. Idbarkach, et al. \textit{Journal of Physics: Conference Series}, 1412(11):112028, 2020.
\end{enumerate}
```

This gives the in-progress manuscript maximum visibility — it is the most relevant publication for this application.

### Fix 9: Fix References section — accurate titles, roles, and phone numbers
The references section needs precise institutional titles, roles, and phone numbers. **Replace the entire References section with:**

```latex
\section{\sc References}

\begin{itemize}
\item {\bf Prof. Dr. Elisa Schaum}\\
Head of Research Unit Plankton\"okologie\\
Institut f\"ur marine \"Okosystem- und Fischereiwissenschaften, University of Hamburg\\
Email: \texttt{elisa.schaum@uni-hamburg.de}\\
Phone: +49 40 2395-26625\\
Relation: Postdoctoral collaborator

\item {\bf Prof. Dr. Kai Wirtz}\\
Head of Department Ecosystem Modelling\\
Institute of Coastal Systems -- Analysis and Modelling, Helmholtz-Zentrum Hereon\\
Email: \texttt{kai.wirtz@hereon.de}\\
Phone: +49 4152 87-1513\\
Relation: Guest Scientist supervisor
\end{itemize}
```

**CRITICAL — get these details exactly right:**
- Elisa Schaum: **Postdoctoral collaborator** (NOT supervisor). Head of Research Unit "Planktonökologie". Institute: "Institut für marine Ökosystem- und Fischereiwissenschaften". Phone: +49 40 2395-26625.
- Kai Wirtz: **Guest Scientist supervisor**. Head of Department "Ecosystem Modelling". Institute: "Institute of Coastal Systems – Analysis and Modelling". Phone: +49 4152 87-1513.

### Fix 10: Add dates to Teaching Experience
The teaching section currently has no dates. Add approximate timeframes:

```latex
\section{\sc Teaching Experience}

\begin{itemize}
\item {\bf Marine Ecosystem Modelling} (BSc level)\\
University of Hamburg, 2022--2023\\
Regular teaching contribution.

\vspace*{.03in}
\item {\bf ``From 0D to 1D'' -- Advanced Marine Ecosystem Modelling} (MSc level)\\
University of Hamburg, 2023\\
2-day guest lecture as part of ``Introduction to Biological Oceanography and Fisheries Science'' course.
\end{itemize}
```

**NOTE TO AGENT:** The dates 2022–2023 are approximate — they fall within the postdoc period (2021–2025). If you are uncertain about exact dates, use the postdoc period range. Do NOT invent specific semesters. The user can adjust later.

### Fix 11: Fix parental leave phrasing
Replace:
```
- Including parental leave 01/2024–12/2024.
```

With:
```
- Parental leave: 01/2024--12/2024.
```

This is cleaner as a standalone bullet.

### Fix 12: Rephrase Research Profile last sentence
Replace:
```
Seeking to apply this expertise to regional ocean circulation–biogeochemical modelling of marine ecosystem responses under climate change.
```

With:
```
Experienced in contributing to regional-scale modelling of marine ecosystem responses under present-day and projected climate change conditions.
```

This states capability rather than intent — sounds like what you ARE, not what you're looking for.

---

## Verification Checklist (run through ALL of these after editing)

1. [ ] Cover letter compiles without errors
2. [ ] Cover letter is exactly 1 page (signature + enclosures visible on page 1)
3. [ ] CV compiles without errors
4. [ ] CV is 2–3 pages (no nearly-empty final page)
5. [ ] No photo references anywhere
6. [ ] No personal data (DoB, nationality, marital status)
7. [ ] Website (thejusmahajan.github.io) is REMOVED from CV contact info
8. [ ] No bioinformatics jargon (NGS, Galaxy, Nextflow, SQL, Biopython)
9. [ ] No career-change language
10. [ ] Feb–Apr 2025 gap is filled in CV
11. [ ] Teaching has dates in CV
12. [ ] HealthTwiSt is reframed under data analysis in CV
13. [ ] Manuscript in preparation is FIRST item in Publications section
14. [ ] References have correct titles, roles, phone numbers, and institutional names
15. [ ] Elisa Schaum listed as "Postdoctoral collaborator" (NOT supervisor)
16. [ ] Kai Wirtz listed as "Guest Scientist supervisor" with "Head of Department Ecosystem Modelling"
17. [ ] Parental leave phrasing is clean in CV
18. [ ] Cover letter paragraph 4 is split and teaching is accurately described
19. [ ] All dates match the timeline in `../../reference/personal_data_and_grades.md`
20. [ ] Enclosures line present in cover letter
21. [ ] Subject line contains "ZOOM-IN" keyword

## File Operations
- Edit `cv_geomar.tex` (apply fixes 4–12)
- Edit `cover_letter_geomar.tex` (apply fixes 1–3)
- Compile both with `pdflatex` (run TWICE each for references)
- Verify page counts with `pdfinfo` or by checking the PDF
- If cover letter is not 1 page, iterate until it is
- Do NOT modify any files outside the `geomar_zoom_in/` directory
