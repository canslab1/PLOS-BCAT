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

## Post-Integration Fixes (2026-04-03)
26. L236: "topics areas" -> "topic areas" (typo)
27. L583: attitude=81/distance=19 -> attitude=80/distance=20 (numerical inconsistency with avg-of-attitudes=80, std=0)
28. L659: ". and endorsements...was" -> ", and endorsements...were" (punctuation + subject-verb agreement)
29. L388: "difference...fall" -> "falls" (subject-verb agreement)
30. L484: "This finding...They" -> "These findings...They" (pronoun consistency)
31. L649: "adoption failure...They are" -> "It is" (pronoun consistency)
32. L659: "reducing...thresholds to a" -> "as part of a" (correct preposition)
33. L314, L316: "converged with" -> "converged to" (3 occurrences, polisher incorrectly changed original)
34. L649: Restored original "network clustering amplifies adoption suppression" (polisher's noun-stack was unclear)
35. L585: "bounded confidence" -> "bounded-confidence" (missing hyphen in parameter name)
36-61. 26 missed integration items from deep word-by-word comparison (mostly Discussion section)
62. L647: colon -> em dash ("fragile---a single")
63. L649: add comma before "and moderately attenuated"
64. L298: "where...corresponds" -> "with...corresponding" (participial phrase)
65. L659: add comma before "while"
66. L659: converge -> converged, remains -> remained, reach -> reached (past tense for completed experiment)
67. L669: "Fig" -> "Figs" for sub-panel reference consistency with L663

## Deep Word-by-Word Comparison (2026-04-03, multiple passes)

### Round 1: Found 26 missed integration items → all fixed
### Round 2: Found 23 total differences (including known fixes)
- 4 critical flags (TEX correct: abstract, Deffuant, parameter names, DOI)
- 2 TEX-only additions (protocols.io + Zenodo DOI sentences)
- 7 post-integration grammar fixes (already applied)
- 5 TEX semantics/grammar better (converged to, It is, network clustering, as part of, rather than on)
- 3 TEX tense correct for figure descriptions (converge/remains/reach — present tense)
- 2 adopted from DOCX (#14 fragile em dash, #17 comma before "and moderately")

### Round 3: Found 2 additional differences → fixed
- L298: "where...corresponds" → "with...corresponding" (participial phrase)
- L659: comma before "while"

### Round 4: User-requested tense change + Fig/Figs consistency
- L659: converge → converged, remains → remained, reach → reached (Palm paragraph describes completed experiment, past tense more appropriate)
- L669: "Fig~\ref{fig8}a and~\ref{fig8}b" → "Figs~\ref{fig8}a and~\ref{fig8}b" (consistency with L663's plural form)

### Final confirmed TEX-vs-DOCX differences (intentional, not to be changed)
1. Abstract last 3 sentences — TEX clearer
2. "topic areas" — DOCX has typo "topics areas"
3. "converged to" × 3 — DOCX wrong "converged with"
4. Deffuant RA model — DOCX reverses meaning
5. Parameter names — DOCX has wrong names (avg-of-attitudes)
6. "falls" — DOCX wrong "fall"
7. Zenodo DOI — DOCX has old DOI
8. protocols.io sentence — DOCX missing
9. Wilensky citation — LaTeX format difference
10. "These findings" — DOCX wrong "This finding"
11. attitude=80/distance=20 — DOCX has wrong 81/19
12. "bounded-confidence" — DOCX missing hyphen
13. Zenodo DOI in scaling — DOCX missing
14. "rather than on" — TEX parallel structure correct
15. "It is" — TEX pronoun correct
16. "network clustering amplifies adoption suppression" — TEX clearer
17. "were" — DOCX wrong "was"
18. "as part of" — TEX preposition correct
19. Fig vs Figure — PLOS convention
20. S1--S3 Files — PLOS SI naming
21. en-dash vs hyphen — LaTeX rendering convention
22. ~30 citation-stripping spacing artifacts — no actual rendering difference

## Marked-up PDF (latexdiff)
- Generated `manuscript-diff.tex` and `manuscript-diff.pdf` (40 pages)
- Command: `latexdiff --type=UNDERLINE --subtype=SAFE --disable-citation-markup manuscript-old.tex manuscript.tex`
- Preamble replaced with new manuscript preamble + minimal handcrafted DIF definitions
- New text: blue wavy underline; deleted text: red strikethrough
- BibTeX: no errors or warnings
- Figure/algorithm/table environments excluded from diff markup to prevent compilation errors

## LaTeX Syntax Check (2026-04-03, all PASS)
- Brace balance: perfectly balanced across 703 lines
- Environment pairs: all matched (document, figure×12, table×3, algorithm×3, equation×4, tabularx×3, adjustwidth×3, flushleft×2)
- Math mode: all _ ^ inside $..$ or equation environments
- Quotes: correct LaTeX quoting (`` '' and ` ')
- No \input or \externaldocument (single-file, PLOS requirement)
- No TODO/FIXME/PENDING comments

## PLOS ONE Template Compliance (2026-04-03, all PASS)
- Template: Version 3.7 Aug 2025
- Document class: \documentclass[10pt,letterpaper]{article}
- Bibliography: \bibliographystyle{plos2025}
- Figure refs: all use Fig~\ref{} (not "Figure")
- Sections: all use \section*{} (unnumbered)
- Line numbering: \linenumbers enabled, \nolinenumbers before references
- Title: 113 characters (limit 250)
- Abstract: ~295 words (limit 300)
- Supporting Information: S1-S4 File format correct
- NOTE: L183 \previewtrue — change to \previewfalse before Editorial Manager submission

## LaTeX Comments vs Content (2026-04-03, all consistent)
- 18 float marker comments (% Table 1, % Figure 1, etc.) all match their \label{}
- No TODO/FIXME/HACK/PENDING/TBD comments found

## Typo/Grammar/Variable Check (2026-04-03, all clear after fixes)
- No remaining typos or spelling errors
- All parameter names used correctly in context (no avg-of-attitudes/avg-of-thresholds confusion)
- All figure/table/algorithm references are forward references (cited before float appears)
- All citations in ascending order (Fig 1→12, Table 1→3, Alg 1→3)

## manuscript-old.tex vs manuscript-old.docx Correspondence (2026-04-03, confirmed)
- Both are the same pre-revision manuscript
- Title, abstract, all sections, 54 citations, 11 figures, 2 tables, 3 algorithms identical in content
- Minor differences: title capitalization, DOCX has "modified Barabasi", subsection numbering, keywords in DOCX only, Burbach (2020) in DOCX reference list only (uncited)

## BCAT Companion Repo Status (as of 2026-04-03)
- Version: 1.4.1
- Zenodo DOI badge: 10.5281/zenodo.19216365 (v1.1.0)
- protocols.io badge: active (green)
- Scripts: generate_table3_and_figs.py, reproduce_table3_figs.py, run_mechanism_decomposition.py, finite_size_scaling.py
- CITATION.cff, pyproject.toml, CHANGELOG.md: all at v1.4.1
- README.md: all info consistent with PLOS-BCAT repo

## Final Grammar/Syntax/Info Check (2026-04-03, all PASS)
- Grammar: no errors found
- Syntax/style: no doubled words, no missing words, parallel structure correct
- DOIs: Zenodo ×2, protocols.io ×1, GitHub ×1 — all correct
- Information: all parameters, acronyms, experimental details complete
- Minor note: L577 split infinitive "and to not be" (acceptable in modern academic English)
- Minor note: BCAT acronym used at L273 before definition at L321 (context clear)

## Next Steps
1. ~~**Review the integrated PDF**~~ — DONE
2. ~~**Generate marked-up PDF**~~ — DONE: `manuscript-diff.pdf` (40 pages)
3. **Before submission:** Change `\previewtrue` to `\previewfalse` on L183 (removes embedded figures from PDF for Editorial Manager)
4. **Submit to PLOS ONE Editorial Manager:**
   - Upload as "Response to Reviewers": `_Response to Reviewers PONE-D-26-01398.docx`
   - Upload as "Revised Article with Changes Highlighted": `manuscript-diff.pdf`
   - Upload as "Manuscript": `manuscript.pdf` (clean version)
   - Upload figures: `figures_tif/*.tif` (15 files, if any changed from original submission)
   - Fill in form fields from: `data_availability_statement.txt`, `competing_interests.txt`, `funding_statement.txt`
   - Supporting Information (S1-S4) will auto-transfer unless replaced

## Notes
- `\previewtrue` is currently ON (figures included) — correct for revised submission
- Author Contributions: handled via Editorial Manager form, not in manuscript.tex
- Backup of pre-integration manuscript: `manuscript-backup-before-integration.tex`
- Integration workflow notes: `integrate-polished-manuscript.md`
