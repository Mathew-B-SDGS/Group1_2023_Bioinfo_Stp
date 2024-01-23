# Group1_2023_Bioinfo_Stp

Our Project is a Flask Web App, Comprising of a Database and a Front End. 
The Database is used to store patient data and the Front End is used to search for gene panels by R number and download gene panels as BED files.
this Web app can be Locally hosted and run from a local machine or it can be run in a docker container.

## Project goal: A tool to manage gene panels for NHS National genomic test directory tests in the laboratory
- [x] Search for gene panels by R number 
- [x] Download gene panels as BED files
- [x] Store Patient Data within Database

### Team Members
- Huma Z
- Sadie A
- Mathew B

please find links to the User Guide and Install Guide below 
## link to userguide.md :  [User Guide](/USERGUIDE.md)
## link to install.md : [Install Guide](/INSTALL.md)
 

#### Usage
- To Spin up the Flask App run the following command on the command line. 
```
flask --app app run 
```
##### Go to http://localhost:5000 to view the app 
OR check your Local app.log file for the URL to view the app

### For Readthedocs go to: https://group1-2023-bioinfo-stp.readthedocs.io

##### Features

- Find the relevant gene panel for a genomic test to analyse sequence data from a patient appropriately
- Generate a BED file from a gene panel for genomic test analysis to use as an input to an NGS pipeline tool.
- Maintains a repository of which tests, gene panels, BED files, reference sequences and versions which have been applied to each patient case so that the laboratory has an accurate record of how analyses were performed

## Rubrick 
- [Environment setup and build](#environment-setup-and-build)
- [Software integrity and code quality](#software-integrity-and-code-quality)
- [Testing](#testing)
- [Documentation](#documentation)
- [Project management](#project-management)

#### Environment setup and build
a. Requirments.txt file is included in the repository in addition to code being stored within modules outside of the root directory. commands to install the required software are included in the [Install Guide](/INSTALL.md)
b. a Working pyproject.toml has been included. within  requirements.txt all software is version specified. (Conda has not been used)
c. a Working Dockerfile has been included. instructions to run the app in a docker container are included in the [Install Guide](/INSTALL.md)

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
