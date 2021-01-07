# Temperature and US Immigration Data ETL Pipeline
### Data Engineering Capstone Project

#### Project Summary
This project aims to analyze immigration events using I94 Immigration data and city temperature data. Joining these two datasets will provide us a wider range of motion to complete this task.

## Data sources

### I94 Immigration Data
This data comes from the US National Tourism and Trade Office [here](https://travel.trade.gov/research/reports/i94/historical/2016.html).

### World Temperature Data
This dataset came from Kaggle [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).

### U.S. City Demographic Data
This data comes from OpenSoft [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).

## Data cleaning

* Filter temperature data to only use US data.
* Remove irregular ports from I94 data.
* Drop rows with missing IATA codes from I94 data. We need the IATA codes to join the data with other sources.


#### Conceptual Data Model 
Immigration data contains the major information. Therefore it is better to keep it as a fact table and make foreign keys for other tables to connect immigration table.
- cicid     
- year     
- month    
- city     
- res      
- iport  
- arrdate  
- depdate  
- visa     
- addr 

The first dimension table is I94port. The columns are showed below.
- port_code --foreign key
- port_city 
- port_state 

The second dimension table will be the temperature data.
- AverageTemperature 
- City 
- Country 
- Latitude 
- Longitude 
- iport -- foreign key


#### Mapping Out Data Pipelines
As described in the step 2, data clean up should be completed first of all.
- Clean up and normalize the immigration data
- Clean up and normalize the temperature data
- Organize i94port data
- Run create_table.py file
- Join temperature data with i94port
- Insert the data into the database

### Choice of tools and technologies for the project
I used Panda library for this project which I am very comfortable with. It can easily handle multiple file formats (SAS, csv, etc) that contain large amounts of data. It is also easy to manipulate the data and very efficient. However it would be better to use Spark later to on to be able to utilize Amazon Web Services and Apache Airflow. Amazon Services will help (Redshift, EMR) to distribute the data very efficiently and Airflow will be useful for schedeling the process.

### How often the data should be updated
Since the format of the raw files are monthly, we should continue pulling the data monthly.
    
### FAQ
- The data was increased by 100x.
- - Use Spark with EMR to process the data in a distributed way with high efficiency
- The data populates a dashboard that must be updated on a daily basis by 7am every day
- - Use Airflow and create a DAG to monitor the process
- The database needed to be accessed by 100+ people
- - Use Redshift. Great auto-scaling capabilities and can be accessed by many people
