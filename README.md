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

