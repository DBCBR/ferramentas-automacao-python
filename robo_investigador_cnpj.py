import requests
import json

def consultar_cnpj(cnpj_alvo):
    # --- HIGIENE DOS DADOS (O Robô limpa antes de enviar) ---
    cnpj_limpo = cnpj_alvo.replace(".", "").replace("/", "").replace("-", "")
    
    # Agora usamos o limpo na URL
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    
    print(f"Consultando CNPJ: {cnpj_limpo}...")
    
    resposta = requests.get(url)
    
    status_map = {
        2: "Ativa",
        3: "Suspensa",
        4: "Inapta",
        8: "Baixada"
    }
    
    if resposta.status_code == 200:
        dados = resposta.json()
        print("Consulta realizada com sucesso!")
        print(f"Nome Fantasia: {dados.get('fantasia', 'N/A')}")
        print(f"Razão Social: {dados.get('razao_social', 'N/A')}")
        situacao_cadastral = dados.get('situacao_cadastral', 'N/A')
        situacao_texto = status_map.get(situacao_cadastral, 'Desconhecida')
        print(f"Situação Cadastral: {situacao_texto}")
        print(f"Data de Abertura: {dados.get('data_abertura', 'N/A')}")
        print(f"Atividade Principal: {dados.get('atividade_principal', [{'text': 'N/A'}])[0]['text']}")
        print(f"Endereço: {dados.get('logradouro', 'N/A')}, {dados.get('numero', 'N/A')} - {dados.get('bairro', 'N/A')}, {dados.get('municipio', 'N/A')} - {dados.get('uf', 'N/A')}, CEP: {dados.get('cep', 'N/A')}")
        return dados
    else:
        print(f"Erro ao consultar CNPJ: {resposta.status_code}")
        return None

if __name__ == "__main__":
    cnpj_teste = "57.929.932/0001-30"
    consultar_cnpj(cnpj_teste)
