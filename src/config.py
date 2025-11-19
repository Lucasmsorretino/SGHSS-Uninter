import os

# Configurações básicas da aplicação
class Config:
    # A chave secreta é crucial para segurança de sessões e cookies (Requisito Não Funcional - Segurança)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_padrao_muito_longa_e_segura'
    
    # Configuração do SQLite, apontando para o arquivo no diretório raiz
    # O SQLITE_DATABASE_URI utiliza o SQLite, conforme sua escolha.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sghss.db')
    
    # Desabilita o aviso de modificação do track, que polui o console
    SQLALCHEMY_TRACK_MODIFICATIONS = False