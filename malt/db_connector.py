import pymysql.cursors

class DBConnection
"""
MALT's connection to MySQL database using PyMySQL.

Attributes:
    host:       PyMySQL host
    user:       PyMySQL user
    password:   PyMySQL password
    db:         PyMySQL database Name
    charset:    PyMySQL character set (='utf8mb4')
    cursorclass: PyMySQL cursor setting
    sql:        SQL query to execute
    query:      query result
Methods:
    db_connection()
"""

def __init__(self, host, user, password, db, charset, cursorclass):
    self.host = host
    self.user = user
    self.password = password
    self.db = db
    self.charset = charset
    self.cursorclass = cursorclass
    # self.sql = sql
    # self.query = query


def db_connection():  #host='localhost', user='root', password, db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='a1boxxit',
                                 db='malttest',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #
        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `userName`,`userPassword` FROM maltusers WHERE `userName` = 'user1'";
            cursor.execute(sql)
            result = cursor.fetchall()
            return(result)
    finally:
        connection.close()

#print(db_connection())
