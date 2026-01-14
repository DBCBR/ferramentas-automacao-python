from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configuração Padrão
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# 1. Acessar site estável
navegador.get("http://quotes.toscrape.com/login")

# 2. Encontrar o campo de Login
campo_login = navegador.find_element(By.ID, "username")
campo_login.send_keys("admin")

# 3. Encontrar o campo de Senha
campo_senha = navegador.find_element(By.ID, "password")
campo_senha.send_keys("admin")

# 4. Encontrar o botão de Login e Clicar
btn_login = navegador.find_element(By.XPATH, "//input[@value='Login']")
btn_login.click()

# 5. Verificação visual
try:
    # Tente encontrar o botão
    navegador.find_element(By.XPATH, "//a[text()='Logout']")
    print("Login bem-sucedido! Acesso liberado.")
except:
    # Se der erro ao procurar (não achou), caímos aqui sem travar
    print("Falha no login. O botão Logout não apareceu.")