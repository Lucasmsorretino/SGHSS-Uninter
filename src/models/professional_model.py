from database import db

class Professional(db.Model):
    __tablename__ = 'professionals'
    id = db.Column(db.Integer, primary_key=True)
    
    # Chave Estrangeira para o User (Relacionamento 1:1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
    registro_profissional = db.Column(db.String(50), nullable=False)  # Ex: CRM, COREN
    especialidade = db.Column(db.String(50))

    # Relacionamento 1:N com Consultas (a ser implementado no model Appointment)
    consultas = db.relationship('Appointment', backref='professional', lazy='dynamic')
    
    def to_dict(self):
        """Retorna representação para JSON."""
        return {
            'id': self.id,
            'nome': self.user.nome if self.user else None,
            'registro_profissional': self.registro_profissional,
            'especialidade': self.especialidade
        }