import pandas as pd
import requests
from bs4 import BeautifulSoup
import time  # Importante para não ser bloqueado

print(">>> INICIANDO O ROBÔ CRAWLER <<<")

# Lista Mestre (Acumula tudo)
TUDO = []

# Loop das Páginas (1 a 5)
for pag in range(1, 6):
    print(f"Lendo página {pag}...")  # Feedback visual para o usuário

    url = f"http://quotes.toscrape.com/page/{pag}/"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    citacoes = soup.find_all("div", class_="quote")

    # Lista Temporária (Só desta página)
    dados_pagina = []

    for frase in citacoes:
        texto = frase.find("span", class_="text").text
        autor = frase.find("small", class_="author").text

        dado = {"Citacao": texto, "Autor": autor}
        dados_pagina.append(dado)

    # Despeja o balde pequeno no balde grande
    TUDO.extend(dados_pagina)

    # Pausa de 2 segundos para não sobrecarregar o servidor
    time.sleep(2)

print("Consolidando dados...")
df = pd.DataFrame(TUDO)
df.to_excel("citacoes_famosas_completo.xlsx", index=False)

print(f"SUCESSO! {len(df)} citações salvas em 'citacoes_famosas_completo.xlsx'")
