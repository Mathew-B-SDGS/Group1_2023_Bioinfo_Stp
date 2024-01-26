Installation and set up
===================================================

Local setup without Docker
------
This will work on Mac OS X or Linux operating systems
Required Software: Please see requirements.txt

Clone the repository using the following command::

    git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git

There are several ways to install the required software. The easiest way is to use the requirements.txt file. This will install all the required software in a virtual environment.

To install the required software using the requirements.txt file, run the following commands in the terminal::

    python -m venv myenv    
    source myenv/Scripts/activate
    pip install -r requirements.txt


To use pyproject.toml, run the following commands in the terminal, this will install a .egg-info file in the repository. (the little "." at the end of the command is important)::

    python -m venv myenv
    source myenv/Scripts/activate
    pip install .


Usage: To Spin up the Flask App run the following command::

    flask --app app run 

Go to http://localhost:5000 to view the app


Setup within a Docker container
------

Clone the repository using the following command::

    git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git

Build the Docker image using the Dockerfile, first ensure you are in the root level of the repository before running::

    docker build -t panel_flask_app .

Spin up the Docker image into a Docker container::

    docker run -p 5000:5000 panel_flask_app

This will start the container, go to http://localhost:5000 to view the app

Bringing the app down
------
To bring the app down use Ctrl+C on the terminal where the app was set up.

*Please refer to app.log to help you debug if you are unable to bring up the app, or a search brings up no results when they are expected*

*Please note the panel search requires an internet connection to be performed*

Updating the National Genomic Test Directory
------

PanelSearcher is currently using the National Genomic Test Directory Version 5.1 (updated 1st June 2023). This will need to be updated upon release of the new version

To update the directory, replace the .xlxs file within the resources directory.

