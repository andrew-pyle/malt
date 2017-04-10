import pandas as pd

# Pandas DataFrame Generation
def create_df(data):
    ## Import flat JSON file with data sample for development
    data = "data.json"
    df = pd.read_json(data)
    df.index += 1

    return df


# Pandas DataFrame Query
def filter_df(df, radius=None, latitude=None, longitude=None, start_date=None, end_date=None, start_time=None, end_time=None):
    ''' Selects rows in a dataframe within a search radius (in km) around a latitude/longitude coordinate point'''
    filtered_df = df[((df['Latitude']<= latitude + (radius / 111)) & (df['Latitude']>= latitude - (radius / 111)) & ((df['Longitude']<= longitude + (radius / 111)) & (df['Longitude']>= longitude - (radius / 111))))]

    return filtered_df.to_string()
