# PLOS-BCAT Project Memory

## Project Overview
- **Paper:** "Using a mixed opinion dynamics and innovation diffusion model to explore the 'best game no one played' phenomenon"
- **Journal:** PLOS ONE
- **Manuscript ID:** PONE-D-26-01398
- **Authors:** Chung-Yuan Huang (Chang Gung University), Sheng-Wen Wang (NKUST, corresponding: swwang@nkust.edu.tw)
- **Status:** Final Author Requirements submitted to PLOS ONE (2026-04-29), awaiting production team review and formal acceptance letter
- **Submission file:** PONE-D-26-01398_R1.pdf
- **Academic Editor:** Krzysztof Malarz, D.Sc., Ph.D., M.Sc.
- **DOI:** 10.1371/journal.pone.0349217 (assigned 2026-04-29; not yet active until publication)
- **Peer Review History:** YES (opted in to publish review materials)

## Key DOIs (verified consistent across all files)
- **Zenodo:** 10.5281/zenodo.19216365 (v1.1.0)
- **protocols.io:** 10.17504/protocols.io.261geykydv47/v1
- **GitHub:** https://github.com/canslab1/BCAT (simulation code + data)
- **GitHub:** https://github.com/canslab1/PLOS-BCAT (manuscript repo)

## Repository Structure
- `manuscript.tex` — LaTeX source (PLOS ONE template v3.7)
- `manuscript.pdf` — Compiled PDF (32 pages with `\previewfalse`; figures uploaded separately, algorithms 1-3 inline)
- `references.bib` — 64 entries, all verified for PLOS ONE compliance
- `plos2025.bst` — PLOS bibliography style
- `Response to Reviewers.docx` — Response to editor + 2 reviewers (source, 15 references matching bib)
- `Response to Reviewers.pdf` — Response letter for Editorial Manager upload
- `figures/` — 15 PNG files (fig1-fig12, alg1-alg3) for LaTeX preview
- `figures_tif/` — 15 TIF files (300 DPI, for journal upload), 1:1 with PNG
- `supporting_information/` — S1_File.xlsx, S2_File.csv, S3_File.csv, S4_File.zip
- `data_availability_statement.txt` — GitHub + Zenodo + protocols.io + S1-S4
- `check_figures_plos_compliance.py` — PLOS figure spec verification script (re-runnable)

Note: `competing_interests.txt` and `funding_statement.txt` removed 2026-04-29 — PLOS now confirms via Editorial Manager forms, separate .txt files no longer required.

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
4. 2026-04-28: Editor decision — Accepted in principle ("scientifically suitable for publication")
   - Reviewer #1 (anonymous): "All comments have been addressed", recommend acceptance; only minor presentation suggestions (no revision required, declined per editor's "no other changes" warning)
   - Reviewer #2 (Marcelo N Kuperman, public identity): "All comments have been addressed", recommend acceptance
5. 2026-04-29: Technical requirements e-mail received (Final Author Requirements production task)
   - DOI assigned: 10.1371/journal.pone.0349217
   - 6 items: CRediT/COI/funding confirmation, figures-out-of-PDF, S4_File.zip repackage, LaTeX bundle (.tex+.bib+PDF), separate .bib, NAAS figure check
   - Due May 02 11:59 PM
6. 2026-04-29: Final Author Requirements submitted via Editorial Manager
   - manuscript.tex updated: `\previewfalse` (figures excluded from PDF) + algorithms 1-3 unconditionally inline (separated from `\ifpreview` block)
   - manuscript.pdf recompiled: 32 pages, 1.37 MB (was 38 pages / 18 MB with figures embedded; algorithms 1-3 visible at p.8/10/12)
   - references.bib uploaded as independent file (no content change from R1)
   - S4_File.zip repacked: removed `__MACOSX/` and `._*` (20.2 KB → 17.8 KB)
   - Files NOT re-uploaded (unchanged from R1): S1-S3, fig1.tif-fig12.tif (12 figures already on PLOS server)
   - Peer Review History: YES (consent to publish review materials)
   - Letter body: confirmed CRediT roles, competing interests, funding, data availability — all unchanged
7. 2026-04-29: PLOS production team — round-2 technical requirements e-mail (after first submission)
   - 2 outstanding items: S4_File.zip still could not be opened; "footnote-style" annotations under Table 3 to be removed and incorporated into text
8. 2026-04-29: Round-2 fixes submitted via Editorial Manager
   - manuscript.tex (Table 3 area, 4 surgical edits):
     * Caption extended to absorb 3 footnote-style notes (SE explanation, Parameter Importance equivalence, avg-of-thresholds conversion)
     * Removed `\textsuperscript{*}` from "Feature Importance" row label
     * Removed `\textsuperscript{\textdagger}` from "Parameter Importance" row label
     * Replaced `\footnotesize` (table density sizing) with equivalent `\fontsize{8pt}{9pt}\selectfont` to eliminate literal "footnote" string
     * Removed `\begin{flushleft}...\end{flushleft}` block containing the 3 explanatory notes
     * Title-page corresponding-author `\textsuperscript{2*}` preserved (PLOS allows for group authorship status indicators)
   - manuscript.pdf: recompiled to 32 pages / 1.34 MB
   - supporting_information/S4_File.zip: rebuilt with Python zipfile module (ZIP_DEFLATED + flat structure, no `S4_File/` wrapper, 17.7 KB). Previous `zip -X` left Unix-origin "stored" compression + wrapper directory which PLOS could not open
   - references.bib re-uploaded with LaTeX bundle (no content change)
9. 2026-04-30: PLOS production team — round-3 technical requirements e-mail (recurring S4_File.zip + footnote issues, despite round-2 fixes)
10. 2026-04-30: Multiple successive EM uploads addressing the same recurring issues:
    - Round 3: title-page corresponding-author wording revised to `\textsuperscript{*}Corresponding author. E-mail: swwang@nkust.edu.tw` (PLOS-template-compatible explicit wording with superscript asterisk)
    - Round 4: all asterisk markers removed from title page entirely (`\textsuperscript{2*}` → `\textsuperscript{2}`; corresponding-author line is now plain inline text "Corresponding author: Sheng-Wen Wang. E-mail: ..."); chosen as deliberate departure from PLOS template's asterisk convention
    - S4_File.zip rebuilt with Python zipfile module: most portable settings (flat structure, MS-DOS / NT FAT origin, all deflated, zero extra fields, PKZip 2.0 minimum, 18,107 bytes, SHA-256 starting `aa6d2f96`)
    - File-locked (chmod 444) on disk between local build and upload to prevent macOS-side re-zipping
    - 4 .py scripts uploaded individually as `S4_File-*.py` (defensive backup; byte-identical to the scripts inside S4_File.zip)
11. 2026-04-30: Discovered EM keeps duplicate file entries (2 × S4_File.zip and 2 × manuscript.pdf), with older problematic copies persisting alongside newly-uploaded corrected copies. Hypothesis: PLOS production typesetting workflow may be picking up the older obsolete copies, explaining why each round's fixes appear ineffective.
12. 2026-04-30: Authoritative file bundle e-mailed directly to plosone@plos.org (CC: swwang@nkust.edu.tw):
    - 8 attachments: manuscript.tex, manuscript.pdf, references.bib, S4_File.zip, 4 × S4_File-*.py
    - Detailed explanation of EM duplicate situation with Description-field disambiguation (date-suffixed = latest correct; no date suffix = obsolete)
    - SHA-256 hashes provided for each file for verification
    - Request: use attached files as canonical, discard obsolete EM copies
    - Total attachment size: 1.5 MB
13. 2026-05-01: PLOS production team — round-5 technical requirements e-mail (EMID:20e1fb2adec1a6fc, due May 04 11:59 PM)
    - Single outstanding item: "Algorithm are not formatted to PLOS guidelines. Algorithm image must be editable."
    - Root cause: Algorithms 1-3 were embedded as `\includegraphics{alg*.png}` raster images, not editable text
14. 2026-05-01: Round-5 fix completed locally, ready for EM upload:
    - Added `\usepackage{listings}` + custom `NetLogoStyle` language definition (bold keywords, italic gray comments, monospace) to manuscript.tex preamble
    - Replaced all three `\includegraphics{alg[123].png}` calls with `\begin{lstlisting}...\end{lstlisting}` blocks containing the actual NetLogo-style pseudo-code as fully editable text
    - Algorithm 3 uses smaller per-listing font (`\fontsize{6.2pt}{7.2pt}`) to keep the long opinion-exchange + adoption-decision-making block on a single page
    - Updated stale preamble comment about algorithm rendering ("alg*.png inline because not separately uploaded" → "Algorithms 1-3 are typeset directly as editable LaTeX listings")
    - manuscript.pdf recompiled: 32 pages, 422 KB (same page count as round 4); algorithms now appear at p.8/10/12 as before
    - Cross-references to `Algorithm~\ref{alg1/2/3}` throughout the body remain valid (labels preserved inside algorithm float environments)
    - alg1.tif / alg2.tif / alg3.tif under `figures_tif/` are no longer referenced by the manuscript and can be removed from the EM submission queue when production picks up the new files
    - Local backup: `manuscript-backup-before-alg-conversion.tex` (in .gitignore)
15. 2026-05-01: Round-5 Final Author Requirements submitted via Editorial Manager (3 files: manuscript.tex / manuscript.pdf / references.bib)
    - SHA-256 (manuscript.tex): 3b4190003c4c99858c475036c1826712ad50791db9192b19fc74a026fc27ef8f
    - SHA-256 (manuscript.pdf): a8b1ab9efb2be86d14a4a8af5f304367327cd67606601434abb632020d035e61
    - SHA-256 (references.bib): 7bf1577985f47bec835885f3c8c613cd33188f077e2d31900e41971a5666253d
    - Letter Body explicitly notes the 3 alg*.tif files are now obsolete
16. 2026-05-01: Defensive backup e-mail sent to plosone@plos.org (CC: swwang@nkust.edu.tw)
    - Same 3 files attached, with SHA-256 hashes for typesetter verification
    - Subject prefix `Authoritative file bundle for PONE-D-26-01398R1 — round-5 FAR (algorithm editability fix) [EMID:20e1fb2adec1a6fc]`
    - Mitigates the EM duplicate-file pattern observed in rounds 2-4
17. Pending: PLOS production team response (formal acceptance letter expected)

## Figure Compliance Pre-check (2026-04-28)

Ran `check_figures_plos_compliance.py` against `figures_tif/` (15 TIF files) before next upload round.

### Core specs all PASS (15/15)
- File size: 0.20–8.35 MB (all ≤ 10 MB limit)
- DPI: 300 (all)
- Color mode: RGB (all)
- Bit depth: 8/channel (all)
- Compression: LZW (all)
- Frames: 1 (all flattened)

### Pixel dimension exceedances (12/15) vs PLOS spec (≤ 2250 px wide, ≤ 2625 px tall)
| File | Actual px | At 300 DPI | Issue |
|------|-----------|------------|-------|
| fig1 | 3810 × 614 | 12.70 × 2.05 in | width 1.69× |
| fig2/4/5/11/12 | 2784 × 2580 | 9.28 × 8.60 in | width 1.24× |
| fig3 | 1498 × 3545 | 4.99 × 11.82 in | height 1.35× |
| fig6 | 2784 × 5245 | 9.28 × 17.48 in | width 1.24×, **height 2.00×** |
| fig7 | 4094 × 3188 | 13.65 × 10.63 in | width 1.82×, height 1.21× |
| fig8 | 3567 × 5965 | 11.89 × 19.88 in | width 1.59×, **height 2.27×** |
| fig9 | 3567 × 5965 | 11.89 × 19.88 in | width 1.59×, **height 2.27×** |
| fig10 | 3475 × 1524 | 11.58 × 5.08 in | width 1.54× |

PASS without issue: alg1.tif, alg2.tif, alg3.tif

### Context: these passed PLOS twice already
- R0 upload (2026-01-09) accepted, R1 upload (2026-04-06) accepted, editor "accepted in principle" 2026-04-28
- PACE tool likely warned but did not block; production team will do final check at technical requirements stage

### Decision: defer until technical requirements e-mail
- If e-mail flags fig6 / fig8 / fig9 (most likely targets due to height 2.0–2.3× over): need to **re-generate** rather than naive resize (multi-panel figures, text legibility would suffer)
- If e-mail does not flag dimensions: leave as-is (production handles scaling)
- Pre-prepared resize plan: see compliance script output and the table above
- Rerun anytime: `python3 check_figures_plos_compliance.py`
