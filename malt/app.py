'''
MALT - Flask Web Application
-----------------------------------------------
Andrew Pyle, Zhenlin Jin, Hanzhao Chen
UA LITTLE ROCK DEPARTMENT OF COMPUTER SCIENCE
-----------------------------------------------
This python applicaiton routes HTTP requests, manipulates data (Pandas Library), creates charts
(Plotly Python API). The static CSS and JS files are under static/assets. This is requrired for
Flask to serve them in production. The web server should serve these files in production.

The data manipulation and charting functions are defined below. They expect a Pandas DataFrame with
The data to be visualized.

DataFrame columns expected (as of 23 Mar 2017):
 - df['Account Name']
 - df['City']
 - df['Hour']
 - df[['Country']
 - df['State']
 - df['City']
 - df['Date']
 - df['Time']
 - df['IP Address']

TODO:
 - Create python function to query a database for the data and feed it to the functions (save it in
 memory or query in each function?)
  - Create markers for the leaflet map. (Database query)
  - AJAX query for leafletMapCustom.js to fetch markers (lat/long)
'''

import datetime
from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
from flask_mysqldb import MySQL

import dashboard_units as dash
from df_process import create_df
from df_process import filter_df

app = Flask(__name__)


## Import flat JSON file with data sample for development
data = "data.json"
df = create_df(data)
df.index += 1


# MySQL Connection
MySQL.MYSQL_HOST = 'localhost'
MySQL.MYSQL_***REMOVED***
mysql = MySQL(app)


## URL Routing
@app.route("/")
def index():
    return render_template("index.html",
        account_distribution = dash.AccountDistribution(df),
        location_distribution = dash.LocationDistribution(df),
        time_of_day_distribtion = dash.TimeOfDayDistribution(df),
        ip_address_distribution_today = dash.IPAddressDistributionToday(df),
        data_table = dash.DataTable(df),
        markers = df[['Latitude', 'Longitude','Account Name','City','State','Date','IP Address']].values.tolist())


@app.route("/query/")
def query():
    subsetdf =  filter_df(df, radius=request.args['radius'],
                  latitude=request.args['latitude'],
                  longitude=request.args['longitude'],
                  start_date=request.args['start_date'],
                  end_date=request.args['end_date'],
                  start_time=request.args['start_time'],
                  end_time=request.args['end_time'])
    return render_template("index.html",
        account_distribution = dash.AccountDistribution(subsetdf),
        location_distribution = dash.LocationDistribution(subsetdf),
        time_of_day_distribtion = dash.TimeOfDayDistribution(subsetdf),
        ip_address_distribution_today = dash.IPAddressDistributionToday(subsetdf),
        data_table = dash.DataTable(subsetdf),
        markers = subsetdf[['Latitude', 'Longitude','Account Name','City','State','Date','IP Address']].values.tolist())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
