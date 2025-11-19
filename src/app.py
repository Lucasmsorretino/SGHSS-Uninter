from flask import Flask
from config import Config
from models.user_model import User
from models import db # Importa a instância de DB
from routes.auth_routes import auth # Importa o novo módulo de rotas

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # REGISTRO DOS BLUEPRINTS
    # Define que todas as rotas em auth_routes começarão com /auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    
    # Cria as tabelas do banco de dados (SQLite)
    with app.app_context():
        db.create_all() # Cria as tabelas User, Patient, etc.
        
    app.run(debug=True)