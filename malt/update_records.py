# run every 2 hrs

import pandas as pd
from df_process import store_emails
from quickstart import get_emails

# Set configuration here for MySQL server
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

# Get emails and store them to MySQL database as described above
email_list = get_emails()
store_emails(email_list, hostname=HOSTNAME, user=USER, password=PASSWORD, database=DATABASE)
