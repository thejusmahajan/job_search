import os
import glob
import re

base_dir = "/scratch/local1/bioinformatics_project/job_search"

# Find all .tex files
tex_files = glob.glob(os.path.join(base_dir, "**", "*.tex"), recursive=True)

cv_files = [f for f in tex_files if not os.path.basename(f).startswith("cover_letter") and not os.path.basename(f).startswith("motivation_letter")]

new_en_sentence = r"Finalised the computational modelling framework and prepared the simulation data for peer-reviewed publication."
new_de_sentence = r"Fertigstellung des rechnergest\"utzten Modellierungs-Frameworks und Aufbereitung der Simulationsdaten f\"ur eine Peer-Review-Publikation."

new_en_item = "\\item " + new_en_sentence
new_de_item = "\\item " + new_de_sentence

new_en_item_dash = "\\item[-] " + new_en_sentence
new_de_item_dash = "\\item[-] " + new_de_sentence

for cv_file in cv_files:
    if "cv_custom.log" in cv_file or "BEWERBUNG" in cv_file:
        continue
        
    with open(cv_file, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content
    is_german = "_de.tex" in cv_file or "Lebenslauf" in content or "cv_custom.tex" in cv_file

    if "cv_geomar.tex" in cv_file:
        # cv_geomar already has this information
        pass
    elif "cv_helmholtz.tex" in cv_file:
        # We know cv_helmholtz has item[-]
        # Find: \item[-] Simulated long-term impacts of environmental changes on ecosystems.
        target = r"\item[-] Simulated long-term impacts of environmental changes on ecosystems."
        repl = target + "\n\\item[-] " + new_en_sentence
        content = content.replace(target, repl)
    else:
        # For the others, let's determine if it uses itemize or not for Guest Scientist
        # Find the Guest Scientist block
        if is_german:
            # German Baseline (no bullets):
            # Modellierung evolution\"arer Prozesse in Meeres\"okosystemen; Simulation langfristiger Umweltauswirkungen mittels fortgeschrittener Rechenmethoden.}
            target_no_bullet = r"mittels fortgeschrittener Rechenmethoden.\}"
            m = re.search(target_no_bullet, content)
            if m:
                content = content.replace(m.group(0), "mittels fortgeschrittener Rechenmethoden. " + new_de_sentence + "}")
            
            # German Application (bullets):
            # \item Anwendung fortgeschrittener Rechenmethoden zur Simulation langfristiger Umweltauswirkungen.
            # \end{itemize}}
            target_bullet = r"(\\item Anwendung fortgeschrittener Rechenmethoden zur Simulation langfristiger Umweltauswirkungen.\s*)(\\end\{itemize\}\})"
            m = re.search(target_bullet, content)
            if m:
                content = content.replace(m.group(0), m.group(1) + "    \\item " + new_de_sentence + "\n             " + m.group(2))

        else:
            # English Baseline (no bullets):
            # ... simulation of long-term environmental impacts using advanced computational methods.}
            target_no_bullet = r"advanced computational methods.\}"
            m = re.search(target_no_bullet, content)
            if m:
                content = content.replace(m.group(0), "advanced computational methods. " + new_en_sentence + "}")
            
            # English Application (bullets):
            # \item Applied advanced computational techniques to simulate long-term environmental impacts.
            # \end{itemize}}
            target_bullet = r"(\\item Applied advanced computational techniques to simulate long-term environmental impacts.\s*)(\\end\{itemize\}\})"
            m = re.search(target_bullet, content)
            if m:
                content = content.replace(m.group(0), m.group(1) + "    \\item " + new_en_sentence + "\n             " + m.group(2))

    if content != orig_content:
        with open(cv_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated:", cv_file)

print("Done")
