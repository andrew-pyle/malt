import pandas as pd

df = pd.read_json("data.json")

ipSeries = df["IP Address"].value_counts()
ipFrame = pd.DataFrame({'ipAddress':ipSeries.index, 'login count':ipSeries.values})
x=[ipFrame.ipAddress]
y=[ipFrame['login count']]

print(x, y)
