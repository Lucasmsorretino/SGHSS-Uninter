from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models.user_model import User
from database import db# Importa a instância de DB
from routes.auth_routes import auth # Importa o novo módulo de rotas
from routes.patient_routes import patient # Importa o novo módulo
from routes.appointment_routes import appointment_bp # Importa o módulo de rotas de agendamento

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # Inicializa o JWT Manager
    jwt = JWTManager(app)

    # REGISTRO DOS BLUEPRINTS
    # Define que todas as rotas em auth_routes começarão com /auth
    app.register_blueprint(auth, url_prefix='/auth') # Rotas de autenticação
    app.register_blueprint(patient, url_prefix='/api/v1') # Rotas de dados principais
    app.register_blueprint(appointment_bp, url_prefix='/api/v1') # Rotas de agendamento

    return app

if __name__ == '__main__':
    app = create_app()
    
    # Cria as tabelas do banco de dados (SQLite)
    with app.app_context():
        # Importar os modelos aqui dentro para garantir que o SQLAlchemy os reconheça antes do create_all
        from models import User, Patient, Professional, Appointment
        db.create_all() # Cria as tabelas User, Patient, etc.
        
    app.run(debug=True)