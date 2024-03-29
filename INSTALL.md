# Installation and Setup

Home Page: [README.md](/README.md)

To see the documentation in readthedocs go to: https://group1-2023-bioinfo-stp.readthedocs.io/

## Local setup without Docker

This will work on Mac OS X or Linux operating systems
Required Software: Please see requirements.txt

Clone the repository using the following command:

```
   git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git
```

There are two ways to install the required software. This will install all the required software in a virtual environment.

To install the required software using the **requirements.txt file**, run the following commands in the terminal:

```
   python -m venv myenv
   source myenv/Scripts/activate
   pip install -r requirements.txt
```

To use **pyproject.toml**, run the following commands in the terminal, this will install a .egg-info file in the repository. (the little "." at the end of the command is important):

```
   python -m venv myenv
   source myenv/Scripts/activate
   pip install .
```

*Please note ```python3``` made by required within the command in place of ```python```*

Usage: After the required software has been installed, to spin up the Flask App run the following command:

  ```
      flask --app app run
  ```

* Go to http://localhost:5000 to view the app *
* OR check your Local app.log file for the URL to view
* OR check http://127.0.0.1:5000/ (local host Port 5000) to view the app * 

## Setup within a Docker container


Clone the repository using the following command:

```
    git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git
```

Build the Docker image using the Dockerfile, first ensure you are in the root level of the repository before running:

```
    docker build -t panel_flask_app .
```

Spin up the Docker image into a Docker container:

```
    docker run -p 5000:5000 panel_flask_app
```

This will start the container, go to http://localhost:5000 to view the app

## Bringing the app down

To bring the app down use ```Ctrl+C``` on the terminal where the app was set up.

## Debugging

*Please refer to app.log to help you debug if you are unable to bring up the app, or if a search brings up no results when they are expected*

Due to the Nature of a Flask app, you may be unable to use the back button on your browser. If you need to go back, please use the navigation links on the page.
This App utilises Several API calls, if you are unable to use certain functions on the app, please wait and retry. This is likely due to the API being overloaded or down.

*Please note the panel search requires an internet connection to be performed*

Please accept accept and store cookies as these are used by the application

## Testing 
### Pytest

To run testing of the backend code and flask app locally on the command line, navigate to the root of the repository and run::

```
    pytest tests/*
```

### Continuous integration

Continuous integration (CI) testing allows you to continuously build and test the code to ensure the new commit doesn't introduce errors. 
* CI is achevied using GitHub Actions and performed when new commits are pushed to the main or staging branch of the repository,* 
this automatically runs the tests. Workflows code can be viewed under [testing](./.github/workflows/ci_testing_workflow.yml) CI workflows can be seen by navigating to the actions tab within the GitHub repository of the project. This is Comparative to the CI testing completed with Jenkins. A Report is generated each time and can be viewed as an Artifacts at [https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp/actions/workflows/ci_testing_workflow.yml]

### Code Test Coverage

Name                                  Stmts   Miss  Cover
---------------------------------------------------------
app.py                                   91     42    54%
appblueprints/database_blueprint.py     101     39    61%
modules/bedmake.py                      102     25    75%
modules/parser_test_directory.py          7      0   100%
modules/settings.py                       2      0   100%
tests/__init__.py                         1      0   100%
tests/conftest.py                        67      0   100%
tests/test_bedmake.py                    31      0   100%
---------------------------------------------------------
TOTAL                                   402    106    74%

## Updating the National Genomic Test Directory

PanelSearcher is currently using the National Genomic Test Directory Version 5.1 (updated 1st June 2023). This will need to be updated upon release of the new version

To update the directory, replace the .xlxs file within the resources directory.
Then go to modules/parser_test_directory.py and update the version.


