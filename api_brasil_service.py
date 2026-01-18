import requests
import json

# --- ÁREA DE CONFIGURAÇÃO (Fácil de alterar) ---
# Se a API mudar de versão ou URL, alteramos apenas aqui.
BASE_URL = "https://brasilapi.com.br/api/cnpj/v1"


def consultar_cnpj(cnpj_alvo):
    # --- 1. HIGIENE DOS DADOS ---
    # Garante que só tenhamos números, mesmo que o main.py envie com pontos
    cnpj_limpo = cnpj_alvo.replace(".", "").replace("/", "").replace("-", "")

    # Montagem da URL usando a constante
    url = f"{BASE_URL}/{cnpj_limpo}"

    # Print mais discreto para não poluir o terminal
    print(f"Consultando: {cnpj_limpo}...", end=" ")

    try:
        # --- 2. SEGURANÇA (TIMEOUT) ---
        # Se a API demorar mais de 10s, o robô desiste para não travar seu PC
        resposta = requests.get(url, timeout=10)

        # --- 3. SUCESSO (200) ---
        if resposta.status_code == 200:
            dados = resposta.json()

            # PADRONIZAÇÃO: Cria um dicionário limpo para o Excel não quebrar
            empresa_formatada = {
                "cnpj": dados.get("cnpj", cnpj_limpo),
                "razao_social": dados.get("razao_social", "N/A"),
                "nome_fantasia": dados.get("nome_fantasia", ""),
                "uf": dados.get("uf", ""),
                "municipio": dados.get("municipio", ""),
                "logradouro": dados.get("logradouro", ""),
                "bairro": dados.get("bairro", ""),
                "cep": dados.get("cep", ""),
                "situacao": dados.get("descricao_situacao_cadastral", "N/A"),
                "data_abertura": dados.get("data_inicio_atividade", ""),
            }

            print("✅ Encontrada!")
            return empresa_formatada

        # --- 4. TRADUÇÃO DE ERROS (Humanizado) ---

        elif resposta.status_code == 429:
            print(
                "\n   ⏳ CALMA: O servidor pediu um tempo (Muitas consultas seguidas)."
            )
            print("      -> O robô vai pular este e tentar o próximo.")
            return None

        elif resposta.status_code == 404:
            print("\n   🔍 NÃO ENCONTRADO: Esse CNPJ não existe na Receita Federal.")
            return None

        elif resposta.status_code == 400:
            print("\n   ⚠️ CNPJ INVÁLIDO: O número parece estar errado ou incompleto.")
            return None

        elif resposta.status_code >= 500:
            print(
                "\n   ☁️ ERRO NO SERVIDOR: A BrasilAPI está fora do ar momentaneamente."
            )
            return None

        else:
            print(f"\n   ❌ Erro desconhecido: {resposta.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("\n   🐢 DEMOROU DEMAIS: A conexão caiu ou o site está lento.")
        return None

    except Exception as e:
        print(f"\n   ❌ ERRO TÉCNICO: {e}")
        return None


# --- ZONA DE TESTE RÁPIDO ---
if __name__ == "__main__":
    # Teste com um CNPJ válido para ver se funciona
    print(consultar_cnpj("00000000000191"))  # Banco do Brasil
