from flask import Blueprint, request, jsonify
from models.appointment_model import Appointment
from models.patient_model import Patient
from models.professional_model import Professional
from database import db
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

# Cria o Blueprint para Agendamentos
appointment_bp = Blueprint('appointment', __name__)

# ------------------------------------------------------------------
# ROTA POST /appointments (Agendar Consulta)
# Requisito: Agendar consultas presenciais ou telemedicina
# ------------------------------------------------------------------
@appointment_bp.route('/appointments', methods=['POST'])
@jwt_required() # Exige login para agendar
def create_appointment():
    data = request.get_json()
    
    # Validação de campos obrigatórios
    if not data or 'patient_id' not in data or 'data_hora' not in data:
        return jsonify({"message": "Dados incompletos. Informe patient_id e data_hora."}), 400

    # Verifica se o Paciente existe
    patient = Patient.query.get(data['patient_id'])
    if not patient:
        return jsonify({"message": "Paciente não encontrado."}), 404

    # Conversão de Data/Hora (Esperado: "2025-10-20 14:30:00")
    try:
        dt_object = datetime.strptime(data['data_hora'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({"message": "Formato de data inválido. Use YYYY-MM-DD HH:MM:SS"}), 400

    # Lógica para vincular Profissional (Opcional na criação, pode ser atribuído depois)
    professional_id = data.get('professional_id')
    if professional_id:
        prof = Professional.query.get(professional_id)
        if not prof:
            return jsonify({"message": "Profissional não encontrado."}), 404

    # Criação do Agendamento
    new_appointment = Appointment(
        patient_id=data['patient_id'],
        professional_id=professional_id,
        data_hora=dt_object,
        tipo=data.get('tipo', 'PRESENCIAL'), # PRESENCIAL ou TELEMEDICINA
        status='AGENDADA',
        observacoes=data.get('observacoes'),
        link_telemedicina=data.get('link_telemedicina') # Para requisito de Telemedicina
    )

    try:
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({
            "message": "Consulta agendada com sucesso!",
            "appointment": new_appointment.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Erro ao agendar: {str(e)}"}), 500

# ------------------------------------------------------------------
# ROTA GET /appointments (Listar Consultas)
# ------------------------------------------------------------------
@appointment_bp.route('/appointments', methods=['GET'])
@jwt_required()
def list_appointments():
    # Filtros opcionais (ex: listar apenas de um paciente específico)
    patient_id = request.args.get('patient_id')
    
    if patient_id:
        query = Appointment.query.filter_by(patient_id=patient_id)
    else:
        query = Appointment.query
        
    appointments = query.all()
    return jsonify([a.to_dict() for a in appointments]), 200