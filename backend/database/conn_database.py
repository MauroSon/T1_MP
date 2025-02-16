import pymysql

from auth.helper import AuthHelper
from loja.helper import LojaHelper
from produto.helper import ProdutoHelper
from avaliacao.helper import AvaliacoesHelper

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
        self.loja = LojaHelper(self.connection, self.cursor)
        self.produto = ProdutoHelper(self.connection, self.cursor)
        self.reviews = AvaliacoesHelper(self.connection, self.cursor)

    def close(self):
        self.connection.close()
        self.cursor.close()
