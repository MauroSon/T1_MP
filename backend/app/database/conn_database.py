import pymysql

from auth.helper import AuthHelper

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        database='buscamao',
        user='root',
        password='mypassword'
    )
    return connection


class Database:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()
        self.auth = AuthHelper(self.connection, self.cursor)

    def close(self):
        self.connection.close()
        self.cursor.close()
