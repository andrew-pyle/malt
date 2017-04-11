import pandas as pd

# Pandas DataFrame Generation
def create_df(data):
    ## Import flat JSON file with data sample for development
    data = "data.json"
    df = pd.read_json(data)
    df.index += 1

    return df


# Pandas DataFrame Query
def filter_df(df, radius='',
                  latitude='',
                  longitude='',
                  start_date='',
                  end_date='',
                  start_time='',
                  end_time=''):
    ''' Selects rows in a dataframe within a search radius (in km)
    around a latitude/longitude coordinate point'''

    # Remove dataframe rows outside a circle area with approximate radius (km) from latitude/longitude coordinate point
    if latitude != '' and longitude != '':
        df = df[((df['Latitude']<= float(latitude) + (float(radius) / 111)) & (df['Latitude']>= float(latitude) - (float(radius) / 111)) \
             & ((df['Longitude']<= float(longitude) + (float(radius) / 111)) & (df['Longitude']>= float(longitude) - (float(radius) / 111))))]
    # Remove dataframe rows outside the date range
    if start_date != '':
        df = df[df['Date'] >= pd.to_datetime(start_date)]
    if end_date != '':
        df = df[df['Date'] <= pd.to_datetime(end_date)]
    # Remove dataframe rows outside the time range
    if start_time != '':
        df = df[df['Time'] >= pd.to_datetime(start_time)]
    if end_time != '':
        df = df[df['Time'] <= pd.to_datetime(end_time)]

    return df
