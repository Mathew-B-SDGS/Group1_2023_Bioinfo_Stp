Installation
===================================================
- Clone the repository using the following command
```
git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git

```
- There are several ways to install the required software. The easiest way is to use the requirements.txt file. This will install all the required software in a virtual environment.

- To install the required software using the requirements.txt file, run the following commands in the terminal

```
python -m venv myenv
source myenv/Scripts/activate
pip install -r requirements.txt

```
- To use pyproject.toml, run the following commands in the terminal. this will install a .egg-info file in the repository. (the little "." at the end of the command is important)
```
python -m venv myenv
source myenv/Scripts/activate
pip install .

```
- This will work on Mac OS X or Linux operating systems
- Required Software: Please see requirements.txt

- Usage: To Spin up the Flask App run the following command
```
flask --app app run 

```
- Go to http://localhost:5000 to view the app

- Running in Docker : Please refer to DOCKER.md