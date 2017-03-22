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
def AccountDistribution():
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

def LocationDistribution():
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

def TimeOfDayDistribution():
    # Declare variables for layout below. I couldn't figure out how to create them inline.
    hours_list = list(range(0,25))
    hours_format_list = []
    for x in range(0,25):
        hours_format_list.append('{}:00'.format(x))


    timeSeries = df["Hour"].value_counts()
    timeFrame = pd.DataFrame({'Time':timeSeries.index, 'Count':timeSeries.values})
    trace = [
        go.Bar(
            x = timeFrame["Time"],
            y = timeFrame["Count"],
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
            b=50,
            ),
        xaxis = dict(
            autotick = False,
            showticklabels = True,
            tickmode = 'array',
            tickvals = list(range(0,25)), ## Should be: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
            ticktext = hours_format_list, ## Should be: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'],
            tickfont = dict(
                size=10,
                ),
            ),
        yaxis = dict(
            #title = "Frequency"
            ),
    )
    times = go.Figure(data=trace, layout=layout)
    return plotly.offline.plot(
        times,
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

def DataTable():
    table = FF.create_table(
        df,
        colorscale = [[0, '#3D4A57'],
                      [.5, '#d9d9d9'],
                      [1, '#ffffff']],
        )

    return plotly.offline.plot(
        table,
        filename='file.html',
        output_type='div',
        include_plotlyjs=False,
        show_link=False,
        )

## URL Routing
@app.route("/")
def index():
    return render_template(
        "index.html",
        account_distribution = AccountDistribution(),
        location_distribution = LocationDistribution(),
        time_of_day_distribtion = TimeOfDayDistribution(),
        #data_table = df.to_html(),
        data_table = DataTable(),
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
