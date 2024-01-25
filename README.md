# PanelSearcher

PanelSearcher is a tool which searches for the relevant gene panel for a genomic test to allow the appropriate analysis for each sample.
Each search returns the genes within the panel along with other relevant information related to the panel. From this search, a BED file 
can be created from either the whole gene transcript (MANE Select) or from the exons. Additionally, padding can be added to each side of
the entity within the BED file. Each search can be associated with a patient and added to a database, creating a record with the panel
versions.

## Project goal: A tool to manage gene panels for NHS National genomic test directory tests in the laboratory
- [x] Search for gene panels by R number 
- [x] Download gene panels as BED files
- [x] Store patient data within database

### Team Members
- Huma Z
- Sadie A
- Mathew B

Please find links to the User Guide and Installation Guide below:
## link to userguide.md :  [User Guide](/USERGUIDE.md)
## link to install.md : [Installation Guide](/INSTALL.md)

### Visit Readthedocs at: https://group1-2023-bioinfo-stp.readthedocs.io

## Marking Rubric

- Find the relevant gene panel for a genomic test to analyse sequence data from a patient appropriately
- Generate a BED file from a gene panel for genomic test analysis to use as an input to an NGS pipeline tool.
- Maintains a repository of which tests, gene panels, BED files, reference sequences and versions which have been applied to each patient case so that the laboratory has an accurate record of how analyses were performed

- [Environment setup and build](#environment-setup-and-build)
- [Software integrity and code quality](#software-integrity-and-code-quality)
- [Testing](#testing)
- [Documentation](#documentation)
- [Project management](#project-management)

#### Environment setup and build
a. Requirments.txt file is included in the repository in addition to code being stored within modules outside of the root directory. commands to install the required software are included in the [Installation Guide](/INSTALL.md)
b. A working pyproject.toml has been included. within  requirements.txt all software is version specified. (Conda has not been used)
c. A working Dockerfile has been included, instructions to run the app within a docker container are included in the [Installation Guide](/INSTALL.md)

#### Software integrity and code quality
a. 



###### License 

- MIT License

Copyright (c) 2023 Mathew-B-SDGS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
