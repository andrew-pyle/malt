import pandas as pd

# Pandas DataFrame Generation
def create_df(data):
    ## Import flat JSON file with data sample for development
    data = "data.json"
    df = pd.read_json(data)
    df.index += 1

    return df


# Pandas DataFrame Query
def query_df(df, latitude=None, longitude=None, start_date=None, end_date=None, start_time=None, end_time=None):


    return df
