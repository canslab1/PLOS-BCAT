# PLOS-BCAT — Manuscript Repository

Manuscript source files, figures, data, and reviewer correspondence for the paper:

> Huang, C.-Y., & Wang, S.-W. (2026). Exploring the "Best Game No One Played" Phenomenon Using A Mixed Opinion Dynamics and Innovation Diffusion Model. *PLOS ONE*. (Manuscript ID: PONE-D-26-01398)

## Related Repository

The BCAT simulation model (Python 3 and NetLogo implementations), analysis scripts, and replication data are hosted separately:

- **Model & Code:** [github.com/canslab1/BCAT](https://github.com/canslab1/BCAT)
- **Zenodo Archive:** [DOI: 10.5281/zenodo.19081523](https://doi.org/10.5281/zenodo.19081523)

## Repository Structure

```
PLOS-BCAT/
├── manuscript.tex                         # LaTeX source (PLOS ONE template)
├── manuscript.pdf                         # Compiled PDF
├── references.bib                         # BibTeX bibliography
├── plos2025.bst                           # PLOS ONE bibliography style
├── data_availability_statement.txt        # For Editorial Manager submission
├── figures/                               # PNG figures for LaTeX compilation
│   ├── fig2.png ... fig5.png              # Simulation scenario figures
│   ├── Fig1-combined.png                  # Andy adoption threshold example
│   ├── Fig6-combined.png                  # Identical conditions divergence
│   ├── Fig7-combined.png                  # Correlation heatmaps
│   ├── Fig8-combined.png                  # Sensitivity analysis plots
│   ├── Fig9-combined.png                  # Feature importance bar charts
│   ├── fig10.png, fig11.png               # Downward compatibility
│   ├── fig_mechanism_decomposition_*.png  # MD-A/B/C results (Fig 12)
│   └── alg1.png, alg2.png, alg3.png      # Algorithm pseudocode
├── figures_tif/                           # TIFF figures for PLOS ONE submission
├── data/
│   ├── sensitivity_analysis/              # 1,000-run batch results (4 xlsx)
│   ├── mechanism_decomposition/           # MD-A/B/C experiments (6 CSV)
│   └── finite_size_scaling/               # N=400–2,500 scaling results
├── _Email PONE-D-26-01398.md              # Editor decision letter
├── _Referee Report PONE-D-26-01398.pdf    # Reviewer report
└── _Response to Reviewers PONE-D-26-01398.docx  # Point-by-point response
```

## Manuscript Overview

The paper proposes the BCAT (Bounded Confidence + Adoption Threshold) model, which integrates a bounded confidence opinion dynamics mechanism with an adoption threshold innovation diffusion model. Using agent-based simulations on four network topologies (regular lattice, small-world, random, scale-free), the study:

1. Demonstrates the "best game no one played" phenomenon — products with favorable reviews that fail to achieve widespread adoption
2. Identifies avg-of-thresholds as the dominant factor through sensitivity analysis across 1,000-run batch experiments
3. Decomposes the opinion–adoption gap into two channels — coordination failure (dominant) and opinion clustering (neutralized by testimony effect) — via controlled mechanism decomposition experiments (30,000 runs)
4. Compares BCAT predictions with information cascades, network externalities, and global games frameworks

## Building the PDF

```bash
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

Requires a LaTeX distribution with the PLOS ONE template packages.

## Authors

- **Chung-Yuan Huang** (黃崇源) — Department of Computer Science and Information Engineering, Chang Gung University, Taiwan
- **Sheng-Wen Wang** (Corresponding author) — Department of Finance and Information, National Kaohsiung University of Science and Technology, Taiwan
