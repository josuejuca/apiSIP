from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import urllib.parse
from models import Extension, ApagarExtension, ExtensionCreate

# Configurações de conexão com o banco de dados
user = "pbx"
password = urllib.parse.quote_plus("pbx@2023")  # codifica a senha
host = "192.168.1.200"
database = "fusionpbx"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Função para verificar a conexão com o banco de dados
def check_db_connection():
    try:
        # Tenta criar uma sessão no banco de dados
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))  # Use text() para criar uma expressão SQL textual
        return True  # Retorna True se a conexão for bem-sucedida
    except OperationalError:
        return False  # Retorna False se a conexão falhar

# Rota para verificar o estado da conexão com o banco de dados
@app.get("/" , tags=["STATUS"])
async def db_status():
    """
    Rota verifica se a conexão com o banco de dados está ativa.

    Caso não esteja entre em contato.
    """
    if check_db_connection():
        return {"db": "Online"}  # Se a conexão for bem-sucedida, retorne {"db": "Online"}
    else:
        return {"db": "offline"}  # Se a conexão falhar, retorne {"db": "offline"}

# Nova rota para buscar todas as extensões
@app.get("/extensions" , tags=["BASE"])
async def get_extensions():
    with SessionLocal() as session:
        # Busca todas as extensões
        extensions = session.query(Extension).all()

        # Converte os resultados em dicionários
        results = [extension.__dict__ for extension in extensions]

        # Retorna os resultados como JSON
        return results
    
    
# Rota para excluir um usuário com base no extension_uuid
@app.delete("/delete-user/{extension_uuid}" , tags=["BASE"])
async def delete_user(extension_uuid: str):
    db = SessionLocal()
    user = db.query(ApagarExtension).filter(ApagarExtension.extension_uuid == extension_uuid).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "Usuário excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
# Rota para editar um usuário com base no extension_uuid
@app.put("/edit-user/{extension_uuid}", tags=["BASE"])
async def edit_user(extension_uuid: str, extension_update: dict):
    query = text(
        "UPDATE v_extensions "
        "SET extension = :extension, "
        "    number_alias = :number_alias, "
        "    password = :password, "
        "    accountcode = :accountcode, "
        "    effective_caller_id_name = :effective_caller_id_name, "
        "    effective_caller_id_number = :effective_caller_id_number, "
        "    outbound_caller_id_name = :outbound_caller_id_name, "
        "    outbound_caller_id_number = :outbound_caller_id_number "
        "WHERE extension_uuid = :extension_uuid"
    )
    with engine.connect() as connection:
        try:
            connection.execute(
                query,
                extension_uuid=extension_uuid,
                **extension_update
            )
            return {"message": "Usuário atualizado com sucesso", "extension_uuid": extension_uuid}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))