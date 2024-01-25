# User Guide 

Home page: [README.md](/README.md)

For more detailed documentation about PanelSearcher go to: https://group1-2023-bioinfo-stp.readthedocs.io/

## Table of Contents
- [Introduction](#introduction)
- [Search for gene panels by R number](#search-for-gene-panels-by-r-number)
- [Download gene panels as BED files](#download-gene-panels-as-bed-files)
- [Store patient data within Database](#store-patient-data-within-database)
- [The patient-panel Database](#database)

==============================

## Introduction
PanelSearcher is a Flask web app, comprising of a search function, datbase and user front end interface.
The app's front end is used to search for gene panels by R number and download gene panels as BED files, the search 
can be associated with a patient and saved in the database.

- Ensure that you have installed the required software and dependencies as outlined in the [Install Guide](/INSTALL.md)

- To spin up the Flask App run the following command on the command line. 
```
flask --app app run 
```
##### Go to http://localhost:5000 to view the app
OR check your Local app.log file for the URL to view