```mermaid
useCaseDiagram
    left to right direction
    actor "Paciente" as Patient
    actor "Profissional de Saúde" as Professional
    actor "Administrador" as Admin

    package "SGHSS - Sistema de Gestão Hospitalar" {
        
        %% Módulo de Acesso (Implementado)
        usecase "Realizar Login / Autenticação" as UC1
        
        %% Módulo do Paciente (Implementado)
        usecase "Cadastrar-se (Autoatendimento)" as UC2
        usecase "Agendar Consulta (Presencial/Tele)" as UC3
        usecase "Visualizar Histórico de Agendamentos" as UC4
        
        %% Módulo do Profissional (Implementado Parcialmente)
        usecase "Listar Pacientes" as UC5
        usecase "Visualizar Agenda Diária" as UC6
        
        %% Módulo Administrativo (Apenas Modelado - Não Codificado)
        usecase "Gerenciar Profissionais e Usuários" as UC7
        usecase "Gerenciar Leitos e Insumos" as UC8
    }

    %% Relacionamentos
    Patient --> UC1
    Patient --> UC2
    Patient --> UC3
    Patient --> UC4

    Professional --> UC1
    Professional --> UC5
    Professional --> UC6

    Admin --> UC1
    Admin --> UC7
    Admin --> UC8
```