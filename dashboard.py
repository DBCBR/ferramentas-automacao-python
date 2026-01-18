import sqlite3
import pandas as pd
import logging
import matplotlib.pyplot as plt  # <--- O PINTOR CHEGOU

logging.basicConfig(level=logging.INFO, format="%(message)s", encoding="utf-8")


def gerar_dashboard():
    print("📊 INICIANDO ANÁLISE DE DADOS...")

    try:
        conn = sqlite3.connect("dados/banco_contratos.db")
        query = "SELECT * FROM fornecedores"
        df = pd.read_sql(query, conn)
        conn.close()
    except Exception as e:
        logging.error(f"Erro ao ler banco de dados: {e}")
        return

    if df.empty:
        print("⚠️ O banco de dados está vazio.")
        return

    # --- ESTATÍSTICAS (TEXTO) ---
    print(f"\n🔹 Total de Empresas: {len(df)}")

    contagem_situacao = df["situacao"].value_counts()
    print("\n🔹 Situação Cadastral:")
    print(contagem_situacao)

    # --- GRÁFICOS (VISUAL) ---
    print("\n🎨 Gerando gráfico visual...")

    # 1. Definir o tamanho da figura (10 de largura, 6 de altura)
    plt.figure(figsize=(10, 6))

    # 2. Criar o gráfico de barras
    # Eixo X = Nomes (Ativa, Baixada)
    # Eixo Y = Quantidade
    # color = cor das barras
    contagem_situacao.plot(kind="bar", color="skyblue", edgecolor="black")

    # 3. Enfeitar o gráfico
    plt.title("Situação Cadastral dos Fornecedores", fontsize=16)
    plt.xlabel("Situação", fontsize=12)
    plt.ylabel("Quantidade", fontsize=12)
    plt.xticks(rotation=0)  # Deixar o texto do eixo X reto
    plt.grid(axis="y", linestyle="--", alpha=0.7)  # Linhas de grade

    # 4. Mostrar na tela
    print(
        "A janela do gráfico deve abrir agora. (Feche a janela para encerrar o script)"
    )
    plt.show()


if __name__ == "__main__":
    gerar_dashboard()
