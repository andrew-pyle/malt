import json
import plotly.offline
import plotly.graph_objs as go
import pandas as pd

df = pd.read_json("data.json")

accounts = [
    go.Histogram(x=df["IP Address"])
]

locations = [
    go.Histogram(x=df["City"])
]

print(plotly.offline.plot(accounts, output_type='div', filename='account_distr.html', include_plotlyjs=False))
plotly.offline.plot(locations, output_type='div', filename='loc_distr.html')
