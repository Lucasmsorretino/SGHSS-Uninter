from .__init__ import db
# datetime é usado para manipular datas, como 'data_nascimento'
from datetime import date 

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    
    # RELACIONAMENTO: Um Paciente PODE ter um User (login no sistema) - 1:1
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=True)
    
    # Dados de Cadastro (Requisito RF001)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.Text)

    # RELACIONAMENTO: Um Paciente pode ter VÁRIAS Consultas - 1:N
    # Esta linha referencia a classe 'Appointment' (a ser criada)
    consultas = db.relationship('Appointment', backref='patient', lazy='dynamic')
    
    # Métodos (Comportamento)
    
    def calculate_age(self):
        """Calcula a idade do paciente com base na data de nascimento."""
        today = date.today()
        # Subtrai o ano de nascimento do ano atual e ajusta se o aniversário não passou
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def to_dict(self):
        """Método essencial para retornar o objeto como JSON na API."""
        # Se o paciente tiver um User, incluímos o nome do User
        nome_paciente = self.user.nome if self.user else "Paciente não registrado" 
        
        return {
            'id': self.id,
            'nome': nome_paciente,
            'cpf': self.cpf,
            'data_nascimento': str(self.data_nascimento),
            'idade': self.calculate_age(),
            'telefone': self.telefone
        }