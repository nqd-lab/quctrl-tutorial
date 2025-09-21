Visual elements refer to figures, tables, videos, or any other form of representing data. The rules of thumb are to: 
   * add to the Zenodo record not only the scripts that generate the visuals but also their outputs (i.e., the visuals themselves).
   * scripts should use processed data and the path to the data in them should be specified to obey the directory structure of the record.
   * use a clear, self-explanatory datafile naming convention that matches the paper (e.g., `fig-1.pdf`, etc.).  

Please, stick to the following guidelines:
   * figures
      - label scripts by `fig-#.py` (or some other appropriate extension if not python). Remember: we need to be able to run these using only the packages listed in `requirements.txt`;
      - add demo command to README showing how to run the scripts;
      - for schematic figs, upload keynote, inkscape, illustrator, tikz (i.e., tex), or whatever other file; 
      - upload add output of the scripts (e.g., pdf files of figs, etc.);
   * videos
      - label by `video-#.py` (or some other appropriate extension if not python);
      - add demo command showing how to run scripts;
      - upload add output of scripts (e.g., mp4 files of videos or png/pdf files of video frames, etc.);
      - in general, it is recommended to produce videos from iamges using `ffmpeg` since once can then select individual frames for presentation purposes when no video format is avaialble. 
   * tables
      - provide data used to create tables with numerical values in the paper;
      - you can read in the table data in latex (see src_latex below) and create the table in latex;