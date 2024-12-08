# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt

#################################################
# Database Setup
#################################################

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    return '''<h1>Welcome to the Hawaii Climate API</h1>
              <h2>Available Routes:</h2>
              <ul>
                <li>/api/v1.0/precipitation</li>
                <li>/api/v1.0/stations</li>
                <li>/api/v1.0/tobs</li>
                <li>/api/v1.0/startdate <strong>(in YYYY-MM-DD format)</strong></li>
                <li>/api/v1.0/startdate/enddate <strong>(in YYYY-MM-DD/YYYY-MM-DD format)</strong></li>
              </ul>'''

###################################################################################################################
#                                                PRECIPITATION
#
#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) 
# to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary. 
###################################################################################################################

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)

    # Calculate the date one year ago and store it to be displayed later
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prev_date = dt.date(one_year_ago.year, one_year_ago.month, one_year_ago.day)
    results = (
    session.query(Measurement.date, Measurement.prcp)
    .filter(Measurement.date >= prev_date)
    .order_by(Measurement.date.desc())
    .all()
)

    # Query the last 12 months of precipitation data
    session.close()

    # Create a dictionary from the query results and drop null values
    precipitation_dict = {date: prcp for date, prcp in results if prcp is not None}

    return jsonify(precipitation_dict)

###################################################################################################################
#                                                STATION
#
#Return a JSON list of stations from the dataset. 
###################################################################################################################

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    display = [Station.name,Station.station,]

    # Query the desired information
    results = session.query(*display).all()
    session.close()

    # Display the desired information
    stations = []
    for station,name in results:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        stations.append(station_dict)

    return jsonify(stations)

###################################################################################################################
#                                                TOBS
#
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
# 
###################################################################################################################

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    # Find the most recent date in the Measurement table
    result_tob = (
    session.query(Measurement.date, Measurement.tobs)
    .filter(Measurement.station == 'USC00519281')
    .filter(Measurement.date >= '2016-08-23')
    .all()
)

    session.close()

    # Initialize an empty list to store the temperature observation data 
    tob_list = []
    for date, tobs in result_tob:
         tobs_dictionary = {}
         tobs_dictionary["Date"] = date
         tobs_dictionary["Tobs"] = tobs
         tob_list.append(tobs_dictionary)
         
    return jsonify(tob_list)

###################################################################################################################
#                                           <start> <start>/<end>
#
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a 
# specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to 
# the end date, inclusive.
# 
###################################################################################################################

@app.route('/api/v1.0/<start>')
def start(start):
    session = Session(engine)

    # Query the minimum, average and maximum temperatures for the given start date
    results = session.query(
        func.min(Measurement.tobs).label('TMIN'),
        func.avg(Measurement.tobs).label('TAVG'),
        func.max(Measurement.tobs).label('TMAX')
    ).filter(Measurement.date >= start).all()

    session.close()

    # Create a dictionary with temperature data
    temp_data = {
        'TMIN': results[0].TMIN,
        'TAVG': results[0].TAVG,
        'TMAX': results[0].TMAX
    }

    response_data = {
        'message': f"Minimum, Average and Maximum Temperature of: {start}",
        'data': temp_data
    }

    return jsonify(response_data)

@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):
    session = Session(engine)

    # Query the temperature data for a start-end range
    results = session.query(
        func.min(Measurement.tobs).label('TMIN'),
        func.avg(Measurement.tobs).label('TAVG'),
        func.max(Measurement.tobs).label('TMAX')
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    temp_data = {
        'Start Date': start,
        'End Date': end,
        'TMIN': results[0].TMIN,
        'TAVG': results[0].TAVG,
        'TMAX': results[0].TMAX
    }

    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)
