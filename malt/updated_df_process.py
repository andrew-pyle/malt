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


# '''
# MALT Dashboard Data Manipulation module

# DataFrame column names expected:
#  - df['Account Name']
#  - df['City']
#   - df['State']
#  - df['Country']
#  - df['Date']'''
# MALT Dashboard Data Manipulation module

# DataFrame column names expected:
#  - df['Account Name']
#  - df['City']
#  - df['State']
#  - df['Country']
#  - df['Date']
#  - df['Time']
#  - df['IP Address']
#  - df['Latitude']
#  - df['Longitude']
#  '''

# import pandas as pd

# # Pandas DataFrame Generation
# def create_df(data):
#     ''' Creates pandas dataframe in memory from the data source'''
#     ## JSON file data source (for development)
#     df = pd.read_json(data)
#     df.index += 1

#     ## MySQL data source

#     return df


# # Pandas DataFrame Query
# def filter_df(df, radius='', latitude='', longitude='',
#               start_date='', end_date='', start_time='', end_time=''):
#     ''' Selects rows in a dataframe within a search radius (in km)
#     around a latitude/longitude coordinate point'''

#     # Remove dataframe rows outside a circle area with approximate radius (km) from latitude/longitude coordinate point
#     if latitude != '' and longitude != '':
#         df = df[((df['Latitude']<= float(latitude) + (float(radius) / 111)) & (df['Latitude']>= float(latitude) - (float(radius) / 111)) \
#              & ((df['Longitude']<= float(longitude) + (float(radius) / 111)) & (df['Longitude']>= float(longitude) - (float(radius) / 111))))]
#     # Remove dataframe rows outside the date range
#     if start_date != '':
#         df = df[df['Date'] >= pd.to_datetime(start_date)]
#     if end_date != '':
#         df = df[df['Date'] <= pd.to_datetime(end_date)]
#     # Remove dataframe rows outside the time range
#     if start_time != '':
#         df = df[df['Time'] >= pd.to_datetime(start_time)]
#     if end_time != '':
#         df = df[df['Time'] <= pd.to_datetime(end_time)]

#     return df
#  - df['Time']
#  - df['IP Address']
#  - df['Latitude']
#  - df['Longitude']
#  '''

import pandas as pd
import MySQLdb   #pip3 install mysql-client
import sys



#here we have the MySQL configured as an example. Running on localhost, its username is root,
# password is '123123123', and we are accessing the specific database named 'malt'
try:
    conn = MySQLdb.connect('localhost','root','123123123','malt')
except Exception as e:
    sys.exit("We can't get into the database")

c = conn.cursor()

#before we get the data variable from Hanzhao, we insert the following records into database

#two data records

schema = [['jinzh','34.7464809','92.2895947', '2017-01-08 20:52:47','73.133.196.202','P-town','Oregon','USA'],['Dummy Data', '92.2895947', '34.7464809','2016-01-08 20:52:47', '2602:30a:c071:a260:6c0d:5d86:be0f:a774', 'San Jose', 'California', 'USA']]

#create a table named T7
c.execute("CREATE TABLE IF NOT EXISTS T7(`Account Name` varchar(15), Latitude float(20), longitude float(20), Datetime datetime, `IP Address` varchar(40), `City` varchar(20), `State` varchar(20), `Country` varchar(25)) ")


#here is the insertion and commit row by row of data records
for col in schema:
    c.execute("INSERT INTO T7( `Account Name`, Latitude, Longitude, Datetime, `IP Address`, City, State, Country) VALUES (%s, %s, %s, %s, %s,%s, %s, %s )", (col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7]))
    conn.commit()

# Pandas DataFrame Generation
def create_df():
    ## MySQL data source
    df = pd.read_sql('SELECT * from T7', con = conn)
    c.close()
    conn.close()
    return df

# def create_ts():
#     timestamp = pd.read_sql('SELECT TIMESTAMP(Date, Time) from T5', con = conn)
#     c.close()
#     conn.close()
#     return timestamp


# Pandas DataFrame Query
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
        df = df[df['Date'] >= pd.to_datetime(start_date)]
    if end_date != '':
        df = df[df['Date'] <= pd.to_datetime(end_date)]
    # Remove dataframe rows outside the time range
    if start_time != '':
        df = df[df['Time'] >= pd.to_datetime(start_time)]
    if end_time != '':
        df = df[df['Time'] <= pd.to_datetime(end_time)]

    return df
