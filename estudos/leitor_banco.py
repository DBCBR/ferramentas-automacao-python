import pandas as pd
import sqlite3

# Conexão
conn = sqlite3.connect("banco_contratos.db")

# A mágica: Lê SQL e transforma em DataFrame numa linha só
df_banco = pd.read_sql("SELECT * FROM citacoes", conn)

# Fecha conexão
conn.close()

# Mostra como se fosse Excel
print(df_banco.head())
