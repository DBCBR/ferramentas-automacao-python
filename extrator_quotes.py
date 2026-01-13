"""
-------------------------------------------------------------------------
NOME: extrator_quotes.py
DESCRIÇÃO: 
    Crawler que navega pelo site quotes.toscrape.com, percorre múltiplas
    páginas (paginação), extrai citações e autores, e exporta para Excel.
    Inclui delay ético para não sobrecarregar o servidor.
-------------------------------------------------------------------------
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time # Importante para o delay (ética do robô)

def main():
    print(">>> INICIANDO O ROBÔ CRAWLER <<<")

    # Lista Mestre (Acumula os dados de TODAS as páginas)
    dados_totais = []

    # Loop das Páginas (de 1 até 5)
    for pag in range(1, 6):
        print(f"Lendo página {pag}...") 
        
        # 1. Construção da URL Dinâmica
        url = f"http://quotes.toscrape.com/page/{pag}/"
        
        # 2. Requisição (GET)
        try:
            resposta = requests.get(url)
            # O soup transforma o HTML texto em objetos Python
            soup = BeautifulSoup(resposta.text, 'html.parser')
            
            # 3. Busca dos Containers (Caixas das citações)
            citacoes = soup.find_all('div', class_='quote')
            
            # 4. Extração dos dados desta página
            for frase in citacoes:
                texto = frase.find('span', class_='text').text
                autor = frase.find('small', class_='author').text
                
                # Cria o dicionário e adiciona na lista mestre
                dado = {"Citacao": texto, "Autor": autor}
                dados_totais.append(dado)
            
            # 5. Delay Ético (Espera 2 segundos antes de ir para a próxima página)
            time.sleep(2)
            
        except Exception as e:
            print(f"Erro ao ler página {pag}: {e}")

    # 6. Consolidação e Exportação (Fora do Loop)
    print("Consolidando dados...")
    
    if dados_totais:
        df = pd.DataFrame(dados_totais)
        nome_arquivo = "citacoes_famosas_completo.xlsx"
        df.to_excel(nome_arquivo, index=False)
        print(f"SUCESSO! {len(df)} citações salvas em '{nome_arquivo}'")
    else:
        print("Nenhum dado foi extraído.")

if __name__ == "__main__":
    main()