from flask import Flask
from flask import render_template

import json
import plotly.offline
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)

# Data Path
#data = "data.json"
#df = pd.read_json(data)
#df.index += 1

# Function Declarations
def AccountHistogram():
    #df = pd.read_json(data_filename)
    trace = [
        go.Histogram(x=[1,1,1,1,1,2,2,45,6,43,4,2]) #x=df["IP Address"]),
    ]
    layout = go.Layout(
        margin = dict(
            l=10,
            r=0,
            t=0,
        ),
    )
    accounts = go.Figure(data=trace, layout=layout)

    return plotly.offline.plot(
        accounts,
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

def LocationHistogram(data_filename):
    #df = pd.read_json(data_filename)
    trace = [
        go.Histogram(x=df["City"])
    ]
    layout = go.Layout(
        margin = dict(
            l=10,
            r=0,
            t=0,
        ),
    )
    locations = go.Figure(data=trace, layout=layout)

    return plotly.offline.plot(
        locations,
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )


@app.route("/")
def index():
    return render_template(
        "index.html",
        account_histogram=AccountHistogram(),
        #location_histogram=LocationHistogram(data),
        #data_table=df.to_html(),
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
