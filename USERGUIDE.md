# User Guide 

Home page: [README.md](/README.md)

To see the documentation in readthedocs go to: https://group1-2023-bioinfo-stp.readthedocs.io/

==============================

## Using PanelSearcher
PanelSearcher is a Flask web app, comprising of a search function, database and user front end interface.
The app's front end is used to search for gene panels by R number and download gene panels as BED files, the search 
can be associated with a patient and saved in the database.

- Ensure that you have installed the required software and dependencies as outlined in the [Install Guide](/INSTALL.md)

- To spin up the Flask App run the following command on the command line. 
```
flask --app app run 
```
##### Go to http://localhost:5000 to view the app
OR check your Local app.log file for the URL to view

**Follow in app instructions to search for a panel and save the result to a database.**

## Using the Database
The database is an SQLite database, built using SQLAlchemy. The database is used to store the results of searches and link against patients.

- To View the Database from the Homepage click on the 'View Database' button
this will take you into the database section of the web app. From here you can view the complete database and inspect specific samples for more information.

- To Link a Panel with a Patient, First Search a Valid Panel R number. 
this will take you into to the panel information page, where you can download the panel as a BED file. From here you can link the panel to a patient by clicking the 'Link to Patient' button.
This will take you to a page where you can either: add a new patient or link to an existing patient.

- Create New Patient 
if the patient is new, you MUST first add the patient to the database. To do this:
fill in the form with patients Name and ID number and click 'Create Patient' button. this will submit the patient details into the database WITHOUT linking to a panel.

- Selecting an existing Patinet
Once the Patient details are in the database, you can link the patient to a panel by selecting the patient from the drop down menu, entering your scientist credentials, and clicking 'Link to Patient' button. This will link the panel to the patient and save the link in the database. Redirecting you to the panel information page. where you can confirm the link has been made.