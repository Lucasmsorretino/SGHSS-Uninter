# SGHSS - Sistema de Gestão Hospitalar (Backend)

Projeto de desenvolvimento de uma API RESTful para o Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS), desenvolvido como atividade prática da disciplina de Projeto Multidisciplinar (UNINTER - 2025).

## 📋 Sobre o Projeto

O sistema visa centralizar a gestão de pacientes, profissionais de saúde e agendamentos de consultas (presenciais e telemedicina), garantindo segurança e integridade dos dados conforme a LGPD.

**Ênfase:** Back-end (Modelagem de Dados, API, Regras de Negócio e Segurança).

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework:** Flask
* **Banco de Dados:** SQLite (via SQLAlchemy)
* **Autenticação:** JWT (Flask-JWT-Extended)
* **Segurança:** Werkzeug (Password Hashing)

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3 instalado.
* Git instalado.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Lucasmsorretino/SGHSS-Uninter](https://github.com/Lucasmsorretino/SGHSS-Uninter)
    cd SGHSS-Uninter
    ```

2.  **Crie e ative o ambiente virtual:**
    * Linux/Mac:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\Activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o servidor:**
    ```bash
    python src/app.py
    ```
    *O servidor iniciará em `http://127.0.0.1:5000`*

## 📚 Documentação da API (Endpoints)

### 🔐 Autenticação

| Método | Rota | Descrição | Body (JSON) |
| :--- | :--- | :--- | :--- |
| **POST** | `/auth/register` | Cria novo usuário | `{"nome": "...", "email": "...", "password": "..."}` |
| **POST** | `/auth/login` | Gera Token JWT | `{"email": "...", "password": "..."}` |

### 🏥 Pacientes

| Método | Rota | Descrição | Header Obrigatório |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/patients` | Cadastra paciente | *Nenhum* |
| **GET** | `/api/v1/patients` | Lista pacientes | `Authorization: Bearer <token>` |

### 📅 Consultas (Agendamento)

| Método | Rota | Descrição | Header Obrigatório |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/appointments` | Agenda consulta | `Authorization: Bearer <token>` |
| **GET** | `/api/v1/appointments` | Lista consultas | `Authorization: Bearer <token>` |

## 📂 Estrutura do Projeto

```text
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
```

## ✒️ Autor

Desenvolvido por **Lucas MArtins Sorrentino** - RU: **4585828**.