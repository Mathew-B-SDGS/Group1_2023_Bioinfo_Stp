# User Guide 

home page: [README.md](/README.md)

For detailed documentation go to: https://group1-2023-bioinfo-stp.readthedocs.io/

## Table of Contents
- [Introduction](#introduction)
- [Search for gene panels by R number](#search-for-gene-panels-by-r-number)
- [download gene panels as BED files](#download-gene-panels-as-bed-files)
- [Store Patient Data within Database](#store-patient-data-within-database)
- [Database](#database)

==============================

## Introduction
This is a Flask Web App, Comprising of a Database and a Front End.
The Database is used to store patient data and the Front End is used to search for gene panels by R number and download gene panels as BED files.

- ensure that you have installed the required software and dependencies as outlined in the [Install Guide](/INSTALL.md)

- To Spin up the Flask App run the following command on the command line. 
```
flask --app app run 
```
##### Go to http://localhost:5000 to view the app
OR check your Local app.log file for the URL to view