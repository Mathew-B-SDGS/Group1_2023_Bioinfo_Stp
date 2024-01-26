Testing with Pytest
===================================================

To run testing of the backend code and flask app locally on the command line, navigate to the root of the repository and run::

    pytest tests/*

Continuous integration
------
Continuous integration (CI) testing allows you to continuously build and test the code to ensure the new commit doesn't introduce errors.
CI using GitHub Actions is performed when new commits are pushed to the main or staging branch of the repository, 
this automatically runs the tests. CI workflows can be seen by navigating to the actions tab within the GitHub repository of the project.

this CI testing is instead of Jenkins. the reports can be Viewed as Artifacts on GitHub Actions.
Code Test Coverage
-------

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
