# ------------------------------------------------------------------------------
# --- CONTROLE FINANCEIRO PESSOAL COM FASTAPI, SQLALCHEMY E IA (ATUALIZADO) ---
# ------------------------------------------------------------------------------
import os
import json
from dotenv import load_dotenv
from google import genai 

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session, declarative_base

app = FastAPI()

# ------------------------------------------------------------------------------
# --- CONFIGURAÇÃO DA IA (GEMINI 2.5) ---
# ------------------------------------------------------------------------------

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    print("⚠️ AVISO: A chave GENAI_API_KEY não foi encontrada no arquivo .env!")
    client = None
else:
    # NA NOVA VERSÃO: Criamos um "Cliente" em vez de usar .configure()
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Erro ao configurar IA: {e}")
        client = None

# ------------------------------------------------------------------------------
# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
# ------------------------------------------------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./financas.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------------------------------------------------------------------
# --- A TABELA (MODELO) ---
# ------------------------------------------------------------------------------

class FinancasDB(Base):
    __tablename__ = "financas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    tipo = Column(String)
    valor = Column(Float)

Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------------------------
# --- DEPENDÊNCIA ---
# ------------------------------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------------------------
# --- MOLDE (PYDANTIC) ---
# ------------------------------------------------------------------------------

class Financa(BaseModel):
    titulo: str
    tipo: str
    valor: float

# ------------------------------------------------------------------------------
# --- ROTAS ---
# ------------------------------------------------------------------------------

@app.get("/")
def home():
    return {"mensagem": "Controle Financeiro Pessoal! 💰"}

# --- ROTA DE IA + DB ---
@app.post("/analisar-transacao-ia")
def analisar_transacao_com_ia(texto_usuario: str, db: Session = Depends(get_db)):
    """
    1. Usa IA para entender o texto.
    2. Salva automaticamente no Banco de Dados.
    """
    
    # Validação de segurança
    if not client:
        raise HTTPException(status_code=500, detail="Serviço de IA não configurado.")

    # 1. O Prompt para a IA
    prompt = f"""
    Aja como um assistente financeiro. Analise a frase: '{texto_usuario}'
    Extraia as informações para um JSON com os campos:
    - titulo (resumo curto da transação)
    - tipo (deve ser estritamente 'receita' ou 'despesa')
    - valor (número float, positivo)
    
    Responda APENAS o JSON válido.
    """
    
    try:
        # 2. Chamada para o Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", # O modelo que funcionou para você
            contents=prompt
        )
        
        # 3. Limpeza e Conversão
        texto_limpo = response.text.replace("```json", "").replace("```", "").strip()
        dados_estruturados = json.loads(texto_limpo)
        
        # 4. AQUI ACONTECE A MÁGICA DA GRAVAÇÃO (O código novo)
        nova_transacao = FinancasDB(
            titulo=dados_estruturados["titulo"],
            tipo=dados_estruturados["tipo"],
            valor=dados_estruturados["valor"]
        )
        
        db.add(nova_transacao)
        db.commit()          # Salva de verdade
        db.refresh(nova_transacao) # Pega o ID gerado
        
        return {
            "mensagem": "Transação analisada e salva com sucesso! 🤖💾",
            "dados": nova_transacao
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {str(e)}")


@app.post("/financas", status_code=201)
def criar_financa(nova_financa: Financa, db: Session = Depends(get_db)):
    financa_para_banco = FinancasDB(**nova_financa.dict())
    db.add(financa_para_banco)
    db.commit()
    db.refresh(financa_para_banco)
    return financa_para_banco

@app.get("/financas")
def listar_financas(db: Session = Depends(get_db)):
    lista_transacoes = db.query(FinancasDB).all()
    saldo = 0.0
    for item in lista_transacoes:
        if item.tipo.lower() == "receita":
            saldo += item.valor
        elif item.tipo.lower() == "despesa":
            saldo -= item.valor
    return {"saldo_atual": f"{saldo:.2f}", "extrato": lista_transacoes}

@app.put("/financas/{financa_id}")
def atualizar_financa(financa_id: int, financa_atualizada: Financa, db: Session = Depends(get_db)):
    financa_no_banco = db.query(FinancasDB).filter(FinancasDB.id == financa_id).first()
    if not financa_no_banco:
        raise HTTPException(status_code=404, detail="Finança não encontrada!")
    financa_no_banco.titulo = financa_atualizada.titulo
    financa_no_banco.tipo = financa_atualizada.tipo
    financa_no_banco.valor = financa_atualizada.valor
    db.commit()
    db.refresh(financa_no_banco)
    return financa_no_banco

@app.delete("/financas/{financa_id}", status_code=204)
def deletar_financa(financa_id: int, db: Session = Depends(get_db)):
    financa_no_banco = db.query(FinancasDB).filter(FinancasDB.id == financa_id).first()
    if not financa_no_banco:
        raise HTTPException(status_code=404, detail="Finança não encontrada!")
    db.delete(financa_no_banco)
    db.commit()
    return