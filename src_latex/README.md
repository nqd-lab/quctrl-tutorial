This directory contains the latex files uploaded to the arXiv (and some extra latex files, if you have supplementary notes and you would like to add them). 

Note that:  
   * we don't upload here the .bib file because it may have entries that do not make it into the paper; instead, we provide the .bbl file (the file you use for the arXiv submission). 
   * the latex files should refer to the `visual_elements/figs/` directory to read in the figure files.

We also have a latex template on [Github](https://github.com/nqd-lab/_template-repo). 

*It is recommended to copy the relevant directory structure and naming conventions on Overleaf (e.g., `src_latex/`, `visual_elements/figs/`, etc.) when you start your project. This will save you some work with renaming the files later on.* 


Use `paper_body.tex` to write your paper. Once done, you may run one of the other files, as follows:
   * `main.tex` to produce the main text only;
   * `supp.tex` to produce the SM only (adding author names and paper title);
   * `combined.tex` to produce the combined main text + SM. Use this version for the arXiv. 
