# Taming quantum systems: A tutorial for using shortcuts-to-adiabaticity, quantum optimal control, and reinforcement learning (arXiv:2501.16436)

This Zenodo record contains the complete data for the manuscript "Taming Quantum Systems: A Tutorial for Using Shortcuts-To-Adiabaticity, Quantum Optimal Control, and Reinforcement Learning" by Callum W. Duncan, Pablo M. Poggi, Marin Bukov, Nikolaj Thomas Zinner, and Steve Campbell. The repository provides jupyter notebooks, generated data, and publication figures necessary to reproduce the results presented in the paper.

## Citation

### Plain Text Citation
Callum W. Duncan, Pablo M. Poggi, Marin Bukov, Nikolaj Thomas Zinner, and Steve Campbell, "Taming Quantum Systems: A Tutorial for Using Shortcuts-To-Adiabaticity, Quantum Optimal Control, and Reinforcement Learning", arXiv:2501.16436.

### BibTeX Citation
```bibtex

@article{duncan2025taming,
  title = {Taming Quantum Systems: A Tutorial for Using Shortcuts-To-Adiabaticity, Quantum Optimal Control, and Reinforcement Learning},
  author={Duncan, Callum W and Poggi, Pablo M and Bukov, Marin and Zinner, Nikolaj Thomas and Campbell, Steve},
  journal = {PRX Quantum},
  publisher = {American Physical Society},
  doi = {10.1103/j8c7-v2hd},
  url = {https://link.aps.org/doi/10.1103/j8c7-v2hd}
}

```

## Links
- **arXiv**: https://doi.org/10.48550/arXiv.2501.16436
- **PRX Quantum**: https://doi.org/10.1103/j8c7-v2hd
- **GitHub Repository**: https://github.com/nqd-lab/quctrl-tutorial
- **Zenodo DOI**: https://doi.org/10.5281/zenodo.17169846



## Table of Contents
- [Installation and Setup](#installation-and-setup)
- [Directory Structure](#directory-structure)
- [Data Formats](#data-formats)
- [Figures](#figures)
- [Tables](#tables)
- [Videos](#videos)
- [License Information](#license-information)



## Installation and Setup

All required libraries and their versions are listed in `requirements.txt`. 

### Prerequisites
- Python 3.10 or higher

### Environment Setup
Create a dedicated Python environment and install all required packages:

```bash
# Create virtual environment
python -m venv .quctrl
source .quctrl/bin/activate # On Windows: quctrl\Scripts\activate

# Install all dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Directory Structure

```
quctrl-tutorial/
├── LICENSE                     # BSD 3-Clause License for source code
├── LICENSE-DATA                # CC-BY 4.0 License for data
├── README.md                   # This file - project documentation
├── requirements.txt            # Python dependencies
├── data/                       # Research data and results
│   └── raw/                   # Raw datasets organized by figure
│       ├── Fig2/              # Data for Figure 2 (eigenstate evolution)
│       ├── Fig3/              # Data for Figure 3 (STA protocols)
│       ├── Fig4a/             # Data for Figure 4a (LMG model)
│       ├── Fig4b/             # Data for Figure 4b (contour plots)
│       ├── Fig5/              # Data for Figure 5 (scaling analysis)
│       ├── Fig7a/             # Data for Figure 7a (cost function evolution)
│       ├── Fig7b/             # Data for Figure 7b (protocol optimization)
│       ├── Fig8a/             # Data for Figure 8a (quantum control)
│       ├── Fig8b/             # Data for Figure 8b (control performance)
│       ├── Fig9/              # Data for Figure 9 (entangled state generation)
│       ├── Fig12a/            # Data for Figure 12a (RL training)
│       ├── Fig13/             # Data for Figure 13 (STA protocols)
│       └── Fig14b/            # Data for Figure 14b (quantum noise effects)
├── src_code/                   # Source code and jupyter notebooks
│   ├── README.md              # Code-specific documentation
│   ├── notebooks/             # Tutorial jupyter notebooks
│   │   ├── quantum_optimal_control/    # QOC tutorial notebooks
│   │   ├── reinforcement_learning/     # RL tutorial notebooks
│   │   └── shortcuts_to_adiabaticity/  # STA tutorial notebooks
│   └── src/                   # Supporting source code
│       └── Bloch_sphere_lib/  # Bloch sphere visualization utilities
├── src_latex/                  # LaTeX source for the manuscript
│   ├── main.tex               # Main manuscript file
│   ├── references.bib         # Bibliography
│   └── sections/              # Individual manuscript sections
│       ├── I_introduction.tex             # Introduction section
│       ├── IIA_shortcuts_to_adiabaticity.tex # STA methodology section
│       ├── IIB_optimal_control.tex       # Optimal control section
│       ├── IIC_reinforcement_learning.tex # RL methodology section
│       └── III_outlook.tex               # Conclusions and outlook
└── visual_elements/            # Figures, tables, and visual content
    ├── README.md              # Visual elements documentation
    ├── figs/                  # Figure generation and outputs
    │   ├── *.py               # Python scripts for figure generation
    │   ├── *.mplstyle         # Matplotlib style files
    │   ├── *.ai               # Adobe Illustrator files
    │   ├── *.key              # Keynote presentation files
    │   ├── *.svg              # SVG vector graphics files
    │   ├── generate_all_figs.sh  # Script to generate all figures
    │   └── generated_figs/    # Output directory for generated figures
    └── videos/                # Video files
```

## Data

Data is stored under `./data/raw/`, and can be generated using the jupyter notebooks in `src_code/`. 

The data formats used are `.dat`, `.npz`, and `.txt`.

## Figures

Reproducing the figures uses raw data. The figure pdf's are stored under `./visual_elements/figs/generated_figs/`. 

```bash
# Navigate to figure directory
cd visual_elements/figs/

# Generate Figure 3
python fig3.py

# Generate all python figures
sh generate_all_figs.sh
```

### Scripts
All figures can be regenerated using Python scripts located in:

- `visual_elements/figs/fig1.svg` → Figure 1
- `visual_elements/figs/fig2.py` → Figure 2
- `visual_elements/figs/fig3.py` → Figure 3
- `visual_elements/figs/fig4a.py` → Figure 4a
- `visual_elements/figs/fig4b.py` → Figure 4b
- `visual_elements/figs/fig5.py` → Figure 5
- `visual_elements/figs/fig6.svg` → Figure 6
- `visual_elements/figs/fig7a.py` → Figure 7a
- `visual_elements/figs/fig7b.py` → Figure 7b 
- `visual_elements/figs/fig8a.py` → Figure 8a
- `visual_elements/figs/fig8b.py` → Figure 8b    
- `visual_elements/figs/fig9.py` → Figure 9  
- `visual_elements/figs/fig10.ai` → Figure 10
- `visual_elements/figs/fig11.key` → Figure 11
- `visual_elements/figs/fig12a.py` → Figure 12a 
- `visual_elements/figs/fig12b.key` → Figure 12b 
- `visual_elements/figs/fig13.py` → Figure 13
- `visual_elements/figs/fig14a.key` → Figure 14a 
- `visual_elements/figs/fig14b.py` → Figure 14b
- `visual_elements/figs/fig15.svg` → Figure 15 

## Tables

All tables can be found in the corresponding `.tex` files under `src_latex/`.


## Videos

Videos visualizing the trained RL agent are available under `visual_elements/videos` in `mp4` format. 

## License Information

This project uses multiple licenses based on content type:

### Source Code
- **License**: [BSD 3-Clause License](./LICENSE)
- **Applies to**: All files in `src_code/` directory
- **Permissions**: Commercial use, modification, distribution
- **Requirements**: License and copyright notice

### Data
- **License**: [Creative Commons Attribution 4.0 International (CC-BY 4.0)](./LICENSE-DATA)
- **Applies to**: All files in `data/` directory
- **Permissions**: Share, adapt, commercial use
- **Requirements**: Attribution to original authors


---

**Repository Version**: v1.0  
**Last Updated**: September 21, 2025  
**Zenodo DOI**: https://doi.org/10.5281/zenodo.17169846