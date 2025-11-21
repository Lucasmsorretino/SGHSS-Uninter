from database import db

# IMPORTAÇÃO dos models para que o SQLAlchemy os reconheça
from .user_model import User
from .patient_model import Patient
from .professional_model import Professional 
from .appointment_model import Appointment
# Adicionar futuros models aqui: Prontuario, etc.