import json
import plotly.offline
import plotly.graph_objs as go
import pandas as pd

df = pd.read_json("data.json")
df.MapText = df.Location + ' ' + df["Account Name"].astype(str)


data = [ dict(
    type = 'scattergeo',
    lon = df.Longitude,
    lat = df.Latitude,
    mode = 'markers',
    text = df.MapText,
    name = df["Account Name"],
    )
]
layout = dict(
    title  = 'Test plot',
    geo = dict(
        projection = dict( type = "miller"),
        showland = True,
        showcoastlines = True,
        showlakes = True,
        showcountries = True,
        showsubunits = True,
        showframe = False,
    )
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, validate=False, filename='test-plot')
