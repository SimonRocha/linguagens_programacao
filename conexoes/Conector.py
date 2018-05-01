import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='db_teatro',
                                       user='root',
                                       password='')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn;

    except Error as e:
        print(e)

def insert():
    cnx = connect()
    cursor = cnx.cursor()

    sql_insert = ("INSERT INTO usuario (login, senha, tipo) VALUES (%s, %s, %s)")
    data_insert = ('simon', 'teste', 1)

    cursor.execute(sql_insert, data_insert)
    new_id = cursor.lastrowid
    cnx.commit()

    cursor.close()
    cnx.close()
    return new_id

def delete(id_delete):
    cnx = connect()
    cursor = cnx.cursor()

    sql_delete = ("DELETE FROM usuario WHERE id = %s")
    data_delete = (id_delete,)

    cursor.execute(sql_delete, data_delete)
    cnx.commit()

    cursor.close()
    cnx.close()

id = insert()
delete(id)

