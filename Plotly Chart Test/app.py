from flask import Flask
from flask import render_template

import json
import plotly.offline
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

# Data Path
data = "data.json"
df = pd.read_json(data)
df.index += 1

# Function Declarations
def AccountHistogram(data_filename):
    #df = pd.read_json(data_filename)
    accounts = [
        go.Histogram(x=df["IP Address"])
    ]
    return plotly.offline.plot(accounts, output_type='div', include_plotlyjs=False)

def LocationHistogram(data_filename):
    #df = pd.read_json(data_filename)
    locations = [
        go.Histogram(x=df["City"])
    ]
    return plotly.offline.plot(locations, output_type='div', include_plotlyjs=False)


@app.route("/")
def index():
    return render_template(
        "index.html",
        account_histogram=AccountHistogram(data),
        location_histogram=LocationHistogram(data),
        data_table=df.to_html(),
        )

@app.route("/hero_thirds")
def hero_thirds():
    return render_template("hero_thirds.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/number1")
def number1():
    return render_template("number1.html")

@app.route("/geo")
def geo():
    return render_template("geo.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
