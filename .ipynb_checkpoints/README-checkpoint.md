# sqlalchemy-challenge

This assignment is divided in two(2) parts

==========================Part 1: Analyze and Explore the Climate Data===========================================

-In this section, we’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of our climate database. Specifically, we’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, we'll complete the following steps:
*Use the SQLAlchemy create_engine() function to connect to your SQLite database.
*Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
*Link Python to the database by creating a SQLAlchemy session.
-Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
-----------------------------------Precipitation Analysis-----------------------------------------------
In this subsection, we are tasked with the following:
-Find the most recent date in the dataset.
-Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
-Load the query results into a Pandas DataFrame. Explicitly set the column names.
-Sort the DataFrame values by "date".
-Plot the results by using the DataFrame plot method. 
-Use Pandas to print the summary statistics for the precipitation data.
--------------------------------------Station Analysis--------------------------------------------------------
In this subsection, we are tasked with the following:
-Design a query to calculate the total number of stations in the dataset.
-Design a query to find the most-active stations . To do so, we'll complete the following steps:
*List the stations and observation counts in descending order.
*Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
-Filter by the station that has the greatest number of observations.
-Query the previous 12 months of TOBS data for that station.
-Plot the results as a histogram with bins=12, as the following image shows:
-Close your session.

====================================Part 2: Design Your Climate App===========================================

In this section, we’ll design a Flask API based on the queries that we just developed. To do so, we'll use Flask to create our routes as follows:
-Start at the homepage.
-List all the available routes.
-Convert the query results from our precipitation analysis 
-Return the JSON representation of your dictionary.
-Return a JSON list of stations from the dataset.
-Query the dates and temperature observations of the most-active station for the previous year of data.
-Return a JSON list of temperature observations for the previous year.
-Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
-For a specified start, we'll calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
-For a specified start date and end date, we'll calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
