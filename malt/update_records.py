# run every hour

import pandas as pd
from df_process import store_emails
from quickstart import get_emails
from mysql_credentials import set_credentials
# Set configuration here for MySQL server (also in app.py!)
credentials = set_credentials()
HOSTNAME = credentials['HOSTNAME']
USER = credentials['USER']
PASSWORD = credentials['PASSWORD']
DATABASE = credentials['DATABASE']


# Get emails and store them to MySQL database as described above
email_list = get_emails()
store_emails(email_list, hostname=HOSTNAME, user=USER, password=PASSWORD, database=DATABASE)
