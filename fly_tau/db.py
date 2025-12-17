import mysql.connector
from contextlib import contextmanager
'''MYSQL CONNECTION'''

@contextmanager
def db_cur(dictionary=False):
    mydb= None
    cursor = None
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="fly_tau",
            autocommit=True)
        cursor = mydb.cursor(dictionary=dictionary)
        yield cursor
    except mysql.connector.Error as err:
        raise err
    finally:
        if cursor:
            cursor.close()
        if mydb:
            mydb.close()
