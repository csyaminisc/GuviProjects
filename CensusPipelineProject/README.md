# Introduction
<h3>Census Data Standardization and Analysis Pipeline Project</h3>
This project purpose is to understand data cleaning, analysis of the data and use mongodb and mysql for loading the data.
The pipeline also lays emphasis on <B>Extracting</B> the data from CSV file, <B>Transform</B> the data using Pandas and <B>Load</B> the data into MongoDb and extract from mySql for Data Visualisation.

# Tools Used in the Project
- Python
- Pandas
- MySQL
- MongoDB
- Streamlit

- Colab and Visual Code was used to develop the python code.

 Dataset used for the Project : Census_2011.xlsx
 
 Other Data File Required for the Project : Telangana.txt

# Project Flow
<B>CensusPipeLineProject.ipynb</B>

1) Read the CSV file and Perform Pandas Dataframe Operations on the Dataset. 

Pandas Data Transformation involves 
  - Renaming the Column
  - Updating Column Values
  - Finding and Filling Up the Missing Values

MongoDB Load Operations involves
  - Connecting to the MongoDB Database
  - Creating the DB & Collection
  - Inserting the Transformed Data into MongoDB Collection

mySql Load Operations involves
  - Connecting to the mySql Database
  - Reading the data from MongoDB Collection
  - Inserting the data into mySql

<B>Queries.py</B>

SQL Queries are run and visually displayed on a browser using Streamlit

#Project Guidelines

1) Install pymongo, mysql connector, streamlit before running the project
2) Update the Connection String Parameters in the CensusPipeLineProject.ipynb file and Queries.py
3) Run the Queries.py file as - streamlit run Queries.py



