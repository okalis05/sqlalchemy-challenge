# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

#import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func
from flask import Flask , jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///SurfsUp/Starter_Code-11/Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine)

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
#defining our flask routes
@app.route("/")
def welcome():

    print(f"Welcome to my first Flask")
    #List of all the available routes.
    return (
           f"Available Routes:<br/>"
           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/stations<br/>"
           f"/api/v1.0/tobs<br/>"
           f"/api/v1.0/start<br/>"
           f"/api/v1.0/start/end"
           )


#defining our precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():

    print(f"Starting the precipitation query session.")
   
    #querying the precipitation scores for the past 12 months
    data_df =  session.query(Measurement.date , Measurement.prcp).\
                       filter(Measurement.date >="2016-08-23").all()


    #converting the results of our query to a dictionary
    #declaring a variable to hold our list 
    data = []
  
    #iterating through the rows 
    for  date , prcp in data_df:

        # declaring a variable to hold our dictionary
        data_dict = {}

        #appending values to list of dictionaries.
        data_dict["date"] = date
        data_dict["prcp"] = prcp
        data.append(data_dict)

     #returning the list of dictionaries in a json format
    return jsonify(data)

    print(f"precipitation session completed ")

#defining our stations route
@app.route("/api/v1.0/stations")
def stations():

    print(f" Starting the stations query session.")
    
    #querying the stations of our dataset
    response = session.query(Station.station).all()

    #convering the query results to a list.
    station_list = list(np.ravel(response))

     #returning the query results in a json format
    return jsonify(station_list)
                           
print(f"Station's query session successfully completed.")

# defining our tobs route
@app.route("/api/v1.0/tobs")
def tobs():

    print(f"Starting the query session of temperatures")

    #defining our date range
    previous_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    #querying the dates and temperatures of our most active station
    #for the previous year
    query = session.query(Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date >= previous_year).all()
    
    #converting he query results to a list
    tobs = list(np.ravel(query))

    #returning the query results in a json format
    return jsonify(tobs)

print(f"Query session successfully completed")

#defining our start_date route          
@app.route("/api/v1.0/<start>")
def starter(start):

    #Return a JSON list of the minimum temperature, the average temperature,
    # and the maximum temperature for a specified start date
    #defining the start_date variable and conversion formula
    start_date = dt.datetime.strptime(start, "%m-%d-%Y")

    #setting up our selection 
    sel = [
       func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs)
       ]
     #querying the min,avg and max temperatures for the previous year          
    query1 = session.query(*sel).filter(Measurement.date >= start_date).all()
    
    #converting he query results to a list
    starter_data  = list(np.ravel(query1 ))
       
    #returning the query results in a json format
    return jsonify(starter_data)

print(f"session completed successfully.")

#defining our start/end_date route
@app.route("/api/v1.0/<start>/<end>")
def date_range(start,end):

    #declaring our dates variables and conversion formula
    start_date = dt.datetime.strptime(start, "%m-%d-%Y")
    end_date  = dt.datetime.strptime(end, "%m-%d-%Y")
 
    #querying the min,avg and max temperatures for previous year
    sel = [
       func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs)
       ]

    #calculating the TMIN,TAVG and TMAX of our start date(2017-01-01) and
    #for our end date (2017-01-31)         
    query3 = session.query(*sel).filter(Measurement.date >= start_date ).\
                                    filter(Measurement.date <= end_date ).all()
    
    post_data = list(np.ravel(query3))

    #returning the results in a json format
    return jsonify(post_data)

print(f"End of session!") 
print(f"We will be back  soon!")


if __name__ == "__main__":
    app.run(debug=True)

# --------------------------------------------------------------------------------
