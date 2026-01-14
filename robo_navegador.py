from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configuração Padrão
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# 1. Acessar site estável
print("Acessando Python.org...")
navegador.get("https://www.python.org/")

# 2. Encontrar a Barra de Busca (Pelo ID exato)
# No Python.org, a barra sempre se chama 'id-search-field'
campo_busca = navegador.find_element(By.ID, "id-search-field")

# 3. Digitar
print("Digitando pesquisa...")
campo_busca.send_keys("pandas")

# 4. Encontrar o Botão 'GO' e CLICAR
# Em vez de dar Enter, vamos achar o botão físico e clicar nele.
# O ID do botão lá é 'submit'
botao_go = navegador.find_element(By.ID, "submit")
botao_go.click()

# 5. Verificação visual
print("Pesquisa enviada. Aguardando resultados...")
time.sleep(2)

# 6. Prova Real: Encontrar o primeiro link de resultado
# Lá os resultados ficam numa lista ordenada. Vamos pegar o primeiro título H3.
try:
    # Usando XPATH para pegar o primeiro H3 dentro da área de resultados
    resultado = navegador.find_element(By.XPATH, "//h3[contains(., 'Pandas')]")
    print(f"Sucesso! Encontrei o resultado: {resultado.text}")
except Exception as e:
    print("Erro: Não achei os resultados. O clique falhou?")

# Mantém aberto para você conferir
# navegador.quit()

'''Resumo dos Seletores:
🥇 ID (By.ID): É o CPF do elemento. É único e rápido. Se existir, USE. (Ex: id-search-field).

🥈 NAME (By.NAME): É o Nome. Pode ter homônimos, mas costuma ser seguro em formulários. (Ex: q).

🥉 XPATH (By.XPATH): É a "coordenada GPS". É poderoso e acha tudo, mas se o site mudar o layout, ele quebra. 
Use quando não tiver ID ou Name.
'''
