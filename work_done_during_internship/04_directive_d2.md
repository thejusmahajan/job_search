# Directive 2 (D2): Code Refactoring — "Refactoring repetitiver Funktionalitäten"

**Goal:** Consolidate copy-pasted logic into parameterized functions.

## Phase 1 — Complication Severity Grading
- Found 21 nearly-identical code blocks implementing 7 SIR severity grades × 3 complication slots (K1, K2, K3)
- Designed `grade_complication(data, slot, grade_cols)` — a single function handling asymmetric inputs (K1: 4 input columns, K2/K3: 1 each)
- 124 lines of repetitive code → 1 function definition + 3 calls
- Discovered **Bug 1** during this analysis (complication column inconsistency — see bugs section)

## Phase 2 — Success Criteria
- Analyzed all 26 intervention types' success/failure logic
- Classified criteria into 16 simple (single-column) and 10 complex (multi-column/regex)
- Extracted the 16 simple rules into `config/success_criteria.csv`
- Built a loop to apply CSV-defined criteria automatically
- The 10 complex rules (EVAR, Karotis, Port/PICC, FK-Bergung, Schlaganfalltherapie, Aneurysma, AVM, Kopf: Tumor/Blutung, Kopf: venöse Embo, Venöse Rekanalisation) remained as code — decision boundary was expressibility in CSV format
- Discovered **Bug 2** during this analysis (Karotis operator precedence — see bugs section)

## Result
import.R reduced from 1,566 to 1,349 lines (−218 lines).

**Combined D2+D3:** 1,834 → 1,349 lines (−486, **26.5% reduction**). 8 config CSVs (257 entries total).
