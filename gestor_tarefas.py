from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API do David está online! 🚀"}


class Tarefa(BaseModel):
    tarefa: str
    prazo: str
    realizada: bool = False


tarefas = []


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: Tarefa):
    tarefas.append(nova_tarefa)
    return nova_tarefa


@app.delete("/tarefas/{posicao}")
def deletar_tarefa(posicao: int):
    if posicao >= 0 and posicao < len(tarefas):
        tarefa_removida = tarefas.pop(posicao)
        return {"mensagem": "Tarefa removida com sucesso!", "tarefa": tarefa_removida}
    else:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.put("/tarefas/{posicao}")
def atualizar_tarefa(posicao: int, tarefa_atualizada: Tarefa):
    if posicao >= 0 and posicao < len(tarefas):
        tarefas[posicao] = tarefa_atualizada
        return {
            "mensagem": "Tarefa atualizada com sucesso!",
            "nova_tarefa": tarefa_atualizada,
        }
    else:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
