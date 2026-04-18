# Verification Prompt: Career Work Report Audit

**Target agent:** Any capable model with file access to this repository
**Your role:** Independent fact-checker. You are verifying a set of career documents for accuracy.
**Location of documents to verify:** `docs/career/` (20 markdown files, 01–20)
**DO NOT read those files first.** Answer the questions below by examining the PRIMARY SOURCES listed for each question. Only after you have compiled your independent answers should you compare them against the career report files.

---

## RULES — Read These Before Starting

1. **Answer from primary sources ONLY.** The career files (`docs/career/*.md`) are the CLAIMS. The primary sources (code, git, config, docs) are the EVIDENCE. You are checking claims against evidence.
2. **Do NOT assume a claim is correct just because it sounds reasonable.** Verify every number, every date, every file name.
3. **Be precise with numbers.** "~360" is not the same as "357" or "363". Get the exact count where possible.
4. **Record discrepancies.** If a claim in the career file says X but your evidence says Y, record BOTH values.
5. **Do not skip checks.** Complete every single question below. Mark each as PASS, FAIL, or UNABLE TO VERIFY.
6. **Show your work.** For each answer, state the command you ran or the file/line you read. Do not just state a number — show where it came from.
7. **Be suspicious.** The author of these career files may have rounded numbers, used outdated figures, conflated different metrics, or made honest mistakes. Your job is to catch these.

---

## PHASE 1: Code-Level Verification (run commands, count lines, check files)

### Q1: Line counts
Run `wc -l` on these files and record the ACTUAL current line counts:
- `RScripts/import.R`
- `RScripts/global.R`
- `RScripts/renderReport.R`
- `RScripts/reportgenerator.Rmd`
- `RScripts/reportgenerator_yearly2024.Rmd`

**Then check:** Do the career files claim import.R is 1,348 lines? Do they claim global.R is 70 lines? Are those numbers still accurate?

### Q2: Config CSV counts
For each file in `config/`, count the number of DATA rows (excluding headers):
```bash
for f in config/*.csv; do echo "$f: $(tail -n +2 "$f" | wc -l) rows"; done
```
**Then check:** Do the career files claim 8 CSVs with 257 total entries? Count them yourself. Is it 257 or something else?

### Q3: degirtools package
- How many `.R` files are in `degirtools/R/`?
- Run `wc -l degirtools/R/*.R` — what is the total?
- How many functions are exported? Check `degirtools/NAMESPACE` and count `export()` lines.
- What version does `degirtools/DESCRIPTION` say?

**Then check:** Do the career files claim 9 functions, 859 lines, v0.1.0? Verify each number.

### Q4: Dashboard code
- Run `wc -l` on all files matching `/path/to/degir-dashboard/R/*.R` and `degir-dashboard/app.R`
- Count the total. Count the number of files.

**Then check:** Do the career files claim 1,469 lines across 10 files? Is that accurate?

### Q5: Deprecated replacement count
The career files claim 360 deprecated sites replaced across 4 files. Verify this by reading `docs/MASTER_RECALL.md` section 3 (Completed Work Log) — specifically the D4 entries. Add up the site counts from each phase:
- Phase 1 (import.R): how many?
- Phase 2 (global.R): how many?  
- Phase 3a (Rmd %<>%): how many?
- Phase 3b (Rmd gather): how many?
- Phase 3c (Rmd spread): how many?
- What is the TOTAL?

**Also check:** The MASTER_RECALL line 181 states a "Grand Total." What number does it say? Does it say 357 or 360?

### Q6: Tidymodels script
Find the tidymodels Quarto file. What is its actual line count? The career files claim 302 lines.
Check: `wc -l /scratch/local1/bioinformatics_project/internship/github_tidy_models_intro_script/intro_tidymodels.qmd`

---

## PHASE 2: Git History Verification

### Q7: Branch names
Check what branches exist on the collaborative repo references in MASTER_RECALL. The career files mention:
- `thejus/d3-config-extraction`
- `thejus/d4-d1-modernization`

Verify these branch names appear in `docs/MASTER_RECALL.md`. Search for them.

### Q8: Commit hashes
The career files reference these commit hashes. Verify each appears in `docs/MASTER_RECALL.md`:
- `e93275b` (D3 squash)
- `fdbd181` (D2 push)
- `28c8799` (D4 Rmd)
- `c5a990a` (D1 package)

### Q9: Git log
Run `git log --oneline -5` in the radioDB_on_duty repo. What is the most recent commit? Does the project appear active or stale?

---

## PHASE 3: Content Cross-Verification (read docs, compare claims)

### Q10: Bug descriptions
Read the bug descriptions in `docs/MASTER_RECALL.md` section 4 (Pitfalls & Lessons Learned). 
- Bug 1: What exactly is it? What was the resolution?
- Bug 2: What exactly is it? What was the resolution?

**Then check:** Do the career files accurately describe both bugs? Do they correctly state which was fixed and which was preserved?

### Q11: Meeting count
Count the number of meeting files in `docs/meetings/meeting_*.md`. How many formal meetings are documented?

**Then check:** Do the career files claim 5 meetings? Is that accurate?

### Q12: Complication grading
The career files describe "7 SIR severity grades × 3 complication slots (K1, K2, K3)." Verify this by:
- Reading the `grade_complication()` function in `RScripts/import.R` (search for "grade_complication")
- Count how many severity grades exist
- Count how many times the function is called (for K1, K2, K3)

### Q13: Success criteria split
The career files claim "16 simple rules in CSV + 10 complex rules in code." Verify:
- Count rows in `config/success_criteria.csv` (excluding header)
- Search import.R for "Erfolg_computed" to see how many complex rules remain in code

### Q14: Weekly emails in German
The career files claim weekly status emails were written in German. Check these files:
- `docs/meetings/email_update_2026-02-28.md`
- `docs/meetings/email_update_2026-03-06.md`

Are they actually in German? Or are they in English with German subject lines? Be precise.

### Q15: Dashboard deployment URL
The career files claim the dashboard is at `https://thejusmahajan.shinyapps.io/degir-dashboard/`. 
Check if this URL appears in `docs/MASTER_RECALL.md`. Does it match exactly?

---

## PHASE 4: Consistency Checks (compare career files against each other)

### Q16: Cross-file number consistency
Read the following numbers from multiple career files and check they all agree:
- import.R line reduction: check files 01, 03, 04, 10, 16
- D4 total sites: check files 01, 05, 16
- Config CSV count: check files 01, 03, 16
- degirtools function count: check files 01, 06, 16
- Dashboard line count: check files 01, 08, 16

If ANY of these numbers disagree between files, record the discrepancy.

### Q17: Date accuracy
The career files state the internship was "Feb 2 – Apr 15, 2026." Verify against `docs/MASTER_RECALL.md` line 7-8. Do the dates match?

### Q18: Supervisor name and title
The career files name the supervisor as "Dr. Andreas Busjahn (CEO, HealthTwiSt GmbH)." Verify against MASTER_RECALL. Is CEO mentioned, or just "supervisor"?

---

## PHASE 5: Completeness Check

### Q19: Missing topics
Scan these source files for topics that should be in the career report but might be missing:
- `docs/MASTER_RECALL.md` — any major work items NOT covered in the career files?
- `docs/FINAL_PRESENTATION_PLAN.md` — any significant presentation details missing?
- `docs/meetings/email_certificate_2026-04-13.md` — any skills listed there but NOT in the career files?

### Q20: Keyword completeness
Read 3 random job descriptions for "Bioinformatics" or "Data Engineer" or "R Developer" roles. List 5 keywords from those descriptions that you think SHOULD appear in the keyword index (`docs/career/19_keyword_index.md`) but are missing.

---

## OUTPUT FORMAT

For each question (Q1–Q20), output:

```
Q[N]: [PASS / FAIL / UNABLE TO VERIFY]
Evidence: [what you found — be specific]
Career file claim: [what the career file says]
Discrepancy: [if FAIL, describe the mismatch]
```

At the end, provide:
1. Total PASS / FAIL / UNABLE counts
2. A list of ALL discrepancies found, with corrections
3. Your confidence level (HIGH / MEDIUM / LOW) in the overall accuracy of the career report

---

*This prompt was generated on 2026-04-18. The career files are in `docs/career/` (files 01–20). The primary sources are the rest of this repository.*
