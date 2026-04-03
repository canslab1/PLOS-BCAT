# PLOS-BCAT Project Memory

## Project Overview
- **Paper:** "Using a mixed opinion dynamics and innovation diffusion model to explore the 'best game no one played' phenomenon"
- **Journal:** PLOS ONE
- **Manuscript ID:** PONE-D-26-01398
- **Authors:** Chung-Yuan Huang (Chang Gung University), Sheng-Wen Wang (NKUST, corresponding: swwang@nkust.edu.tw)
- **Status:** Polished manuscript integrated; ready for revised submission to PLOS ONE (as of 2026-04-03)

## Key DOIs (verified consistent across all files)
- **Zenodo:** 10.5281/zenodo.19216365 (v1.1.0)
- **protocols.io:** 10.17504/protocols.io.261geykydv47/v1
- **GitHub:** https://github.com/canslab1/BCAT (simulation code + data)
- **GitHub:** https://github.com/canslab1/PLOS-BCAT (manuscript repo)

## Repository Structure
- `manuscript.tex` — LaTeX source (PLOS ONE template v3.7), polished English integrated 2026-04-03
- `manuscript.pdf` — Compiled PDF (38 pages, 18 MB, with figures embedded)
- `references.bib` — 64 entries, all verified for PLOS ONE compliance
- `plos2025.bst` — PLOS bibliography style
- `_Response to Reviewers PONE-D-26-01398.docx` — Response to editor + 2 reviewers (15 references, all matching bib)
- `figures/` — 15 PNG files (fig1-fig12, alg1-alg3) for LaTeX preview
- `figures_tif/` — 15 TIF files (300 DPI, for journal upload), 1:1 with PNG
- `supporting_information/` — S1_File.xlsx, S2_File.csv, S3_File.csv, S4_File.zip
- `competing_interests.txt` — No competing interests
- `funding_statement.txt` — No specific funding
- `data_availability_statement.txt` — GitHub + Zenodo + protocols.io + S1-S4

## Files NOT in git (on disk only, in .gitignore)
- `manuscript-backup-before-integration.tex` — backup of pre-polishing manuscript.tex
- `manuscript-REVISED.docx` — polished manuscript from proofreading service (input file)
- `manuscript-backup.tex`, `manuscript-backup.pdf` — older backups
- `manuscript-old.docx`, `manuscript-old.tex`, `manuscript-Jon.docx` — old versions
- `integrate-polished-manuscript.md` — integration workflow notes
- LaTeX build artifacts (*.aux, *.bbl, *.blg, *.log, *.out, *.fdb_latexmk, *.fls, *.synctex.gz)

## Manuscript Structure (sections in order, post-integration line numbers)
1. L220: Title (revised: "Using a mixed...model to explore...")
2. L224: Abstract
3. L228: Introduction
4. L249: Related opinion dynamics and adoption threshold models
5. L319: Simulation model specifications
6. L407: Evaluation indicators (subsection)
7. L431: Emergent properties of the combined model (subsection)
8. L438: Results
9. L442: Simulating favorable reviews with good or poor sales (subsection, title revised)
10. L470: Two simulations with identical initial conditions (subsection)
11. L486: Sensitivity analysis (subsection)
12. L579: Mechanism decomposition (subsection)
13. L606: Downward compatibility (subsection)
14. L639: Discussion and conclusion
15. L677: Acknowledgments
16. L685: Supporting information (S1-S4 Files)

## Floats
- **Figures:** fig1-fig12 (12 figures, all referenced, 15 PNG + 15 TIF files)
- **Tables:** table1 (model comparison), table2 (parameters), table3 (statistical results)
- **Algorithms:** alg1-alg3 (all referenced)
- **Equations:** eq:eq1, eq:eq2 (cross-referenced); eq:fri, eq:gsi (labeled)

## Completed Fixes (2026-04-02)
1. `manuscript.tex` line 279: comment `% Table 3` -> `% Table 1` (matches \label{table1})
2. `manuscript.tex` line 345: comment `% Table 1` -> `% Table 2` (matches \label{table2})
3. `manuscript.tex` line 494: comment `% Table 2` -> `% Table 3` (matches \label{table3})
4. Response letter: 3x `max-opinion-distance` -> `bounded-confidence` (consistent with manuscript)
5. Response letter: `BCAT Opinion Component` -> `Proposed Model` (consistent with manuscript Table 1)
6. Response letter item 14: added 4 missing references to summary list (Deffuant 2000, Erl 2005, McPherson 2001, Stark 2008) — now lists all 10 new references

## Completed Fixes (2026-04-03, pre-integration)
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

## Polished Manuscript Integration (2026-04-03)
20. Integrated professionally polished English text from `manuscript-REVISED.docx` into `manuscript.tex`
21. Title reordered: "Using a mixed...model to explore the...phenomenon" (per polisher)
22. Subsection title updated: "Simulating favorable reviews with good or poor sales" (per polisher)
23. Two Introduction paragraphs merged (original L236+L238 into one, L244+L246 into one)
24. One emergent properties sentence deleted (original L439 last sentence, per polisher)
25. 3 minor \textit{} removed on non-parameter terms (relative consistency, critical point, and) — style change by polisher

### 4 Critical Flags handled during integration (polisher errors overridden)
- **P22 (Deffuant RA model):** Polisher reversed meaning ("Similar to Deffuant...it does not vary" — wrong). Kept ORIGINAL wording that correctly says the proposed model's threshold does NOT vary, unlike Deffuant's which DOES.
- **P35 (parameter names):** Polisher wrote avg-of-attitudes where it should be avg-of-thresholds. Kept ORIGINAL correct parameter names.
- **P3 (Abstract last 2 sentences):** Polisher's rewording was less clear ("a neutralizing effect from testimony opinion clustering"). Kept ORIGINAL clearer wording ("testimony effect neutralizes opinion clustering").
- **P31 (DOI):** Polisher's docx had old DOI 19081523. Kept CORRECT DOI 19216365.

### Integration verification results (all PASS)
- `\cite{}`: 68 commands, 97 keys — character-identical to original
- `\ref{}`: 96 commands — character-identical to original
- `$...$` math: 148 expressions — character-identical to original
- Display equations (Eq 1, 2, FRI, GSI): character-identical to original
- `\url{}`: identical
- `\label{}`: 26 labels — identical
- `\begin{}`/`\end{}`: 31/31 — identical
- DOIs: 19216365 correct, no old DOI, no PENDING
- All 18 figure/table/algorithm captions: character-identical
- All 3 table data bodies: character-identical
- PDF compiles: 38 pages, no undefined references

## Final Integrity Check Results (2026-04-03, post-integration, all PASS)
- No PENDING/TODO/TBD placeholders in any file
- Citations: 64 unique keys, perfect 1:1 match between tex and bib
- DOIs: Zenodo + protocols.io consistent across manuscript.tex, README.md, data_availability_statement.txt, response letter
- GitHub URLs: all point to canslab1/BCAT for data
- Old DOI (19081523): completely removed from all files
- Figures: 15 PNG in figures/, 15 TIF in figures_tif/, all referenced in tex
- S4_File.zip: 4 scripts with correct names (table3)
- Response letter references: all 15 entries match references.bib
- Submission form files (competing interests, funding, data availability): all correct, complete, and consistent with manuscript.tex
- README.md: consistent with manuscript.tex (file structure, DOIs, authors, title)

## BCAT Companion Repo Status (as of 2026-04-03)
- Version: 1.4.1
- Zenodo DOI badge: 10.5281/zenodo.19216365 (v1.1.0)
- protocols.io badge: active (green)
- Scripts: generate_table3_and_figs.py, reproduce_table3_figs.py, run_mechanism_decomposition.py, finite_size_scaling.py
- CITATION.cff, pyproject.toml, CHANGELOG.md: all at v1.4.1
- README.md: all info consistent with PLOS-BCAT repo

## Next Steps
1. **Review the integrated PDF** — open manuscript.pdf in VS Code (LaTeX Workshop) or Preview to visually confirm the polished text reads well
2. **Generate marked-up PDF** — use `latexdiff manuscript-old.tex manuscript.tex` to create a diff PDF showing changes (required for PLOS ONE revised submission as "Revised Article with Changes Highlighted")
3. **Submit to PLOS ONE Editorial Manager:**
   - Upload: Response to Reviewers (.docx), Marked-up PDF, Clean PDF
   - Update figures_tif/ if any figures changed
   - Fill in: Data Availability Statement, Competing Interests, Funding Statement (from .txt files)
   - Supporting Information will auto-transfer unless replaced

## Notes
- `\previewtrue` is currently ON (figures included) — correct for revised submission
- Author Contributions: handled via Editorial Manager form, not in manuscript.tex
- Backup of pre-integration manuscript: `manuscript-backup-before-integration.tex`
- Integration workflow notes: `integrate-polished-manuscript.md`
