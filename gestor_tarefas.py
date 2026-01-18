from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./tarefas.db"

# connect_args={"check_same_thread": False} é necessário para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# --- A TABELA (MODELO) ---
class TarefaDB(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    tarefa = Column(String)
    prazo = Column(String)
    realizada = Column(Boolean, default=False)


# Cria as tabelas no arquivo
Base.metadata.create_all(bind=engine)


# --- DEPENDÊNCIA (Para pegar o banco a cada pedido) ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- O MOLDE (PYDANTIC) ---
class Tarefa(BaseModel):
    tarefa: str
    prazo: str
    realizada: bool = False


# --- ROTAS ---


@app.get("/")
def home():
    return {"mensagem": "API do David com Banco de Dados! 🚀"}


# ROTA 1: CRIAR (POST) - Agora salvando no SQLite
@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: Tarefa, db: Session = Depends(get_db)):
    # Transforma o Pydantic em Objeto de Banco
    tarefa_para_banco = TarefaDB(**nova_tarefa.dict())

    db.add(tarefa_para_banco)
    db.commit()
    db.refresh(tarefa_para_banco)
    return tarefa_para_banco


# ROTA 2: LER (GET) - Agora lendo do SQLite
@app.get("/tarefas")
def listar_tarefas(db: Session = Depends(get_db)):
    # SELECT * FROM tarefas
    return db.query(TarefaDB).all()


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(
    tarefa_id: int, tarefa_atualizada: Tarefa, db: Session = Depends(get_db)
):
    tarefa_no_banco = db.query(TarefaDB).filter(TarefaDB.id == tarefa_id).first()

    if not tarefa_no_banco:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa_no_banco.tarefa = tarefa_atualizada.tarefa
    tarefa_no_banco.prazo = tarefa_atualizada.prazo
    tarefa_no_banco.realizada = tarefa_atualizada.realizada

    db.commit()
    db.refresh(tarefa_no_banco)
    return tarefa_no_banco


@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa_no_banco = db.query(TarefaDB).filter(TarefaDB.id == tarefa_id).first()

    if not tarefa_no_banco:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(tarefa_no_banco)
    db.commit()
    return
