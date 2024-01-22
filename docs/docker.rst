Run PanelSearcher within a Docker container
======

Clone the repository using the following command::

    git clone https://github.com/Mathew-B-SDGS/Group1_2023_Bioinfo_Stp.git

Build the Docker image using the Dockerfile, first ensure you are in the root level of the repository before running::

    docker build -t panel_flask_app .

Spin up the Docker image into a Docker container::

    docker run -p 5000:5000 panel_flask_app

This will start the container, go to http://localhost:5000 to view the app




