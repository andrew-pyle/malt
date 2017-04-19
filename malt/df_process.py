'''
MALT Dashboard Data Manipulation module

DataFrame column names expected:
 - df['Account Name']
 - df['City']
  - df['State']
 - df['Country']
 - df['Date']
 - df['Time']
 - df['IP Address']
 - df['Latitude']
 - df['Longitude']
 '''

import pandas as pd

# Pandas DataFrame Generation
def create_df(data):
    ''' Creates pandas dataframe in memory from the data source'''
    ## JSON file data source (for development)
    df = pd.read_json(data)
    df.index += 1
    df['Time'] = df['Time'] = pd.to_datetime(df['Time Stamp'])

    ## MySQL data source

    return df


# Pandas DataFrame Query
## Correct df['Date'] df['Time'] to correct column.
def filter_df(df, radius='', latitude='', longitude='',
              start_date='', end_date='', start_time='', end_time=''):
    ''' Selects rows in a dataframe within a search radius (in km)
    around a latitude/longitude coordinate point'''

    # Remove dataframe rows outside a circle area with approximate radius (km) from latitude/longitude coordinate point
    if latitude != '' and longitude != '':
        df = df[((df['Latitude']<= float(latitude) + (float(radius) / 111)) & (df['Latitude']>= float(latitude) - (float(radius) / 111)) \
             & ((df['Longitude']<= float(longitude) + (float(radius) / 111)) & (df['Longitude']>= float(longitude) - (float(radius) / 111))))]
    # Remove dataframe rows outside the date range
    if start_date != '':
        df = df[df['Date'].dt.date >= pd.to_datetime(start_date).date()]
    if end_date != '':
        df = df[df['Date'].dt.date <= pd.to_datetime(end_date).date()]
    # Remove dataframe rows outside the time range
    if start_time != '':
        df = df[df['Time'].dt.time >= pd.to_datetime(start_time).date()]
    if end_time != '':
        df = df[df['Time'].dt.time <= pd.to_datetime(end_time).date()]
    return df
