from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import urllib.parse

# Configurações de conexão com o banco de dados
user = "pbx"
password = urllib.parse.quote_plus("pbx@2023")  # codifica a senha
host = "192.168.1.200"
database = "fusionpbx"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

try:
    # Cria uma engine de banco de dados
    engine = create_engine(SQLALCHEMY_DATABASE_URL, client_encoding='utf8')

    # Tenta conectar ao banco de dados
    with engine.connect() as connection:
        # Cria um objeto de texto SQL
        statement = text("SELECT 1")

        # Executa a consulta
        result = connection.execute(statement)

        # Verifica se a consulta foi bem-sucedida
        if result.fetchone()[0] == 1:
            print("Conexao bem-sucedida")
        else:
            print("Erro ao executar a consulta")
except OperationalError as e:
    print(f"Erro de conexao com o banco de dados: {e}")
