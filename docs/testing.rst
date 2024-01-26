Testing with Pytest
===================================================

To run testing of the backend code and flask app locally on the command line, navigate to the root of the repository and run::

    pytest tests/*

Continuous integration
------
Continuous integration (CI) testing allows you to continuously build and test the code to ensure the new commit doesn't introduce errors.
CI using GitHub Actions is performed when new commits are pushed to the main or staging branch of the repository, 
this automatically runs the tests. CI workflows can be seen by navigating to the actions tab within the GitHub repository of the project.

Code Test Coverage
-------

.. image:: /resources/test_code_coverage.PNG
    :alt: Code coverage

