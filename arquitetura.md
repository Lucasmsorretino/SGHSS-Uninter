SGHSS_ProjetoFinal/
├── venv/                       # Ambiente virtual Python
├── docs/                       # Documentação (PDF final, diagramas UML/DER)
│   ├── Orientacoes.pdf
│   ├── Roteiro.pdf
│   ├── DER.png
│   └── UML.png
├── src/   
│   ├── models/                   # NOVA PASTA para modularização
│   │   ├── __init__.py           # Inicializa o DB e exporta os Models
│   │   ├── user_model.py         # Classe User (Autenticação/Perfil)
│   │   ├── patient_model.py      # Classe Patient (Dados cadastrais)
│   │   └── professional_model.py # Classe Professional (Dados médicos)                     # Código Fonte da Aplicação
│   ├── app.py                  # Instância principal do Flask (Entry Point)
│   ├── config.py               # Configurações (ex: Chave Secreta, Banco de Dados)
│   └── routes/                 # Rotas da API (Endpoints)
│       ├── __init__.py
│       ├── auth_routes.py      # Rotas de /login e /sign-up
│       └── patient_routes.py   # Rotas de /pacientes
├── tests/                      # Casos de Teste (Pytest)
├── requirements.txt            # Dependências Python
└── README.md                   # Descrição e instruções de execução