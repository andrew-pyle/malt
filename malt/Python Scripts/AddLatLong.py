
# coding: utf-8

# In[1]:

import json
import plotly.offline
import plotly.graph_objs as go
import pandas as pd


# In[111]:

df = pd.read_json("data.json")


# In[101]:

df.head()


# In[66]:




# In[67]:

import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim()

location_lat = []
location_long = []
for x in range(0, len(df)):
    city = df.City[x]
    #print(city)
    state = df.State[x]
    #print(state)
    country = df.Country[x]
    #print(country)
    location = {"city": city, "state": state, "country": country,}
    location_lat.append(geolocator.geocode(location, timeout=2).latitude)
    location_long.append(geolocator.geocode(location, timeout=2).longitude)


# In[112]:

lat_series = pd.Series(location_lat, name="Latitude")
long_series = pd.Series(location_long, name="Longitude")
df = pd.concat([df, lat_series, long_series], axis=1)
df.head()


# In[113]:

df.to_json("data.json", orient="records")


# In[ ]:



