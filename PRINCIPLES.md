# Immutable Principles for Incremental Project Stewardship

*A directive for any agent — human or artificial — working on refactoring, documentation, tooling, and knowledge artifacts within a living codebase.*

---

## Preamble: Why Principles, Not Procedures

A procedure tells you what to do in a known situation. A principle tells you how to think in an unknown one. Every refactoring project encounters the unknown — a function whose side effects are invisible, a hardcoded string whose origin no one remembers, a chunk of repeated code that turns out to differ in one critical detail on line 47. Procedures break here. Principles hold.

These principles draw heavily from John Gall's *Systemantics* (later editions titled *The Systems Bible*), from the craft tradition in software (Martin Fowler, Kent Beck, the Unix philosophy), and from a philosophical stance best described as **epistemic humility before working systems**.

---

## Part I: The Foundational Axioms

### 1. The System Works. That Is Sacred.

> *"A complex system that works is invariably found to have evolved from a simple system that worked."* — Gall

The monolith runs. It produces correct output. The PI trusts it. This is not a deficiency to be overcome — it is the single most valuable property of the entire project. Every action you take must preserve this property. If you must choose between elegance and function, function wins absolutely and without exception.

**Directive:** Before any refactoring step, you must be able to answer: *How will I verify that behavior is unchanged?* If you cannot answer this, you are not ready to make the change.


### 2. You Are Not Redesigning. You Are Gardening.

> *"A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over, beginning with a working simple system."* — Gall

Refactoring is not rebuilding. You are not creating a new system. You are tending an existing one — pulling weeds (dead code), staking plants (extracting functions), labeling rows (replacing hardcoded strings with named constants). The garden's layout was chosen by someone who watched what grew. Respect that.

**Directive:** Never introduce a new architectural pattern (e.g., S4 classes, R6, a plugin system) unless the existing code is already straining toward it. Follow the energy of the existing system.


### 3. The Smallest Meaningful Change Is the Correct Unit of Work

> *"Almost anything is easier to get into than out of."* — Gall

Each commit, each file edit, each refactoring step should do exactly one thing. Extract one function. Name one constant. Deduplicate one pattern. The temptation is always to "fix everything while you're in there." Resist this completely. Large changes are unverifiable, unreviewable, and unreversible.

**Directive:** If a change cannot be described in a single sentence, it is too large. Break it down.


### 4. Reversibility Is Non-Negotiable

> *"The system always kicks back."* — Gall (Le Chatelier's Principle for Systems)

Every change must be reversible. This means version control, yes, but more fundamentally it means *structural reversibility* — your refactored code should be translatable back to the original by a reader who knows both forms. If your abstraction is so clever that the original logic is unrecoverable from reading the new code, you have created a trap, not an improvement.

**Directive:** Maintain a clear mapping between old and new. Comments, commit messages, and documentation should make the reverse path visible.

---

## Part II: The Epistemic Principles

### 5. Understand Before You Touch

> *"The system is its own best model."* — Gall

Before extracting a function, you must understand what the code does, what it depends on, and what depends on it. Before replacing a hardcoded string, you must understand *why* it was hardcoded — was it a shortcut, a deliberate choice, or a constraint from an external system? The existing code is a record of decisions. Some of those decisions are wise. You cannot tell which ones until you understand the context.

**Directive:** For every code region you intend to modify, first write a plain-language annotation of what it does and why. If you cannot write this annotation, you do not yet understand the code well enough to change it.


### 6. Names Are Theory. Choose Them as Such.

In R especially, naming is the primary act of modeling. When you extract `hospital_name` from a hardcoded `"Charité"`, you are making a theoretical claim: *this string represents a hospital name, and the logic should work for any hospital name.* This may or may not be true. The PI's logic may depend on it being exactly `"Charité"` in ways that are not syntactically visible.

**Directive:** When naming extracted constants, parameters, or functions, choose names that express the *role* the value plays in the logic, not what it happens to be. But always verify: does the logic actually treat this value generically, or does it depend on the specific value?


### 7. Repetition Is Information. Do Not Destroy It Prematurely.

Two code chunks that look identical may serve different purposes. They may have been copied because the author anticipated they would diverge. Or they may be genuinely redundant. You cannot know from syntax alone.

**Directive:** Before deduplicating repeated code, ask: *Do these repetitions share the same reason for change?* If modifying one would always require modifying the other, they are true duplicates. If they could diverge, they are *coincidentally similar*, and deduplication would create a false coupling.

---

## Part III: The Structural Principles

### 8. Single Source of Truth, Graduated Extraction

Every piece of knowledge — a configuration value, a column name, a business rule — should exist in exactly one place. But you do not achieve this in one step. The graduation is:

1. **Identify**: Comment the hardcoded value with its meaning.
2. **Name**: Assign it to a named variable at the top of its scope.
3. **Centralize**: Move it to a configuration file or constants module.
4. **Parameterize**: Make it an argument to the function that uses it.

Each step is a valid stopping point. Do not jump to step 4 when step 2 is sufficient. Over-parameterization is its own form of complexity.

**Directive:** Extract only as far as the current need requires. A named variable at the top of a script is often the right level of abstraction. Not everything needs to be in a config file.


### 9. Separation by Rate of Change, Not by Type

The traditional advice is "separate data from logic from presentation." This is incomplete. The deeper principle is: **things that change together should live together; things that change independently should live apart.**

In a reporting pipeline, the hospital name and the date range may both be "configuration," but if the hospital name is fixed for the life of the project and the date range changes quarterly, they belong in different places.

**Directive:** When deciding where something lives, ask: *How often does this change, and what changes alongside it?* Group by change-frequency and change-cause, not by syntactic category.


### 10. Directory Structure Is a Claim About the World

How you organize files is not a cosmetic choice. It is a model of the project's ontology. A directory called `R/` claims that the R source files form a coherent unit. A directory called `config/` claims that configuration is separable from logic. A directory called `utils/` is often a confession that you don't know where something belongs.

**Directive:** Every directory should have a name that answers: *What question does someone come here to answer?* If you cannot state the question, the directory is not earning its existence. Prefer flat structures with clear names over deep hierarchies with vague names.


### 11. The Filesystem Is the Primary Interface

For an agent operating on a project, the file and directory structure is not just storage — it is the primary means of orientation. An agent must be able to discover the project's shape, purpose, and current state by reading the filesystem. This means:

- A `README.md` at the root that describes the project's purpose, current state, and how to run it.
- A `CHANGELOG.md` or `DECISIONS.md` that records what has been done and why.
- Agent directive files (like this one) that encode standing instructions.
- Clear naming conventions that do not require institutional memory to decode.

**Directive:** Treat the filesystem as if it must be comprehensible to a newcomer who has no access to any conversation, email, or meeting where the project was discussed. Everything essential must be written down and findable.

---

## Part IV: The Process Principles

### 12. Test Behavior, Not Structure

The PI wants the logic unchanged. This means you need a way to verify that outputs are identical before and after each refactoring step. The correct approach is:

1. Capture the current output (the "golden output") for a set of representative inputs.
2. After each change, run the same inputs and compare.
3. Any difference is a regression until proven otherwise.

This is not unit testing in the traditional sense. You are not testing that `clean_data()` works correctly in isolation. You are testing that the entire pipeline, end to end, produces the same result.

**Directive:** Before beginning any refactoring, establish a reproducible way to generate and compare outputs. This is prerequisite infrastructure, not optional tooling.


### 13. Document the Why, Not the What

Code shows what happens. Comments and documentation should show *why* it happens. "Multiply by 1.19" is visible in the code. "The 1.19 factor is the German VAT rate as of 2024" is the documentation that matters.

**Directive:** Every extracted constant, every new function, every structural change should carry a note explaining the *reason* for its existence, not a description of what it does. The what is readable; the why is not.


### 14. Communication Artifacts Are First-Class Deliverables

Study guides, meeting preparation notes, email archives, memorization tools — these are not secondary outputs. They are how knowledge survives the departure of any single person (or agent session). They must be:

- **Findable**: stored in predictable locations with clear names.
- **Dated**: so their currency can be assessed.
- **Scoped**: each document should serve one purpose for one audience.
- **Honest**: they should state what is uncertain or incomplete.

**Directive:** Treat every knowledge artifact with the same rigor as code. It should be versioned, reviewed, and maintained. An outdated study guide is worse than no study guide.


### 15. Work in Layers, Commit at Boundaries

The order of refactoring operations matters. The correct sequence for a monolithic R codebase is:

1. **Inventory**: Map all hardcoded strings, repeated chunks, external dependencies, and side effects. Change nothing.
2. **Annotate**: Add comments explaining what each section does. Change no logic.
3. **Name**: Replace magic values with named constants within the same file. Change no structure.
4. **Extract**: Pull repeated logic into functions within the same file. Change no file boundaries.
5. **Organize**: Move functions and constants to separate files. Change no interfaces.
6. **Parameterize**: Make hardcoded values into function arguments or config entries. Change no defaults.

Each layer is a stable resting point. You can stop after any layer and the project is better than before. You should commit (in version control and conceptually) at each boundary.

**Directive:** Never skip a layer. Never combine two layers in one step. The layers exist because each one introduces a different *kind* of risk, and mixing risk types makes failures undiagnosable.

---

## Part V: The Systemic Warnings (from Gall)

### 16. Systems Develop Goals of Their Own

As you refactor, the refactored system will begin to exert its own pressures. The new config file will want more entries. The new utility functions will want their own test suite. The documentation will want a table of contents. These are not necessarily bad, but they are *emergent demands of the new structure*, not demands of the original problem. Be aware of the difference.

**Directive:** Regularly ask: *Am I serving the project's goals, or the system's goals?* If you find yourself building infrastructure to support infrastructure, stop and reassess.


### 17. The Intervention Is Part of the System

> *"The problem is not to find the answer; it's to face the answer."* — Terence McKenna (but it could be Gall)

You — the agent — are now part of the system. Your refactoring introduces new coupling (between old code and new structure), new failure modes (a config file that gets out of sync), and new cognitive load (the PI must now learn your naming conventions). Account for this. Minimize your footprint.

**Directive:** The best refactoring is the one the PI barely notices — the code does the same thing, it's just easier to read, easier to modify, and less likely to break.


### 18. Do Not Automate What You Do Not Understand

> *"If a system is working, leave it alone."* — Gall

If you encounter a code section whose purpose is unclear, do not refactor it. Annotate it with your uncertainty and move on. An opaque section that works is infinitely preferable to a "clean" section that subtly changes behavior.

**Directive:** Uncertainty is a stop signal, not a challenge to overcome. Mark it, document it, and return to it only when understanding arrives.

---

## Part VI: On the Agent's Own Conduct

### 19. Prefer Boredom Over Cleverness

The correct refactoring is almost always the boring one. Rename a variable. Extract a function. Move a block. The clever refactoring — the one that uses metaprogramming, or rewrites the loop as a functional pipeline, or introduces a new abstraction layer — is almost always wrong in the context of preserving a PI's existing logic.

**Directive:** If your change would impress a colleague, it is probably too clever. If your change would bore a colleague, it is probably correct.


### 20. Leave the Campsite Cleaner Than You Found It — But Do Not Relandscape

The Boy Scout Rule (leave code cleaner than you found it) applies, but with a boundary. Clean means: better named, better commented, less duplicated, more readable. It does not mean: reorganized, re-architected, or rewritten in a different paradigm.

**Directive:** Improve locally. Transform only with explicit mandate and verified understanding.


### 21. Every Session Ends with a Map

At the end of every work session, the agent must leave behind a record of:
- What was done.
- What was not done and why.
- What is uncertain or risky.
- What should be done next.

This record is owed to the next session — whether that session is the same agent, a different agent, or the human returning after a week away.

**Directive:** The last act of every session is to update the project's state document. This is not optional. It is the primary obligation of a steward.

---

## Epilogue: The Deepest Principle

All of the above reduces to one thing:

**Humility before the working system.**

The code works. The PI's logic is sound. The hardcoded strings were not mistakes — they were decisions made under constraints you may not fully understand. Your job is not to impose order on chaos. Your job is to make the existing order *visible*, *nameable*, and *maintainable* — without breaking it, without distorting it, and without pretending you understand it better than the person who wrote it.

This is not a lesser task than designing from scratch. It is, in many ways, a greater one.

---

*These principles are intended to be read once carefully, internalized, and then applied without re-reading. If you find yourself constantly referring back to them, you have not yet internalized them. If you find yourself violating them, stop and ask why — the answer is usually that you are trying to do too much at once.*
