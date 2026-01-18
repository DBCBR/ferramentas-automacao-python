import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. DADOS DE TREINO (O Passado)
# Imagine que coletamos isso de perfis reais no Upwork
# [Anos de Experiência]
X_treino = np.array([[1], [2], [3], [4], [5], [6], [8], [10]]) 

# [Valor Cobrado por Hora em Dólares]
y_treino = np.array([15, 20, 25, 30, 35, 40, 50, 60])

print("🤖 CÉREBRO: Inicializando modelo de Regressão Linear...")

# 2. A MÁGICA (Treinamento)
# Aqui a IA tenta achar a fórmula matemática que conecta X a Y
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

print("✅ CÉREBRO: Aprendizado concluído!")

# 3. O TESTE (Prevendo o Futuro)
# Vamos pedir para a IA prever o salário de alguém com 7 anos (que não está na lista original)
anos_experiencia = np.array([[7]])
previsao = modelo.predict(anos_experiencia)

print(f"\n🔮 PREVISÃO:")
print(f"Para um dev com 7 anos de experiência, a IA sugere cobrar: ${previsao[0]:.2f}/hora")

# 4. VISUALIZANDO O "PENSAMENTO" DA IA
plt.scatter(X_treino, y_treino, color='blue', label='Dados Reais') # Pontos reais
plt.plot(X_treino, modelo.predict(X_treino), color='red', label='Linha da IA') # O que a IA aprendeu
plt.scatter(anos_experiencia, previsao, color='green', s=100, label='Previsão (7 anos)') # O chute da IA

plt.title('Regressão Linear: Experiência vs. Salário')
plt.xlabel('Anos de Experiência')
plt.ylabel('Valor Hora ($)')
plt.legend()
plt.grid(True)
plt.show()