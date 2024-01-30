# Farmfam_Prototype

# Data Preprocessing, Loading, and Visualization with Docker and Superset
This repository provides a Docker container and docker-compose.yaml file that can be used to preprocess, load, and visualize data using Python, Superset, and MySQL.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Advantages](#advantages)
- [Customization](#customization)

## Overview
The data pipeline consists of three main components:

-  **Data Preprocessing (Data_Proprocessing.py):** This script reads the input file, extracts the relevant data, performs data preprocessing steps, and generates a new file containing the preprocessed data.

- **Database Loading (DB_conn.py):** This script establishes a connection to the MySQL database, loads the preprocessed data into the database, and performs data validation.

- **Visualization Creation (Superset):** Superset is a data visualization tool that allows you to create charts, graphs, and dashboards from your MySQL database. Once the data is loaded into the database, you can access Superset and create visualizations using its intuitive interface.

## Prerequisites

Make sure you have the following software installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**
   git clone https://github.com/Vijayaadhithan/Farmfam_Prototype.git
   cd Farmfam_Prototype
2. **Build the Docker Images:**
   docker-compose build
3. **Start the Containers:**
   docker-compose up -d
4. **Access Superset:** Open a web browser and go to http://localhost:8080. Use the following credentials to log in:
      - Username: admin
      - Password: admin
5. **Create a Database or Connect to the existing Database:** Create a database in Superset that corresponds to the data you want to visualize or Configure Superset by creating a new                                                                 database connection to your MySQL instance
6. **Create a Table:**
   1. In the Superset interface, navigate to the "Databases" section.
   2. Click on the "+" button to create a new database connection.
   3. use this name in developement environment "host.docker.internal"
   4. Enter the database connection details for your MySQL database.
   5. Click the "Save" button to create the database connection.

7. **Create a New Table from Input Data:**
   1. In the Superset interface, navigate to the "Datasets" section.
   2. Click on the "+" button to create a new dataset.
   3. Select the "MySQL" data source.
   4. Enter the database connection details created in step 6.
   5. In the "Query" tab, enter the SQL query to select the data from the input file.
   6. Click the "Save" button to create the dataset.

8. **Create Visualizations:**
   1. In the Superset interface, navigate to the "Dashboards" section.
   2. Click on the "+" button to create a new dashboard.
   3. Drag and drop the dataset you created in step 7 onto the dashboard.
   4. Select the visualization type you want to create.
   5. Configure the visualization settings.
   6. Save the dashboard.

## Advantages
1. The entire setup is encapsulated within Docker containers, making it easy to deploy across different environments without worrying about dependencies.
2. Docker allows for easy scaling by replicating containers based on demand.
3. Ensures consistent execution across different development and deployment environments.
4. The Dockerized pipeline simplifies the process of preprocessing, loading, and visualizing data without the need for manual configuration.

## Customization
1. **Data_Proprocessing.py:** Modify the script to perform the desired data preprocessing steps.

2. **DB_conn.py:** Modify the script to connect to your MySQL database and load the preprocessed data.

3. **superset/config.py:** Modify the script to configure Superset settings, such as database connection details and secret key.
                           **Note:** To generate Secret key use this cmd:  'openssl rand -base64 32'

5. **docker-compose.yaml:** Adjust MySQL credentials, database names, and Superset configurations in the docker-compose.yaml
