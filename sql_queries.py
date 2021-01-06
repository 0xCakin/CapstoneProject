# DROP TABLES

immigration_table_drop = "DROP TABLE IF EXISTS immigration_main"
temperature_table_drop = "DROP TABLE IF EXISTS temperature"

# CREATE TABLES
# Immigration Table Create Statement
immigration_table_create = """
    CREATE TABLE IF NOT EXISTS immigration (
    					cicid    FLOAT,
					    year     FLOAT,
					    month    FLOAT,
					    city     FLOAT,
					    res      FLOAT,
					    iport  VARCHAR,
					    arrdate  FLOAT,
				        depdate  FLOAT,
					    visa     VARCHAR,
					    addr     VARCHAR
					    );"""
					    
# Temperature Table Create Statement
temperature_table_create = """
   				 CREATE TABLE IF NOT EXISTS temperature (
    				      AverageTemperature FLOAT,
                                      City VARCHAR,
                                      Country VARCHAR,
                                      Latitude VARCHAR,
                                      Longitude VARCHAR,
                                      iport VARCHAR); """

# INSERT RECORDS
# Immigration Table Insert Statement
immigration_table_insert = """ INSERT INTO immigration (cicid, year, month, city, res, iport, arrdate, depdate, visa, addr)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
# Temperature Table Insert Statement
temperature_table_insert = """ INSERT INTO temperature (AverageTemperature, City, Country, Latitude, Longitude, iport)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """


# QUERY LISTS
create_table_queries = [immigration_table_create, temperature_table_create]
drop_table_queries = [immigration_table_drop, temperature_table_drop]