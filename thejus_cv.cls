\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thejus_cv}[2026/03/06 Custom CV Class]

\LoadClass[9pt, a4paper]{extarticle}

% --- Packages ---
\RequirePackage[margin=1.2cm, top=1.0cm, bottom=0.8cm]{geometry}
\RequirePackage{paracol}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{calc, shapes.geometric}
\RequirePackage{fontawesome5}
\RequirePackage{enumitem}
\RequirePackage{dashrule}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{tgheros} % TeX Gyre Heros (Helvetica clone) — standard German Bewerbung font
\renewcommand{\familydefault}{\sfdefault}
\RequirePackage{enumitem}
\setlist{nosep, leftmargin=*, topsep=0.2em, itemsep=0.2em}
% --- Colors ---
\definecolor{cvcyan}{HTML}{19B5CA} % Adjusted Cyan to match original closer
\definecolor{cvtext}{HTML}{333333} % Main text color
\definecolor{cvgray}{HTML}{7A7A7A} % Subtitle/date grey
\definecolor{cvlightgray}{HTML}{E0E0E0} % Divider lines / empty dots

% --- Global Settings ---
\color{cvtext}
\setlength{\parindent}{0pt}
\setlist[itemize]{leftmargin=*, label={\textbullet}, itemsep=0.15em, topsep=0.1em}
\columnratio{0.60} % Left column 60%, right column 40%
\setlength{\columnsep}{1.5cm}

% --- Custom Commands ---

% 1. Header
\newcommand{\cvheader}[6]{%
  % #1=Name, #2=Title, #3=Phone, #4=Email, #5=Link, #6=Location
  \begin{tikzpicture}[remember picture, overlay]
    % Background Cyan Rectangle
    \fill[cvcyan] (current page.north west) rectangle ([yshift=-4.3cm]current page.north east);
    
    % Text Content Group
    \node[anchor=north west, inner sep=0pt] at ([xshift=1.2cm, yshift=-1.0cm]current page.north west) {
      \begin{minipage}{14cm}
        \raggedright
        {\fontsize{28pt}{32pt}\selectfont\color{white}\textbf{\uppercase{#1}}}\\[0.2cm]
        {\Large\color{white}\textbf{#2}}\\[0.35cm]
        \color{white}\small
        \renewcommand{\arraystretch}{1.3}
        \begin{tabular}{@{} p{5.5cm} p{6cm} @{}}
          \faPhone\ \ #3 & \textbf{@}\ \ #4 \\
          \faLink\ \ \ #5   & \faMapMarker\ \ #6
        \end{tabular}
      \end{minipage}
    };
    
    % Profile Picture (Proper circular clipping without distortion)
    \begin{scope}
      \clip ([xshift=-3.5cm, yshift=-2.15cm]current page.north east) circle (1.75cm);
      \node[anchor=center] at ([xshift=-3.5cm, yshift=-2.15cm]current page.north east) {
        \includegraphics[width=3.6cm]{assets/img-000.jpg}
      };
    \end{scope}
    % White Border for Profile Picture
    \draw[white, line width=3pt] ([xshift=-3.5cm, yshift=-2.15cm]current page.north east) circle (1.75cm);

  \end{tikzpicture}
  \vspace*{3cm} % Force space for the header so text begins safely below it
}

% 2. Section Heading
\newcommand{\cvsection}[1]{%
  \vspace{0.8em}
  {\Large\textbf{\uppercase{#1}}}\\
  {\color{cvtext}\rule{\linewidth}{1.5pt}}\par
  \vspace{0.5em}
}

% 3. Experience Entry
\newcommand{\cvexperience}[5]{%
  % #1=Job Title, #2=Company, #3=Dates, #4=Location, #5=Bullets
  {\large\textbf{#1}}\par
  {\color{cvcyan}\textbf{#2}}\par
  {\small\color{cvgray}\faCalendar\ \ #3 \hspace{0.5cm} \faMapMarker\ \ #4}\par
  \vspace{0.2em}
  {\color{cvlightgray}\hdashrule{\linewidth}{0.5pt}{1mm}}\par
  \vspace{0.2em}
  #5
  \vspace{0.3em}
}

% 4. Sidebar Strength Item
\newcommand{\cvstrength}[3]{%
  % #1=Icon, #2=Title, #3=Text
  \begin{tabular}{@{}p{0.1\linewidth} p{0.85\linewidth}@{}}
    \raisebox{-0.2\height}{\color{cvcyan}\Large #1} & {\textbf{#2}} \\
    & {\small #3}
  \end{tabular}\par
  \vspace{0.3em}
  {\color{cvlightgray}\hdashrule{\linewidth}{0.5pt}{1mm}}\par
  \vspace{0.3em}
}

% 5. Sidebar Skills List
\newcommand{\cvskills}[2]{%
  % #1=Category, #2=List
  {\color{cvcyan}\textbf{#1}}\par
  {\small #2}\par
  \vspace{0.3em}
  {\color{cvlightgray}\hdashrule{\linewidth}{0.5pt}{1mm}}\par
  \vspace{0.3em}
}

% 6. Language Proficiency Dots
\newcommand{\cvlanguage}[3]{%
  % #1=Language, #2=Level Text, #3=Dots (out of 5)
  \begin{tabular}{@{}p{0.5\linewidth} r@{}}
    \textbf{#1} & 
    \begin{tikzpicture}[baseline=-0.5ex]
      \foreach \i in {1,...,5} {
        \ifnum\i>#3
          \fill[cvlightgray] (\i*0.35,0) circle (0.12);
        \else
          \fill[cvcyan] (\i*0.35,0) circle (0.12);
        \fi
      }
    \end{tikzpicture} \\
    {\small\color{cvgray} #2} & \\
  \end{tabular}\par
  \vspace{0.3em}
  {\color{cvlightgray}\hdashrule{\linewidth}{0.5pt}{1mm}}\par
  \vspace{0.3em}
}
