from flask import Flask
from flask import render_template

import plotly.offline
import plotly.graph_objs as go
import plotly.figure_factory as FF

import pandas as pd

app = Flask(__name__)

# Data Path
data = "data.json"
df = pd.read_json(data)
df.index += 1


# Function Declarations
def AccountHistogram():
    ipSeries = df["IP Address"].value_counts()
    ipFrame = pd.DataFrame({'ipAddress':ipSeries.index, 'login count':ipSeries.values})
    trace = [
        go.Bar(
            x = ipFrame["ipAddress"],
            y = ipFrame["login count"],
            #width = 0.9,
            marker = dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                ),
                #colorbar = dict(
                #    thickness = 1,
                #),
            ),
            opacity=0.6,
        ),
    ]
    layout = go.Layout(
        margin = dict(
            l=35,
            r=0,
            t=1,
            b=30,
            ),
        xaxis = dict(
            #title = "Account Name",
            showticklabels = False,
            tickmode = 'auto',
            nticks = 10,
            tickfont = dict(
                size=10,
                ),
            ),
        yaxis = dict(
            #title = "Frequency"
            ),
    )
    accounts = go.Figure(data=trace, layout=layout)
    return plotly.offline.plot(
        accounts,
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

def LocationHistogram():
    #df = pd.read_json(data_filename)
    trace = [
        go.Histogram(x=df["City"],
        marker = dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
                ),
            ),
        opacity=0.6,
        ),
    ]
    layout = go.Layout(
        margin = dict(
            l=10,
            r=0,
            t=0,
        ),
        xaxis = dict(
            showticklabels = False,

        ),
    )
    locations = go.Figure(data=trace, layout=layout)

    return plotly.offline.plot(
        locations,
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

def DataTable():
    dfTable = df['Account Name','']
    table = FF.create_table(
        df,
        colorscale = [[0, '#3D4A57'],
                      [.5, '#d9d9d9'],
                      [1, '#ffffff']],
        )
    #table.layout.width = 1000 #width in px
    return plotly.offline.plot(
        table,
        #filename='file.html',
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

## URL Routing
@app.route("/")
def index():
    return render_template(
        "index.html",
        account_histogram = AccountHistogram(),
        location_histogram = LocationHistogram(),
        #data_table = df.to_html(),
        data_table = DataTable(),
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
