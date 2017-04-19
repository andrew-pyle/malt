'''
MALT Dashboard

by: Andrew Pyle, Zhenlin Jin, Hanzhao Chen
UA LITTLE ROCK DEPARTMENT OF COMPUTER SCIENCE

DESCRIPTION:
As a part of the MALT: Malicious Login Tracker system, MALT Dashboard serves as the front-end.
This Flask web app routes HTTP requests, manipulates data (Pandas Library),
and creates charts (Plotly Python API).

The static CSS and JS files are under static/assets. This is requrired for
Flask to serve them during development. The web server should serve these files in production.

The data manipulation and charting modules are imported below. They expect a Pandas DataFrame with
The data to be visualized.
'''

import datetime
from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import dashboard_units as dash
from df_process import create_df
from df_process import filter_df

app = Flask(__name__)


## Import flat JSON file with data sample for development
data = "data.json"
df = create_df(data)
df.index += 1


## URL Routing
@app.route("/")
def index():
    url_args = {
    'radius': '',
    'latitude': '',
    'longitude': '',
    'start_date': '',
    'end_date': '',
    'start_time': '',
    'end_time': ''
    }
    return render_template("index.html",
        account_distribution = dash.AccountDistribution(df),
        location_distribution = dash.LocationDistribution(df),
        time_of_day_distribtion = dash.TimeOfDayDistribution(df),
        ip_address_distribution_today = dash.IPAddressDistributionToday(df),
        data_table = dash.DataTable(df),
        iterrows = df.iterrows(),
        filter_vals = url_args)


@app.route("/query/")
def query():
    url_args = {
    'radius': request.args['radius'],
    'latitude': request.args['latitude'],
    'longitude': request.args['longitude'],
    'start_date': request.args['start_date'],
    'end_date': request.args['end_date'],
    'start_time': request.args['start_time'],
    'end_time': request.args['end_time']
    }
    subsetdf = filter_df(df,
        radius = url_args['radius'],
        latitude = url_args['latitude'],
        longitude = url_args['longitude'],
        start_date = url_args['start_date'],
        end_date = url_args['end_date'],
        start_time = url_args['start_time'],
        end_time = url_args['end_time'])
    return render_template("index.html",
        account_distribution = dash.AccountDistribution(subsetdf),
        location_distribution = dash.LocationDistribution(subsetdf),
        time_of_day_distribtion = dash.TimeOfDayDistribution(subsetdf),
        ip_address_distribution_today = dash.IPAddressDistributionToday(subsetdf),
        data_table = dash.DataTable(subsetdf),
        iterrows = subsetdf.iterrows(),
        filter_vals = url_args)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
