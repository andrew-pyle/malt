'''
MALT Dashboard Data Manipulation module

DataFrame column names expected:
 - df['Account Name']
 - df['IP Address']
 - df['Datetime']
 - df['City']
 - df['State']
 - df['Country']
 - df['Latitude']
 - df['Longitude']
 '''

import pandas as pd
import MySQLdb   #pip3 install mysqlclient
import sys
from warnings import filterwarnings

filterwarnings('ignore', category=MySQLdb.Warning) #This will proceed the program without warning getting in the way when creating the table.

# def get_emails():
#     # #before we get the data variable from Hanzhao, we insert the following records into database
#     #two data records
#     email_list = [['jinzh','34.7464809','92.2895947', '2017-01-08 20:52:47','73.133.196.202','P-town','Oregon','USA'],['Dummy Data', '92.2895947', '34.7464809','2016-01-08 20:52:47', '2602:30a:c071:a260:6c0d:5d86:be0f:a774', 'San Jose', 'California', 'USA']]
#     return email_list

#### MySQL Connection
def store_emails(email_list, hostname='localhost', user='', password='', database=''):
    """here we have the MySQL configured as an example. Running on localhost, its username is root,
    password is '123123123', and we are accessing the specific database named 'malt'"""

    try:
        conn = MySQLdb.connect(hostname, user, password, database)
    except Exception as e:
        sys.exit("We can't get into the database")
    c = conn.cursor()

    #create a table if it doesn't exist named emailRecords
    c.execute("CREATE TABLE IF NOT EXISTS emailRecords(`Account Name` varchar(15), Latitude float(20), Longitude float(20), Datetime datetime, `IP Address` varchar(40), `City` varchar(20), `State` varchar(20), `Country` varchar(25))")
    c.execute("Delete from emailRecords WHERE Datetime < NOW() - INTERVAL 90 DAY")
    #here is the insertion and commit row by row of data records
    for col in email_list:
        if '' not in col:
            c.execute("INSERT INTO emailRecords(`Account Name`, `IP Address`, Datetime, City, State, Country, Latitude, Longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7]))
            conn.commit()
    conn.close()

### Pandas DataFrame Generation
def create_df(hostname='localhost', user='', password='', database=''):
    ''' Creates pandas dataframe in memory from the data source'''
    ## JSON file data source (for development)
    # df = pd.read_json(data)
    # df.index += 1
    # df['Time'] = df['Time'] = pd.to_datetime(df['Time Stamp'])

    ## MySQL data source
    try:
        conn = MySQLdb.connect(hostname, user, password, database)
    except Exception as e:
        sys.exit("We can't get into the database")
    c = conn.cursor()

    df = pd.read_sql('SELECT * from emailRecords', con = conn)
    print(df.dtypes)

    c.close()
    conn.close()

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
