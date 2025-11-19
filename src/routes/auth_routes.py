from flask import Blueprint, request, jsonify
from models.user_model import User
from models import db
from datetime import datetime
from functools import wraps

# Cria um Blueprint (módulo de rotas) para Autenticação
auth = Blueprint('auth', __name__)

# ------------------------------------------------------------------
# ENCODING: Rota POST /auth/register (Sign-up)
# Requisito: Criação de Usuário e Segurança (Hashing de Senha)
# ------------------------------------------------------------------
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validação mínima de entrada
    if not data or not 'nome' in data or not 'email' in data or not 'password' in data:
        return jsonify({"message": "Dados incompletos. Nome, email e password são obrigatórios."}), 400

    email = data['email']
    password = data['password']
    nome = data['nome']
    role = data.get('role', 'PACIENTE') # Define 'PACIENTE' como padrão
    
    # Verifica se o e-mail já existe
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Este e-mail já está cadastrado."}), 409 # Conflict

    # Cria o novo usuário
    new_user = User(nome=nome, email=email, role=role)
    new_user.set_password(password) # Armazena o hash da senha (Segurança/LGPD)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "message": "Usuário registrado com sucesso.",
            "user_id": new_user.id,
            "role": new_user.role
        }), 201 # Created
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erro ao registrar usuário: {str(e)}"}), 500

# ------------------------------------------------------------------
# ENCODING: Rota POST /auth/login (Autenticação)
# Requisito: Login e Geração de Token (simulado por enquanto)
# ------------------------------------------------------------------
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    # Verifica o usuário e a senha (usando o hash seguro)
    if user and user.check_password(password):
        # NOTA: Em um projeto real, aqui você geraria um JWT (JSON Web Token)
        # Por simplicidade e para a entrega do projeto, simularemos um token.
        
        simulated_token = f"TOKEN_SGHSS_{user.id}_{user.role}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        return jsonify({
            "message": "Login realizado com sucesso!",
            "token": simulated_token,
            "user_id": user.id,
            "role": user.role
        }), 200 # OK
    else:
        return jsonify({"message": "Credenciais inválidas. Verifique seu e-mail e senha."}), 401 # Unauthorized