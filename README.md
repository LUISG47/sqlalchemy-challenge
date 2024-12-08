# CHALLENGUE 10 [SQL Alchemy]

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.


## Part 1: Analyze and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

The CSV that you will be using are located on the **Resources** folder, make sure to point them correctly when you create and import them.

### Precipitation Analysis

1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, the resulting image should be as follows:

![Screenshot 2024-12-08 at 11 54 53 a m](https://github.com/user-attachments/assets/bb4d77eb-0126-414c-813e-a5169b6b51ec)

7. Use Pandas to print the summary statistics for the precipitation data.
   
### Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
+ List the stations and observation counts in descending order.
+ Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
+ Filter by the station that has the greatest number of observations.
+ Query the previous 12 months of TOBS data for that station.
+ Plot the results as a histogram with bins=12, as the following image shows:

![Screenshot 2024-12-08 at 11 55 03 a m](https://github.com/user-attachments/assets/c40d2a3c-aeb5-4552-a24d-61f763f621c1)

## Part 1: Analyze and Explore the Climate Data

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows, 
We recommend using **FIREFOX** for the display of the web app

1. /
+ Start at the homepage.
+ List all the available routes.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 50 53 a m](https://github.com/user-attachments/assets/379d02de-6f7a-4ee1-8c36-ef58a060fff5)


2. /api/v1.0/precipitation
+ Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
+ Return the JSON representation of your dictionary.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 51 01 a m](https://github.com/user-attachments/assets/1bfc4a05-5e9a-4116-8891-65e317a88dae)

3. /api/v1.0/stations
+ Return a JSON list of stations from the dataset.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 51 08 a m](https://github.com/user-attachments/assets/1a6054e2-c930-42e5-9f51-0ee966cf0dc6)

4. /api/v1.0/tobs
+ Query the dates and temperature observations of the most-active station for the previous year of data.
+ Return a JSON list of temperature observations for the previous year.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 51 17 a m](https://github.com/user-attachments/assets/30b85936-f932-413d-a95b-d65fda73868b)

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
+ Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
+ For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 51 23 a m](https://github.com/user-attachments/assets/b9d67292-c3f3-42da-b976-36fe82790477)

+ For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

The result on the browser should display as follows:

![Screenshot 2024-12-08 at 11 51 31 a m](https://github.com/user-attachments/assets/e2f11733-dcb0-411e-8ba4-b077d14c908c)
































