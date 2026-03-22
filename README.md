# PLOS-BCAT — Manuscript Repository

Manuscript source files, figures, simulation data, and supporting information for the paper:

> Huang, C.-Y., & Wang, S.-W. (2026). Exploring the "Best Game No One Played" Phenomenon Using A Mixed Opinion Dynamics and Innovation Diffusion Model. *PLOS ONE*. (Manuscript ID: PONE-D-26-01398)

## Related Repository

The BCAT simulation model (Python 3 and NetLogo implementations) is hosted separately:

- **Model & Code:** [github.com/canslab1/BCAT](https://github.com/canslab1/BCAT) (MIT License)
- **Zenodo Archive:** [DOI: 10.5281/zenodo.19081523](https://doi.org/10.5281/zenodo.19081523)

## Repository Structure

```
PLOS-BCAT/
├── manuscript.tex                          # LaTeX source (PLOS ONE template v3.7)
├── manuscript.pdf                          # Compiled PDF
├── references.bib                          # BibTeX bibliography
├── plos2025.bst                            # PLOS ONE bibliography style
├── figures/                                # PNG figures (for LaTeX compilation)
│   ├── Fig1-combined.png                   #   Fig 1: Adoption threshold example
│   ├── fig2.png                            #   Fig 2: HK/RA/BCAT model comparison
│   ├── fig3.png                            #   Fig 3: Adoption threshold schematic
│   ├── fig4.png                            #   Fig 4: Python GUI screenshot
│   ├── fig5.png                            #   Fig 5: Simulation process flowchart
│   ├── Fig6-combined.png                   #   Fig 6: Identical conditions divergence
│   ├── Fig7-combined.png                   #   Fig 7: Correlation heatmaps
│   ├── Fig8-combined.png                   #   Fig 8: Sensitivity analysis plots
│   ├── Fig9-combined.png                   #   Fig 9: Feature importance bar charts
│   ├── fig10.png                           #   Fig 10: Mechanism decomposition (lattice)
│   ├── fig11.png                           #   Fig 11: Opinion dynamics only
│   ├── alg1.png                            #   Alg 1: Network construction
│   ├── alg2.png                            #   Alg 2: Pioneer agent initialization
│   └── alg3.png                            #   Alg 3: Opinion exchange & adoption
├── figures_tif/                            # TIFF figures (300 DPI, for journal upload)
│   ├── Fig1.tif ... Fig12.tif              #   Figs 1–12
│   └── Alg1.tif ... Alg3.tif              #   Algorithms 1–3
├── data/                                   # Raw simulation data
│   ├── sensitivity_analysis/               #   1,000-run batch results (4 XLSX, 4 topologies)
│   ├── mechanism_decomposition/            #   MD-A/B/C experiments (6 CSV, 30,000 runs)
│   └── finite_size_scaling/                #   N = 400–2,500 scaling results (2 CSV)
├── scripts/                                # Analysis and visualization scripts
│   ├── generate_table2_and_figs.py         #   Table 3 & Figs 7–9
│   ├── reproduce_table2_figs.py            #   Reproduction verification
│   └── finite_size_scaling.py              #   FSS analysis
├── run_mechanism_decomposition.py          # Mechanism decomposition runner
├── supporting_information/                 # Supporting Information for PLOS ONE
│   ├── upload/                             #   Ready-to-upload files
│   │   ├── S1_File.xlsx                    #     Sensitivity analysis data (100,548 obs)
│   │   ├── S2_File.csv                     #     Mechanism decomposition data (30,000 runs)
│   │   ├── S3_File.csv                     #     Finite-size scaling data
│   │   └── S4_File.zip                     #     Python analysis scripts (4 files)
│   ├── S1_File.xlsx                        #   Source copies
│   ├── S2_File.csv
│   ├── S3_File.csv
│   └── S4_File_scripts/                    #   Unzipped script sources
├── data_availability_statement.txt         # For Editorial Manager submission form
├── funding_statement.txt                   # For Editorial Manager submission form
└── competing_interests.txt                 # For Editorial Manager submission form
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
| Fig 2 | Structural comparison of HK, Deffuant RA, and BCAT opinion update |
| Fig 3 | Schematic diagram of adoption threshold model |
| Fig 4 | Python 3 BCAT simulation GUI |
| Fig 5 | Simulation process flowchart |
| Fig 6 | Two runs with identical parameters but divergent outcomes |
| Fig 7 | Correlation coefficient heatmaps (4 network topologies) |
| Fig 8 | Sensitivity analysis results (4 network topologies) |
| Fig 9 | Feature importance bar charts |
| Fig 10 | Mechanism decomposition on regular lattice (MD-A/B/C) |
| Fig 11 | Opinion dynamics only configuration |
| Fig 12 | Adoption threshold only configuration |
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

All simulation source code and raw data are publicly available:

- **Source code:** [github.com/canslab1/BCAT](https://github.com/canslab1/BCAT) (MIT License)
- **Archived copy:** [Zenodo DOI: 10.5281/zenodo.19081523](https://doi.org/10.5281/zenodo.19081523)
- **Simulation data:** `data/` directory in this repository and Supporting Information files S1–S4

## License

- **Manuscript content:** Subject to PLOS ONE publication terms
- **Simulation code:** MIT License (see [BCAT repository](https://github.com/canslab1/BCAT))
- **Data files:** Available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Authors

- **Chung-Yuan Huang** (黃崇源) — Department of Computer Science and Information Engineering, Chang Gung University, Taoyuan City, Taiwan
- **Sheng-Wen Wang** (王聖文, Corresponding author) — Department of Finance and Information, National Kaohsiung University of Science and Technology, Kaohsiung City, Taiwan
  - ✉ swwang@nkust.edu.tw
