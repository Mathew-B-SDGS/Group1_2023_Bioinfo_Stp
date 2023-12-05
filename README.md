# Group1_2023_Bioinfo_Stp

## Project goal: A tool to manage gene panels for NHS National genomic test directory tests in the laboratory

### Team Members
- Huma
- Sadie 
- Mathew 

#### Installation 
- This will work on Mac OS X or Linux operating systems 
- Required Software: Please see requirements.txt 

#### Usage 
- Run the Code from the Command line using the following command
```
python3 main.py rnumber --outputfile
```
- To Spin up the Flask App run the following command
```
flask --app app run 
```


##### Features

- Find the relevant gene panel for a genomic test to analyse sequence data from a patient appropriately
- Generate a BED file from a gene panel for genomic test analysis to use as an input to an NGS pipeline tool.
- Maintains a repository of which tests, gene panels, BED files, reference sequences and versions which have been applied to each patient case so that the laboratory has an accurate record of how analyses were performed

- Currently using Genomic Test Directory (Version 5.1, updated 1st June 2023). This will need to be updated upon release of the new version 

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
