import plotly
#import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import pandas as pd

df = pd.read_json("data.json")

table = FF.create_table(df)
print(plotly.offline.plot(
    table,
    filename='file.html',
    output_type='div',
    include_plotlyjs=False,
    show_link=False,
))