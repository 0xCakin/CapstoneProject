# DROP TABLES

immigration_table_drop = "DROP TABLE IF EXISTS immigration_main"
temperature_table_drop = "DROP TABLE IF EXISTS temperature"

# CREATE TABLES
# Immigration Table Create Statement
songplay_table_create = """
    CREATE TABLE IF NOT EXISTS immigration (
    					    cicid    FLOAT PRIMARY KEY,
					    year     FLOAT,
					    month    FLOAT,
					    city     FLOAT,
					    res      FLOAT,
					    i94port  VARCHAR(3),
					    arrdate  FLOAT,
				            depdate  FLOAT,
					    visa     FLOAT,
					    addr     VARCHAR,
					    AverageTemperature FLOAT,
					    Latitude VARCHAR,
					    Longitude VARCHAR
					    );"""
					    
# Temperature Table Create Statement
temperature_table_create = """
   				 CREATE TABLE IF NOT EXISTS temperature (
    				      AverageTemperature FLOAT,
                                      City VARCHAR,
                                      Country VARCHAR,
                                      Latitude VARCHAR,
                                      Longitude VARCHAR
                                      i94port VARCHAR(3)); """

# INSERT RECORDS
# Immigration Table Insert Statement
immigration_table_insert = """ INSERT INTO immigration (cicid, year, month, city, res, i94port, arrdate, depdate, visa, addr, AverageTemperature, LATITUDE, LONGITUDE)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
# Temperature Table Insert Statement
temperature_table_insert = """ INSERT INTO users (AverageTemperature, City, Country, Latitude, Longitude, i94port)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """


# QUERY LISTS
create_table_queries = [songplay_table_create, temperature_table_create]
drop_table_queries = [immigration_table_drop, temperature_table_drop]