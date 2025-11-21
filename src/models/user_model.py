from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='PACIENTE', nullable=False)
    
    # Relações (Back-reference para Patient/Professional)
    patient = db.relationship('Patient', backref='user', uselist=False)
    professional = db.relationship('Professional', backref='user', uselist=False)

    def set_password(self, password):
        """Cria o hash seguro da senha (Requisito de Segurança)."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha fornecida corresponde ao hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Retorna representação para JSON."""
        return {'id': self.id, 'nome': self.nome, 'email': self.email, 'role': self.role}