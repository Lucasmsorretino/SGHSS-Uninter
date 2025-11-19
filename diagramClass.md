classDiagram
    %% Classe Base de Usuário (Autenticação e Acesso)
    class User {
        +Integer id
        +String nome
        +String email
        -String password_hash
        +String role
        +set_password(password)
        +check_password(password) : bool
        +get_token() : String
    }

    %% Classe Paciente (Dados Clínicos e Pessoais)
    class Patient {
        +Integer id
        +String cpf
        +Date data_nascimento
        +String telefone
        +Integer user_id
        +to_dict() : JSON
        +get_history() : List
    }

    %% Classe Profissional (Dados do Médico/Enfermeiro)
    class Professional {
        +Integer id
        +String registro_profissional
        +String especialidade
        +Integer user_id
        +to_dict() : JSON
        +check_availability(date) : bool
    }

    %% Classe de Agendamento (Consulta)
    class Appointment {
        +Integer id
        +DateTime data_hora
        +String status
        +String tipo
        +Integer patient_id
        +Integer professional_id
        +String link_telemedicina
        +confirm() : void
        +cancel() : void
        +to_dict() : JSON
    }

    %% Relacionamentos
    User "1" -- "0..1" Professional : possui perfil >
    User "1" -- "0..1" Patient : possui cadastro >
    Patient "1" --> "*" Appointment : solicita >
    Professional "1" --> "*" Appointment : realiza >