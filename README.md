# PLOS-BCAT — Manuscript Repository

Manuscript source files, figures, and supporting information for the paper:

> Huang, C.-Y., & Wang, S.-W. (2026). Exploring the "Best Game No One Played" Phenomenon Using A Mixed Opinion Dynamics and Innovation Diffusion Model. *PLOS ONE*. (Manuscript ID: PONE-D-26-01398)

## Related Repository

The BCAT simulation model, raw simulation data, and analysis scripts are hosted separately:

- **Model, Code & Data:** [github.com/canslab1/BCAT](https://github.com/canslab1/BCAT) (MIT License)
- **Zenodo Archive:** [DOI: 10.5281/zenodo.19216365](https://doi.org/10.5281/zenodo.19216365)
- **Reproduction Protocol:** [protocols.io](https://www.protocols.io/view/reproducing-simulation-results-for-the-bcat-model-jwrwcpd7f) (DOI: 10.17504/protocols.io.261geykydv47/v1)

To reproduce the simulation results reported in this paper, please visit the [BCAT repository](https://github.com/canslab1/BCAT), which contains the complete simulation system, pre-configured parameter files, raw output data, and analysis scripts.

## Repository Structure

```
PLOS-BCAT/
├── manuscript.tex                          # LaTeX source (PLOS ONE template v3.7)
├── manuscript.pdf                          # Compiled PDF
├── references.bib                          # BibTeX bibliography
├── plos2025.bst                            # PLOS ONE bibliography style
├── figures/                                # PNG figures (for LaTeX compilation)
│   ├── Fig1-combined.png                   #   Fig 1: Adoption threshold example
│   ├── fig2.png                            #   Fig 2: Python GUI screenshot
│   ├── fig3.png                            #   Fig 3: Simulation process flowchart
│   ├── fig4.png                            #   Fig 4: Favorable review + good sales
│   ├── fig5.png                            #   Fig 5: Favorable review + poor sales
│   ├── Fig6-combined.png                   #   Fig 6: Identical conditions divergence
│   ├── Fig7-combined.png                   #   Fig 7: Correlation heatmaps
│   ├── Fig8-combined.png                   #   Fig 8: Sensitivity analysis plots
│   ├── Fig9-combined.png                   #   Fig 9: Statistical analysis bar charts
│   ├── fig10.png                           #   Fig 10: Mechanism decomposition
│   ├── fig11.png                           #   Fig 11: Opinion dynamics only
│   ├── fig12.png                           #   Fig 12: Adoption threshold only
│   ├── alg1.png                            #   Algorithm 1: Network construction
│   ├── alg2.png                            #   Algorithm 2: Pioneer initialization
│   └── alg3.png                            #   Algorithm 3: Opinion exchange & adoption
├── figures_tif/                            # TIFF figures (300 DPI, for journal upload)
│   ├── Fig1.tif ... Fig12.tif              #   Figs 1–12
│   └── Alg1.tif ... Alg3.tif              #   Algorithms 1–3
├── supporting_information/                 # Supporting Information for PLOS ONE
│   ├── S1_File.xlsx                        #   Sensitivity analysis data (100,548 obs)
│   ├── S2_File.csv                         #   Mechanism decomposition data (30,000 runs)
│   ├── S3_File.csv                         #   Finite-size scaling data
│   └── S4_File.zip                         #   Python analysis scripts (4 scripts)
├── _Response to Reviewers PONE-D-26-01398.docx  # Response to reviewers letter
├── competing_interests.txt                 # For Editorial Manager submission form
├── data_availability_statement.txt         # For Editorial Manager submission form
└── funding_statement.txt                   # For Editorial Manager submission form
```

## Manuscript Overview

The paper proposes the **BCAT (Bounded Confidence + Adoption Threshold) model**, which integrates a bounded confidence opinion dynamics mechanism with an adoption threshold innovation diffusion model. Using agent-based simulations on four network topologies (regular lattice, small-world, random, scale-free), the study:

1. Demonstrates the "best game no one played" phenomenon — products with favorable reviews that fail to achieve widespread adoption
2. Identifies **avg-of-thresholds** as the dominant factor through sensitivity analysis across 1,000-run batch experiments
3. Decomposes the opinion–adoption gap into two channels — **coordination failure** (dominant) and **opinion clustering** (neutralized by testimony effect) — via controlled mechanism decomposition experiments (30,000 runs)
4. Validates robustness through **finite-size scaling** experiments (N = 400 to 2,500)
5. Compares BCAT predictions with information cascades, network externalities, and global games frameworks

## Figures

| Figure | Description |
|--------|-------------|
| Fig 1 | Andy adoption threshold example (panels a, b) |
| Fig 2 | Python 3 BCAT simulation GUI |
| Fig 3 | Simulation process flowchart |
| Fig 4 | Favorable review and good sales scenario |
| Fig 5 | Favorable review but poor sales scenario |
| Fig 6 | Two runs with identical parameters but divergent outcomes |
| Fig 7 | Correlation coefficient heatmaps (4 network topologies) |
| Fig 8 | Sensitivity analysis results (4 network topologies) |
| Fig 9 | Statistical analysis results for primary BCAT parameters |
| Fig 10 | Mechanism decomposition on regular lattice (MD-A/B/C) |
| Fig 11 | BCAT configured as opinion dynamics model only |
| Fig 12 | BCAT configured as adoption threshold model only |
| Alg 1 | Network model construction pseudo-code |
| Alg 2 | Pioneer agent initialization pseudo-code |
| Alg 3 | Opinion exchange and adoption decision pseudo-code |

## Building the PDF

```bash
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

Requires a LaTeX distribution with the PLOS ONE template packages.

## Data Availability

All simulation source code, raw data, and analysis scripts are publicly available in the companion repository:

- **Source code & data:** [github.com/canslab1/BCAT](https://github.com/canslab1/BCAT) (MIT License)
- **Archived copy:** [Zenodo DOI: 10.5281/zenodo.19216365](https://doi.org/10.5281/zenodo.19216365)
- **Reproduction Protocol:** [protocols.io](https://www.protocols.io/view/reproducing-simulation-results-for-the-bcat-model-jwrwcpd7f) (DOI: 10.17504/protocols.io.261geykydv47/v1)

## License

- **Manuscript content:** Subject to PLOS ONE publication terms
- **Simulation code:** MIT License (see [BCAT repository](https://github.com/canslab1/BCAT))
- **Data files:** Available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Authors

- **Chung-Yuan Huang** — Department of Computer Science and Information Engineering, Chang Gung University, Taoyuan City, Taiwan
- **Sheng-Wen Wang** (Corresponding author) — Department of Finance and Information, National Kaohsiung University of Science and Technology, Kaohsiung City, Taiwan
  - swwang@nkust.edu.tw
