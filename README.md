# Group1_2023_Bioinfo_Stp

Our Project is a Flask Web App, Comprising of a Database and a Front End. 
The Database is used to store patient data and the Front End is used to search for gene panels by R number and download gene panels as BED files.
this Web app can be Locally hosted and run from a local machine or it can be run in a docker container.

## Project goal: A tool to manage gene panels for NHS National genomic test directory tests in the laboratory
- [x] Search for gene panels by R number 
- [x] Download gene panels as BED files
- [x] Store Patient Data within Database

### Team Members
- Huma
- Sadie 
- Mathew 

#### Installation 
 
- Clone the repository using the following command 
```
git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git
```
Their are several ways to install the required software. The easiest way is to use the requirements.txt file. This will install all the required software in a virtual environment. other environment files are included in the repository: such as #TODO: add other enviroment files.


- To install the required software using the requirements.txt file run the following commands in the terminal 
```
python -m venv myenv
source myenv/Scripts/activate

pip install -r requirements.txt
```

- To use pyproject.toml, run the following commands in the terminal. this will install a .egg-info file in the repository.
(the little "." at the end of the command is important)
```
python -m venv myenv
source myenv/Scripts/activate

pip install .
```

- This will work on Mac OS X or Linux operating systems 
- In Some Use Cases the command "python3" must be used to create the virtual environment and run the app.

```
python3 -m venv myenv
source myenv/bin/activate
```

#### Usage
after downloading the repository and installing the required software, follow the instructions below to run the app.

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

: red_flag: warning :  Currently using Genomic Test Directory (Version 5.1, updated 1st June 2023). This will need to be updated upon release of the new version

###### Running in Docker

- Please refer to DOCKER.md 

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
