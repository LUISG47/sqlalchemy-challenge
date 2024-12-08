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
-List the stations and observation counts in descending order.
-Answer the following question: which station id has the greatest number of observations?
4. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.


