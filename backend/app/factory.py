from flask import Flask, g
from database.conn_database import Database
from flask_cors import CORS
from auth.auth import jwt
import pymysql

database = Database()

def create_app():
    # Cria uma instância de aplicação Flask
    app = Flask(__name__)

    CORS(app)

    # Configurações iniciais da aplicação
    """
    OBSERVAÇÃO:
        Esta aplicação foi feita com o intuito educativo. Desta forma, as chaves foram mantidas dentro
        do código-fonte para facilitar o aprendizado. Contudo, é  evidente que esta não é a forma mais segura.
    """
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_PORT'] = '3306'
    app.config['MYSQL_USER'] = 'myuser'
    app.config['MYSQL_PASSWORD'] = 'mypassword'
    app.config['MYSQL_DB'] = 'buscamao'
    app.config['SECRET_KEY'] = "secret_key"
    app.config['JWT_SECRET_KEY'] = 'secret_key'

    # Inicia a instância JWT com a aplicação atual
    jwt.init_app(app)
    
    
    # Cria uma instância de conexão antes de cada request 
    @app.before_request
    def before_request():
        g.db = Database()

    # Exclui a instância de conexão após o término de cada request
    @app.teardown_request
    def teardown_request(err):
        if err:
            print(f"ERROR: {err}")
        db = getattr(g, 'db', None)
        if db is not None:
            try:
                db.close()
            except pymysql.err.Error as e:
                # Se for "Already closed", apenas ignore
                if str(e) != "Already closed":
                    raise


    # Importa rotas a serem utilizadas para as requisições
    from auth.routes import auth_bp
    from loja.routes import loja_bp
    from produto.routes import produto_bp

    # Configura as rotas na aplicação
    app.register_blueprint(auth_bp, url_prefix=f'/{auth_bp.name}')
    app.register_blueprint(loja_bp, url_prefix=f'/{loja_bp.name}')
    app.register_blueprint(produto_bp, url_prefix=f'/{produto_bp.name}')

    return app
