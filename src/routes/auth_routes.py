from flask import Blueprint, request, jsonify
from models.user_model import User
from database import db
from datetime import datetime
from functools import wraps
# Importa as funções para criar o token
from flask_jwt_extended import create_access_token

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

    if user and user.check_password(password):
            # GERAÇÃO DO JWT REAL
            # identity=user.id: guarda o ID do usuário dentro do token criptografado
            # additional_claims: guarda o perfil (role) para verificarmos permissão depois
            access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
            
            return jsonify({
                "message": "Login realizado com sucesso!",
                "token": access_token,  # Token real (eyJh...)
                "user_id": user.id,
                "role": user.role
            }), 200
    else:
        return jsonify({"message": "Credenciais inválidas. Verifique seu e-mail e senha."}), 401 # Unauthorized