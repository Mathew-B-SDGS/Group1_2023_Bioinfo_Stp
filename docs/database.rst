Database of panel-patient data
===================================================

## Using the Database
The database is an SQLite database, built using SQLAlchemy. The database is used to store the results of searches and link against patients.

* the Database is automatically created when the Flask app is run for the first time. and is stored in the /instance/project.db file. *

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

this Database is tested using pytest. To run the tests, run the following command from the root directory of the project:
``` pytest test/*.py ```

## Database Structure
The database is made up of 3 tables: 
- Patients
- TestCases
- TestPanels

the Database is has been normalised to 3rd normal form. through the use of foreign keys and relationships.
the Test Case Table ensures that each test case is unique, and that each test case can only be linked to one patient.
But a patient can have many test cases.