import os
from dotenv import load_dotenv
from google import genai

# Carrega a chave
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

if not API_KEY:
    print("❌ Erro: Chave não encontrada no arquivo .env")
else:
    try:
        client = genai.Client(api_key=API_KEY)
        
        print("🔎 Buscando modelos disponíveis...\n")
        
        # Na nova versão, iteramos direto
        for model in client.models.list():
            # Imprime apenas o nome do modelo (ex: models/gemini-1.5-flash)
            print(f"✅ Modelo: {model.name}")
            
    except Exception as e:
        print(f"Erro ao listar: {e}")