from flask import Blueprint, request, jsonify
from models.patient_model import Patient
from models.user_model import User
from database import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

# Cria um Blueprint (módulo de rotas) para Pacientes
patient = Blueprint('patient', __name__)

# NOTA: Em um projeto real, aqui você usaria um decorator para checar o token de autenticação
# Ex: @jwt_required() ou @role_required('MEDICO', 'RECEPCAO', 'ADMIN')

# ------------------------------------------------------------------
# ENCODING: Rota POST /patients (Cadastro de Pacientes)
# Atende ao Requisito: RF001 (Permitir cadastro de pacientes) [cite: 67]
# ------------------------------------------------------------------
@patient.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    
    # Validação dos campos obrigatórios (Requisito RNF001: Tentar cadastrar paciente sem informar CPF) [cite: 103]
    required_fields = ['cpf', 'data_nascimento', 'nome']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Dados incompletos. CPF, data de nascimento e nome são obrigatórios."}), 400

    # Conversão de string de data para objeto date (Formato esperado: YYYY-MM-DD)
    try:
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "Formato de data de nascimento inválido. Use YYYY-MM-DD."}), 400

    # 1. Cria um usuário básico associado ao paciente (para fins de login futuro)
    # Aqui, a senha é simulada ou o usuário é criado como inativo.
    try:
        new_user = User(nome=data['nome'], email=f"{data['cpf']}@sghss.com.br", role='PACIENTE')
        new_user.set_password(data.get('cpf', 'padrao123')) # Senha padrão para o primeiro acesso
        db.session.add(new_user)
        db.session.flush() # Para obter o ID do usuário antes do commit
        
        # 2. Cria o paciente e associa ao usuário
        new_patient = Patient(
            user_id=new_user.id,
            cpf=data['cpf'],
            data_nascimento=data_nascimento,
            telefone=data.get('telefone'),
            endereco=data.get('endereco')
        )
        
        db.session.add(new_patient)
        db.session.commit()
        
        # Resultado Esperado: Exibir mensagem "Paciente cadastrado com sucesso." [cite: 103]
        return jsonify({
            "message": "Paciente cadastrado com sucesso.", 
            "patient_id": new_patient.id,
            "user_id": new_user.id
        }), 201 # Created
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro: CPF já cadastrado no sistema."}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erro interno ao cadastrar paciente: {str(e)}"}), 500

# ------------------------------------------------------------------
# ROTA GET /patients (Listagem de Pacientes)
# --- ROTA PROTEGIDA ---
# Requisito: Apenas usuários logados podem ver a lista de pacientes (LGPD)
# ------------------------------------------------------------------
@patient.route('/patients', methods=['GET'])
@jwt_required()
def list_patients():
    current_user_id = get_jwt_identity() # Pega o ID de quem está logado
    patients = Patient.query.all()

    # Opcional: Você poderia buscar o usuário e checar se é ADMIN/MEDICO
    # current_user = User.query.get(current_user_id)
    # if current_user.role not in ['ADMIN', 'MEDICO', 'RECEPCAO']:
    #     return jsonify({"message": "Acesso não autorizado."}), 403

    # Converte a lista de objetos Python para JSON usando o método to_dict()
    patient_list = [p.to_dict() for p in patients]
    
    return jsonify(patient_list), 200 # OK