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