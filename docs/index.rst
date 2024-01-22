.. Group1_2023_Bioinfo_Stp documentation master file, created by
   sphinx-quickstart on Fri Nov 10 12:17:37 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PanelSearcher's Documentation!
===================================================

.. toctree::
   :maxdepth: 2
   :caption: content

   installation
   testing
   changelog


Features
==================
PanelSearcher is a tool which searches for the relevant gene panel for a genomic test to allow the appropriate analysis for each sample.
Each search returns the genes within the panel along with other relevant information related to the panel. From this search, a BED file 
can be created from either the whole gene transcript (MANE Select) or from the exons. Additionally, padding can be added to each side of
the entity within the BED file. Each search can be associated with a patient and added to a database, creating a record with the panel
versions.

*PanelSearcher is currently using the National Genomic Test Directory Version 5.1 (updated 1st June 2023). This will need to be updated upon release of the new version*

Support
==================
Source code is available at : https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp/ 

To inform us of any bugs or to suggest changes you can raise an issue on GitHub : https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp/issues 

Please contact Mathew, Sadie or Huma (Group 1) for further support
