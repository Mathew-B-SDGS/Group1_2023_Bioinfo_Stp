# Install Guide

Home Page: [README.md](/README.md)

For detailed documentation go to: https://group1-2023-bioinfo-stp.readthedocs.io/

## Table of Contents
- [clone the repository](#clone-the-repository) 
- [requirements.txt](#requirements.txt)
- [pyproject.toml](#pyproject.toml)
- [run the app](#run-the-app)
- [Docker](#docker)


##### Clone the repository 
```
git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git
```
Their are several ways to install the required software.
The easiest way is to use eithe the requirements.txt or pyproject.toml file.
This will install all the required software in a virtual environment. 

##### requirements.txt
- To install the required software using the requirements.txt file run the following commands in the terminal 
```
python -m venv myenv
source myenv/Scripts/activate
pip install -r requirements.txt
```
##### pyproject.toml
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

##### run the app
- after Dowloading the repository and installing the required software, Run the following command on the command line. 
```
flask --app app run 
```
#### Go to http://localhost:5000 to view the app

# Docker


Home Page: [README.md](/README.md)