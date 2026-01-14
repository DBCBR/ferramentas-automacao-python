from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configuração Fantasma
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")

# Configuração Padrão
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
print(">>> Robô iniciado em modo invisível...")

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
    # Dizemos ao robô: "Espere até 10 segundos pelo botão de Logout"
    # Se aparecer em 0.5s, ele segue. Se passar de 10s, ele dá erro.
    elemento_logout = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']"))
    )
    print("Login verificado com sucesso!")

except:
    print("Tempo esgotado. O login pode ter falhado ou a página demorou demais.")