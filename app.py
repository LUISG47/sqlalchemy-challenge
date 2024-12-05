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
                <li>/api/v1.0/&lt;start&gt;</li>
                <li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>
              </ul>'''

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)


    # Calculate the date one year ago
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    session.close()

    # Create a dictionary from the query results
    precipitation_dict = {date: prcp for date, prcp in results}

    return jsonify(precipitation_dict)


@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Create a list of stations
    stations_list = [station[0] for station in results]

    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)

    # Find the most recent date in the Measurement table
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')

    # Calculate the date one year ago
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the last 12 months of temperature observation data for the most active station
    most_active_station_id = 'USC00519281'  # Replace with dynamic retrieval if needed
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == most_active_station_id).\
        filter(Measurement.date >= one_year_ago).all()

    session.close()

    # Create a list of temperature observations
    tobs_list = [temp[0] for temp in results]

    return jsonify(tobs_list)

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

    return jsonify(temp_data)

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

if __name__ == "__main__":
    app.run(debug=True)
