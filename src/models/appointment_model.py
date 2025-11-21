from database import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='AGENDADA') # AGENDADA, REALIZADA, CANCELADA
    tipo = db.Column(db.String(20), default='PRESENCIAL') # PRESENCIAL, TELEMEDICINA
    link_telemedicina = db.Column(db.String(255))
    observacoes = db.Column(db.Text)
    
    # Chaves Estrangeiras
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'), nullable=True) # Nullable por enquanto para facilitar testes
    
    def to_dict(self):
        return {
            'id': self.id,
            'data_hora': str(self.data_hora),
            'status': self.status,
            'tipo': self.tipo,
            'link_telemedicina': self.link_telemedicina,
            'patient_id': self.patient_id,
            'professional_id': self.professional_id
        }