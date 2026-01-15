import pandas as pd
import glob

# --- CONFIGURAÇÃO ---
nome_saida = "Relatorio_Executivo_Formatado.xlsx"

print(">>> INICIANDO CONSOLIDAÇÃO COM FORMATAÇÃO <<<")

# 1. Busca os arquivos (EXTRACT)
arquivos = glob.glob("*.xlsx") # Certifique-se que o padrão bate com seus arquivos

lista_dfs = []

# 2. Loop de Leitura (TRANSFORM)
for arq in arquivos:
    try:
        # Lê o Excel
        dt = pd.read_excel(arq)
        
        # Cria a coluna de rastreabilidade (De onde veio esse dado?)
        dt["Origem"] = arq 
        
        lista_dfs.append(dt)
        print(f"-> Lido: {arq}")
    except Exception as e:
        print(f"ERRO ao ler {arq}: {e}")

if not lista_dfs:
    print("Nenhum arquivo encontrado. Verifique o padrão de nome.")
    exit()

# Junta tudo numa tabela só
df_final = pd.concat(lista_dfs)

# 3. Exportação com Design (LOAD)
print("\nGerando Excel formatado...")

# A MÁGICA ACONTECE AQUI:
# Usamos o 'ExcelWriter' para ter acesso às propriedades visuais da planilha
with pd.ExcelWriter(nome_saida, engine='openpyxl') as writer:
    
    # Passo A: Salva os dados SEM o índice (index=False mata a coluna de números 0,1,2)
    df_final.to_excel(writer, index=False, sheet_name='Dados_Consolidados')
    
    # Passo B: Pega o objeto da planilha para podermos mexer na largura
    worksheet = writer.sheets['Dados_Consolidados']
    
    # Passo C: Loop para ajustar a largura de cada coluna automaticamente
    for i, coluna in enumerate(df_final.columns):
        # Calcula o tamanho do maior texto nessa coluna (ou o tamanho do título, o que for maior)
        # converte para string (.astype(str)) para evitar erro com números
        largura_maxima = max(
            df_final[coluna].astype(str).map(len).max(),
            len(coluna)
        )
        
        # Define a largura com uma folga (+2 caracteres)
        largura_ajustada = largura_maxima + 2
        
        # Descobre a letra da coluna (A, B, C...) baseado no número (0, 1, 2)
        letra_coluna = chr(65 + i) 
        
        # Aplica a largura na planilha
        worksheet.column_dimensions[letra_coluna].width = largura_ajustada

print(f"SUCESSO! Arquivo '{nome_saida}' gerado e formatado.")