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

from flask import Flask
from flask import render_template
import dashboard_units as dash
import pandas as pd
from flask_mysqldb import MySQL

app = Flask(__name__)


## Import flat JSON file with data sample for development
data = "data.json"
df = pd.read_json(data)
df.index += 1


# MySQL Connection
MySQL.MYSQL_HOST = 'localhost'
MySQL.MYSQL_USER = 'root'
mysql = MySQL(app)

## URL Routing
@app.route("/")
def index():
    return render_template(
        "index.html",
        account_distribution = dash.AccountDistribution(df),
        location_distribution = dash.LocationDistribution(df),
        time_of_day_distribtion = dash.TimeOfDayDistribution(df),
        ip_address_distribution_today = dash.IPAddressDistributionToday(df),
        data_table = dash.DataTable(df),
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
