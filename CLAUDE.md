# PLOS-BCAT Project Memory

## Project Overview
- **Paper:** "Using a mixed opinion dynamics and innovation diffusion model to explore the 'best game no one played' phenomenon"
- **Journal:** PLOS ONE
- **Manuscript ID:** PONE-D-26-01398
- **Authors:** Chung-Yuan Huang (Chang Gung University), Sheng-Wen Wang (NKUST, corresponding: swwang@nkust.edu.tw)
- **Status:** Revised manuscript submitted to PLOS ONE (2026-04-06)
- **Submission file:** PONE-D-26-01398_R1.pdf

## Key DOIs (verified consistent across all files)
- **Zenodo:** 10.5281/zenodo.19216365 (v1.1.0)
- **protocols.io:** 10.17504/protocols.io.261geykydv47/v1
- **GitHub:** https://github.com/canslab1/BCAT (simulation code + data)
- **GitHub:** https://github.com/canslab1/PLOS-BCAT (manuscript repo)

## Repository Structure
- `manuscript.tex` — LaTeX source (PLOS ONE template v3.7)
- `manuscript.pdf` — Compiled PDF (38 pages, with figures embedded)
- `references.bib` — 64 entries, all verified for PLOS ONE compliance
- `plos2025.bst` — PLOS bibliography style
- `Response to Reviewers.docx` — Response to editor + 2 reviewers (source, 15 references matching bib)
- `Response to Reviewers.pdf` — Response letter for Editorial Manager upload
- `figures/` — 15 PNG files (fig1-fig12, alg1-alg3) for LaTeX preview
- `figures_tif/` — 15 TIF files (300 DPI, for journal upload), 1:1 with PNG
- `supporting_information/` — S1_File.xlsx, S2_File.csv, S3_File.csv, S4_File.zip
- `competing_interests.txt` — No competing interests
- `funding_statement.txt` — No specific funding
- `data_availability_statement.txt` — GitHub + Zenodo + protocols.io + S1-S4

## Files NOT in git (on disk only, in .gitignore)
- `manuscript-backup-before-integration.tex` — backup of pre-polishing manuscript.tex
- `manuscript-REVISED.docx` — polished manuscript from proofreading service
- `manuscript-old.docx`, `manuscript-old.tex` — pre-revision versions (used for latexdiff)
- `Response to Reviewers-old.docx` — pre-polishing version of response letter
- `manuscript-diff.tex`, `manuscript-diff.pdf` — latexdiff output (44 pages, regenerable)
- LaTeX build artifacts (*.aux, *.bbl, *.blg, *.log, *.out, etc.)

## Manuscript Structure (sections with line numbers)
1. L220: Title
2. L224: Abstract
3. L232: Introduction
4. L251: Related opinion dynamics and adoption threshold models
5. L319: Simulation model specifications
6. L407: Evaluation indicators (subsection)
7. L431: Emergent properties of the combined model (subsection)
8. L438: Results
9. L442: Simulating favorable reviews with good or poor sales (subsection)
10. L470: Two simulations with identical initial conditions (subsection)
11. L486: Sensitivity analysis (subsection)
12. L579: Mechanism decomposition (subsection)
13. L606: Downward compatibility (subsection)
14. L639: Discussion and conclusion
15. L677: Acknowledgments
16. L685: Supporting information (S1-S4 Files)

## Floats
- **Figures:** fig1-fig12 (12 figures, 15 PNG + 15 TIF including 3 algorithms)
- **Tables:** table1 (model comparison), table2 (parameters), table3 (statistical results)
- **Algorithms:** alg1-alg3
- **Equations:** eq:eq1, eq:eq2, eq:fri, eq:gsi

## Completed Fixes Summary (74 total, 2026-04-02 through 2026-04-06)

### Manuscript fixes (#1-67, 2026-04-02 to 2026-04-03)
- Fixes #1-6: LaTeX comment corrections, response letter terminology
- Fixes #7-19: references.bib completeness, citation keys, BCAT repo updates
- Fixes #20-25: Polished manuscript integration from `manuscript-REVISED.docx`
- Fixes #26-67: Post-integration grammar, terminology, numerical corrections, deep TEX-vs-DOCX comparison (4 rounds)
- 4 Critical Flags where polisher errors were overridden (abstract causality, Deffuant RA reversal, parameter names, DOI)

### Proofreading fixes (#68-74, 2026-04-04 to 2026-04-06)
68. L273: removed undefined BCAT acronym before definition at L321
69. L244: "affect" → "affects" (subject-verb agreement)
70. Table 1 L287: removed Table 2 parameter name from Confidence threshold cell
71. Table 1 L291: removed Table 2 parameter name from Convergence parameter cell
72. L298: removed bounded-confidence parameter formula reference
73. L298: removed convergence-rate parameter name reference
74. references.bib: replaced Watts2003 (Six Degrees) with Watts2004 (global cascades, Foundations of Social Capital)

### Note on Table 1 after fixes #70-73
- Confidence threshold and Convergence parameter rows now appear identical between HK/Deffuant and Proposed Model
- **Decision: no further changes** — Table 1 is structural comparison; implementation details in Section 3 (Table 2)
- Deffuant's μ includes RA weighting vs Proposed Model's does not — explained in L298 text

## Verification Results (2026-04-04 to 2026-04-06, all PASS)

### Section-by-section proofreading (all PASS)
| Section | Result |
|---------|--------|
| Abstract | PASS |
| 1. Introduction | PASS (1 fix: L244) |
| 2. Related models | PASS (1 fix: L273) |
| 3. Simulation model | PASS |
| 4. Results | PASS |
| 5. Discussion & conclusion | PASS |
| Acknowledgments + SI | PASS |

### Response letter verification (all PASS)
- Fixes applied: fig filename case, paragraph count, Table 1 column name, R2-5 replication detail, Valente/Erl/Watts references, FRI=0.618 small-world value
- Language, semantics, consistency with manuscript.tex: all verified
- DOIs, GitHub URLs, 15 references: all match

### Cross-file consistency (all PASS)
- manuscript.tex ↔ manuscript.pdf ↔ Response to Reviewers.pdf: 100% consistent
- No old DOI (19081523) in any file
- All Watts citations updated to 2004

## BCAT Companion Repo Status
- Version: 1.4.1
- Scripts: generate_table3_and_figs.py, reproduce_table3_figs.py, run_mechanism_decomposition.py, finite_size_scaling.py
- All info consistent with PLOS-BCAT repo

## PLOS ONE Compliance (all PASS)
- Template v3.7, plos2025.bst, unnumbered sections, Fig/Eqs format
- Title: 113 chars (limit 250), Abstract: ~295 words (limit 300)
- `\previewtrue` ON — figures embedded in PDF for revised submission

## Submission History
1. 2026-01-09: Original manuscript submitted (PONE-D-26-01398)
2. 2026-03-17: Editor decision — major revision
3. 2026-04-06: Revised manuscript submitted (PONE-D-26-01398_R1)
   - Response to Reviewers: `Response to Reviewers.pdf`
   - Revised Article with Changes Highlighted: `manuscript-diff.pdf` (44 pages)
   - Manuscript: `manuscript.pdf` (38 pages)
   - Figures: `figures_tif/*.tif` (15 files)
   - Supporting Information: S1-S4 (auto-transferred)
4. Awaiting editor/reviewer decision
