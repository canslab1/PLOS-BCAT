# PLOS-BCAT Project Memory

## Project Overview
- **Paper:** "Exploring the 'Best Game No One Played' Phenomenon Using A Mixed Opinion Dynamics and Innovation Diffusion Model"
- **Journal:** PLOS ONE
- **Manuscript ID:** PONE-D-26-01398
- **Authors:** Chung-Yuan Huang (Chang Gung University), Sheng-Wen Wang (NKUST, corresponding: swwang@nkust.edu.tw)
- **Status:** Awaiting polished manuscript (.txt) from proofreading service (as of 2026-04-03)

## Key DOIs (verified consistent across all files)
- **Zenodo:** 10.5281/zenodo.19216365
- **protocols.io:** 10.17504/protocols.io.261geykydv47/v1
- **GitHub:** https://github.com/canslab1/BCAT

## Repository Structure
- `manuscript.tex` — LaTeX source (PLOS ONE template v3.7, 708 lines)
- `manuscript.pdf` — Compiled PDF (18 MB, with figures embedded)
- `references.bib` — 64 entries, perfectly synced with tex and bbl
- `plos2025.bst` — PLOS bibliography style
- `_Response to Reviewers PONE-D-26-01398.docx` — Response to editor + 2 reviewers
- `figures/` — 15 PNG files (fig1-fig12, alg1-alg3) for LaTeX preview
- `figures_tif/` — 15 TIF files (300 DPI, for journal upload), 1:1 with PNG
- `supporting_information/` — S1_File.xlsx, S2_File.csv, S3_File.csv, S4_File.zip
- `competing_interests.txt` — No competing interests
- `funding_statement.txt` — No specific funding
- `data_availability_statement.txt` — GitHub + Zenodo + protocols.io + S1-S4

## Manuscript Structure (sections in order)
1. Abstract
2. Introduction
3. Related opinion dynamics and adoption threshold models
4. Simulation model specifications
   - Evaluation indicators
   - Emergent properties of the combined model
5. Results
   - Simulating favorable reviews and good/poor sales
   - Two simulations with identical initial conditions
   - Sensitivity analysis
   - Mechanism decomposition: Coordination failure versus opinion clustering
   - Downward compatibility with opinion dynamics and adoption threshold models
6. Discussion and conclusion
7. Acknowledgments
8. Supporting information (S1-S4 Files)

## Floats
- **Figures:** fig1-fig12 (12 figures, all referenced)
- **Tables:** table1 (model comparison), table2 (parameters), table3 (statistical results)
- **Algorithms:** alg1-alg3 (all referenced)
- **Equations:** eq:eq1, eq:eq2 (cross-referenced); eq:fri, eq:gsi (labeled but inline, not cross-referenced)

## Completed Fixes (2026-04-02)
1. `manuscript.tex` line 279: comment `% Table 3` -> `% Table 1` (matches \label{table1})
2. `manuscript.tex` line 345: comment `% Table 1` -> `% Table 2` (matches \label{table2})
3. `manuscript.tex` line 494: comment `% Table 2` -> `% Table 3` (matches \label{table3})
4. Response letter: 3x `max-opinion-distance` -> `bounded-confidence` (consistent with manuscript)
5. Response letter: `BCAT Opinion Component` -> `Proposed Model` (consistent with manuscript Table 1)
6. Response letter item 14: added 4 missing references to summary list (Deffuant 2000, Erl 2005, McPherson 2001, Stark 2008) — now lists all 10 new references

## Completed Fixes (2026-04-03)
7. `references.bib`: Added DOI for Cheng2026 (10.1257/mic.20240077)
8. `references.bib`: Added URLs for Deffuant2002 and Hegselmann2002 (JASSS online articles)
9. `references.bib`: Added address for Erl2005 (Upper Saddle River, NJ) and Morris2003 (Cambridge)
10. `references.bib`: Added URL for Wilensky1999 (http://ccl.northwestern.edu/netlogo/)
11. `references.bib` + `manuscript.tex`: Renamed citation key Shuangnan2021 -> He2021 (surname convention)
12. Response letter: Fixed Valente (1996) to match bib (CMOT, not Social Networks)
13. Response letter: Fixed Watts (2004) -> Watts (2003) to match bib (Six Degrees book)
14. Response letter: Fixed Erl publisher "Prentice Hall PTR" -> "Prentice Hall" to match bib
15. Response letter: Fixed inline citations "Watts 2004/Watts, 2004" -> "Watts 2003/Watts, 2003" (paras 95, 96, 98)
16. Response letter: Fixed data URL canslab1/PLOS-BCAT -> canslab1/BCAT (para 29)
17. BCAT repo: Renamed scripts generate_table2_and_figs.py -> generate_table3_and_figs.py, reproduce_table2_figs.py -> reproduce_table3_figs.py
18. S4_File.zip: Updated with renamed scripts (table3)
19. BCAT repo: Bumped version to 1.4.1 in CITATION.cff, pyproject.toml, CHANGELOG.md

## Final Integrity Check Results (2026-04-03, all PASS)
- No PENDING/TODO/TBD placeholders in any file
- Citations: 64 keys, perfect 1:1 match between tex and bib
- DOIs: Zenodo + protocols.io consistent across manuscript.tex, README.md, data_availability_statement.txt, response letter
- GitHub URLs: all point to canslab1/BCAT for data (no PLOS-BCAT mismatch)
- Old DOI (19081523): completely removed from all files
- Figures: 15 PNG in figures/, 15 TIF in figures_tif/, all referenced in tex
- S4_File.zip: 4 scripts with correct names (table3)
- Response letter references: all 15 entries match references.bib
- Submission form files: competing interests, funding, data availability all correct and complete

## Manuscript Key Content Reference (for polished .txt integration)

### Section line numbers (manuscript.tex)
- L224: Abstract
- L232: Introduction
- L255: Related opinion dynamics and adoption threshold models
- L323: Simulation model specifications
- L411: Evaluation indicators (subsection)
- L435: Emergent properties of the combined model (subsection)
- L442: Results
- L446: Simulating favorable reviews and good/poor sales (subsection)
- L474: Two simulations with identical initial conditions (subsection)
- L490: Sensitivity analysis (subsection)
- L583: Mechanism decomposition (subsection)
- L610: Downward compatibility (subsection)
- L643: Discussion and conclusion
- L681: Acknowledgments
- L689: Supporting information (S1–S4)

### Lines containing DOIs (DO NOT modify during integration)
- L327: Zenodo DOI + protocols.io DOI + GitHub URL
- L581: Zenodo DOI (scaling data)

### LaTeX-specific content to preserve during integration
- All `\cite{...}` commands (64 unique keys, 68 occurrences)
- All `Fig~\ref{fig*}`, `Table~\ref{table*}`, `Algorithm~\ref{alg*}`
- All `\url{...}` commands
- All `$...$` math expressions (e.g., `$N = 400$`, `$\varepsilon$`)
- All `\textit{parameter-name}` (e.g., `\textit{avg-of-thresholds}`)
- Table/figure/algorithm environments (`\begin{table}` ... `\end{table}`)

### Response letter structure (paragraph numbers)
- P1: Title
- P6: Letter to Academic Editor
- P14–P33: Part I: Journal Requirements (JR-1 to JR-6)
- P34–P73: Part II: Reviewer #1 (R1-1 to R1-Minor)
- P75–P135: Part III: Reviewer #2 (R2-1 to R2-8)
- P137–P155: Part IV: Summary of All Manuscript Changes (17 items)
- P156–P171: References Cited in This Response (15 entries)

### Response letter references (15 entries, all verified against references.bib)
Banerjee 1992, Berenbrink 2024, Cheng 2026, Deffuant 2000, Deffuant 2002,
Erl 2005, Golub & Jackson 2010, Golub & Jackson 2012, Katz & Shapiro 1985,
McPherson 2001, Morris & Shin 2003, Oliver 1985, Rogers 2003,
Valente 1996 (CMOT), Watts 2003 (Six Degrees)

## Notes for Proofreading Integration
- `\previewtrue` is currently ON (figures included) — this is correct for revised submission
- Author Contributions: handled via Editorial Manager form, not in manuscript.tex
- After proofreading results arrive: integrate polished text into manuscript.tex, then recompile PDF
- See `integrate-polished-manuscript.md` for integration workflow notes
