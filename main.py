import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dados = pd.read_csv("slr12.csv", sep=";")
print(f"Formato original dos dados: {dados.shape}")

Q1 = dados.quantile(0.25)
Q3 = dados.quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"\nLimite Inferior:\n{limite_inferior}")
print(f"Limite Superior:\n{limite_superior}")


dados = dados[~((dados < limite_inferior) | (dados > limite_superior)).any(axis=1)]
print(f"Formato após a remoção de outliers: {dados.shape}")


X = dados[['FrqAnual']]
y = dados['CusInic']

modelo = LinearRegression()
modelo.fit(X, y)


plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, modelo.predict(X), color='red', label='Regressão Linear')
plt.xlabel("Taxa Anual")
plt.ylabel("Custo Inicial")
plt.title("Gráfico de Dispersão com Regressão Linear")
plt.legend()
plt.show()

# 6. Previsão de uma Nova Franquia
novo_valor = float(input("\nTaxa Anual da Franquia: "))

dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
prev = modelo.predict(dados_novo_valor)

print(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")