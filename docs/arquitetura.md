SGHSS_Uninter/
├── venv/                         # Ambiente virtual Python
├── docs/                         # Documentação (PDF final, diagramas UML/DER)
│   ├── Orientacoes.pdf
│   ├── Roteiro.pdf
│   ├── DER.png
│   └── UML.png
├── src/   
│   ├── models/                   # Classes do Banco de Dados (ORM)
│   │   ├── __init__.py           # Inicializa o DB e exporta os Models
│   │   ├── user_model.py         # Classe User (Autenticação/Perfil)
│   │   ├── patient_model.py      # Classe Patient (Dados cadastrais)
│   │   └── professional_model.py # Classe Professional (Dados médicos)  
│   │   └── appointment_model.py  # Classe Appointment (marcar consultas) 
│   ├── app.py                    # Entry Point da aplicação
│   ├── config.py                 # Configurações (ex: Chave Secreta, Banco de Dados)
│   ├── databse.py                # Instância do SQLAlchemy
│   └── routes/                   # Rotas da API (Endpoints)
│       ├── __init__.py
│       ├── auth_routes.py        # Rotas de /login e /sign-up
│       └── patient_routes.py     # Rotas de /pacientes
│       └── appointment_routes.py # Rotas de /appointment
├── requirements.txt              # Dependências Python
└── README.md                     # Documentaçãoo