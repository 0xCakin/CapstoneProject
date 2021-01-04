# Capstone Project

This project aims to analyze immigration events using I94 Immigration data and city temperature data. Joining these two datasets will provide us a wider range of motion to complete this task.

## Data sources

#### I94 Immigration Data
This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace. [This](https://travel.trade.gov/research/reports/i94/historical/2016.html) 

#### World Temperature Data
This dataset came from Kaggle. You can read more about it [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).

#### U.S. City Demographic Data
This data comes from OpenSoft. You can read more about it [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).


## Conceptual Data Model 

**Fact Table** - I94 immigration data joined with the city temperature data on i94port
Columns:
   - i94yr: 4 digit year,
   - i94mon: numeric month,
   - i94cit: 3 digit code of origin city,
   - i94port: 3 character code of destination USA city,
   - arrdate: arrival date in the USA,
   - i94mode: 1 digit travel code,
   - depdate: departure date from the USA,
   - i94visa: reason for immigration,
   - AverageTemperature: average temperature of destination city,

**Dimension Table** - I94 immigration data Events
Columns:
   - i94yr: 4 digit year
   - i94mon: numeric month
   - i94cit: 3 digit code of origin city
   - i94port: 3 character code of destination USA city
   - arrdate: arrival date in the USA
   - i94mode: 1 digit travel code
   - depdate: departure date from the USA
   - i94visa: reason for immigration

**Dimension Table** - temperature data
Columns:
- i94port: 3 character code of destination city (mapped from cleaned up immigration data)
- AverageTemperature: average temperature
- City: city name
- Country: country name
- Latitude: latitude
- Longitude: longitude


## Mapping Out Data Pipelines
1. Create immigration dimension tables
2. Create temperature dimension tables
3. Join tables above
4. Insert data

## Choice of tools and technologies for the project
I used Spark since it can easily handle multiple file formats (SAS, csv, etc) that contain large amounts of data. Spark SQL was used to process the input files into dataframes and manipulated via standard SQL join operations to create the tables.

## How often the data should be updated
Since the format of the raw files are monthly, we should continue pulling the data monthly.
    
## FAQ
* The data was increased by 100x.
  * Use Spark with EMR to process the data in a distributed way with high efficiency
* The data populates a dashboard that must be updated on a daily basis by 7am every day
  * Use Airflow and create a DAG to monitor the process
* The database needed to be accessed by 100+ people
  * Use Redshift. Great auto-scaling capabilities and can be accessed by many people
