import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='test',
                                       user='root',
                                       password='')
        if conn.is_connected():
            return conn;

    except Error as e:
        print(e)

