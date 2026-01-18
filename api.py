from fastapi import FastAPI
from validadores import ValidadorCPF  # Importando SUA ferramenta!

# Criando a aplicação (o servidor)
app = FastAPI()


# Rota 1: A "Home Page" da API
@app.get("/")
def home():
    return {"mensagem": "API do David está online! 🚀"}


# Rota 2: O Validador de CPF
# O usuário vai acessar: /validar-cpf/12345678900
@app.get("/validar-cpf/{cpf}")
def verificar_cpf(cpf: str):
    # 1. Usamos a SUA classe para limpar e validar
    validador = ValidadorCPF(cpf)

    # Lembre-se: seu método .limpar() retorna None se for inválido
    resultado = validador.limpar()

    # 2. Resposta da API
    if resultado is None:
        return {
            "cpf_enviado": cpf,
            "status": "inválido",
            "mensagem": "CPF incorreto ou formato errado",
        }
    else:
        return {"cpf_enviado": cpf, "cpf_limpo": resultado, "status": "válido"}
