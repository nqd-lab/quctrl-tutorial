# title-of-paper (arXiv:****.*****)

Each Zenodo record comes with its own README.md file. This is the first thing anyone outside of the project will see, so make sure it is clean, organized, and easy-to-follow. You will also copy this README into the _Description_ field on Zenodo (see checklist below). 

Make sure the README for the Zenodo record contains all items from the following **checklist**; use Markdown syntax:
   - short description of record (note that the abstract of the paper will be visible in the _Description_ field so focus on making it easy for readers to follow);
   - add licenses information, see below;
   - links to arXiv, publication journal, Github repo, etc.: **use the DOI rather than url** whenever possible;
   - information on how to cite paper as follows: (i) plain text, and (ii) a bibtex field ready to copy; 
   - table of contents for README to provide an overview of the record (use markdown syntax);
   - detailed description of Zenodo record (directories, main files, etc.)
      + specify data formats used; try to stick to single data format if possible;
      + describe the data we provide (e.g., comma-separated ..., etc.).
   - refer to `requirements.txt` file with package versions:
      + give simple command line instructions on how to automatically install them from the file (e.g., using pip to create a new environment, navigate to it, and install the packages from requirements file).
   - list explicitly the directories with scripts that generate and save all visuals from the paper;
   - misc: mention anything else you find particularly important to reproduce the results of the study.

-------

This project uses multiple licenses based on content type:

- **Code** (in `/src`): Licensed under the [BSD 3-Clause License](./LICENSE).  
- **Data** (in `/data`): Licensed under the [Creative Commons Attribution 4.0 International License (CC-BY 4.0)](./LICENSE-DATA).  
- **Models** (in `/models`): Licensed under the [Apache License 2.0](./LICENSE-MODELS).

Please refer to the individual license files for full terms and conditions.


