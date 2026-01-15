import time
import re
import os
import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import filedialog
from robo_investigador_cnpj import consultar_cnpj
from modulo_web import capturar_texto_da_web

# --- FASE 0: INTERAÇÃO COM O USUÁRIO (MENU) ---
print(">>> BEM-VINDO AO ROBÔ CAÇADOR DE CONTRATOS <<<")
print("Qual fonte de dados você deseja processar?")
print("[1] Arquivo do Computador (.txt, .xlsx, .csv)")
print("[2] Página da Web (URL)")

opcao = input("Digite o número da opção (1 ou 2): ").strip()

FONTE_DADOS = ""

if opcao == '1':
    print("📂 Abrindo janela de seleção de arquivo...")
    time.sleep(1)

    # Configuração do Tkinter (Janela Invisível)
    root = tk.Tk()
    root.withdraw()

    # Abre a caixa "Abrir Arquivo"
    FONTE_DADOS = filedialog.askopenfilename(
        title="Selecione o arquivo de contratos",
        filetypes=[("Todos os arquivos suportados",
                    "*.txt *.xlsx *.xls *.csv")]
    )

    if not FONTE_DADOS:
        print("❌ Operação cancelada pelo usuário.")
        exit()

    print(f"✅ Arquivo selecionado: {FONTE_DADOS}")

elif opcao == '2':
    FONTE_DADOS = input("🌐 Cole a URL do site aqui: ").strip()

    if not FONTE_DADOS.startswith("http"):
        print("❌ URL inválida. O link deve começar com http:// ou https://")
        exit()

else:
    print("❌ Opção inválida. Reinicie o robô.")
    exit()


# --- FASE 1: INGESTÃO DE DADOS (O ROBÔ TRABALHA) ---
print("-" * 30)
print(f"Processando fonte: {FONTE_DADOS}")

texto_bruto = ""

try:
    # A LÓGICA AGORA É UNIFICADA (IF / ELIF / ELSE)

    # 1. É WEB?
    if FONTE_DADOS.startswith('http'):
        print("Modo Detectado: WEB SCRAPING (SELENIUM)")
        texto_bruto = capturar_texto_da_web(FONTE_DADOS)

    # 2. É TXT?
    elif FONTE_DADOS.endswith('.txt'):
        print("Modo Detectado: LEITURA DE TEXTO")
        with open(FONTE_DADOS, 'r', encoding='utf-8') as arquivo:
            texto_bruto = arquivo.read()

    # 3. É EXCEL?
    elif FONTE_DADOS.endswith('.xlsx') or FONTE_DADOS.endswith('.xls'):
        print("Modo Detectado: LEITURA DE EXCEL")
        df_leitura = pd.read_excel(FONTE_DADOS)
        texto_bruto = df_leitura.to_string()

    # 4. É CSV?
    elif FONTE_DADOS.endswith('.csv'):
        print("Modo Detectado: LEITURA DE CSV")
        df_leitura = pd.read_csv(FONTE_DADOS)
        texto_bruto = df_leitura.to_string()

    else:
        print(f"❌ ERRO: O formato do arquivo '{FONTE_DADOS}' não é suportado.")
        exit()

except Exception as e:
    print(f"❌ Erro ao ler a fonte de dados: {e}")
    exit()

# --- DAQUI PARA BAIXO, TUDO IGUAL ---

# --- PASSO 2: MINERAR OS CNPJS ---
padrao = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"
lista_cnpjs_encontrados = re.findall(padrao, texto_bruto)

# Remove duplicatas
lista_cnpjs_encontrados = list(set(lista_cnpjs_encontrados))

print(f"Encontrei {len(lista_cnpjs_encontrados)} contratos únicos.")

# --- PASSO 3: ENRIQUECIMENTO DE DADOS ---
resultados_finais = []

for cnpj_sujo in lista_cnpjs_encontrados:
    print(f"\nProcessando CNPJ: {cnpj_sujo}")

    # Higiene
    cnpj_limpo = cnpj_sujo.replace(".", "").replace("/", "").replace("-", "")

    # API
    dados_empresa = consultar_cnpj(cnpj_limpo)

    if dados_empresa:
        resultados_finais.append(dados_empresa)

    print("Aguardando 3 segundos...")
    time.sleep(3)

# --- PASSO 4: PERSISTÊNCIA ---
print("-" * 30)

if resultados_finais:
    print("Salvando no banco de dados SQLite...")

    df = pd.DataFrame(resultados_finais)
    conn = sqlite3.connect('banco_contratos.db')

    df = df.astype(str)
    df.to_sql('fornecedores', conn, if_exists='append', index=False)
    conn.close()

    print("PROCESSO CONCLUÍDO COM SUCESSO! 🚀")
    print(df[['cnpj', 'razao_social', 'uf']].head())
else:
    print("Nenhum dado válido encontrado nesta fonte.")
