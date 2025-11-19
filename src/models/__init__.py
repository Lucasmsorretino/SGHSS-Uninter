from flask_sqlalchemy import SQLAlchemy

# A instância de DB deve ser criada aqui
db = SQLAlchemy()

# IMPORTAÇÃO dos models para que o SQLAlchemy os reconheça
from .user_model import User
from .patient_model import Patient
from .professional_model import Professional 
# Adicionar futuros models aqui: Appointment, Prontuario, etc.