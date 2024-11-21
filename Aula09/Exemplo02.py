import pandas as pd
import numpy as np
import os

os.system("cls")

dados = pd.Series([2, 4, 6, 8, 10])

# Transforma dados em array
conjunto_dados = np.array(dados)
print(f'Conjunto de dados: {conjunto_dados}')

# Calculando a média
print(f'Média: {conjunto_dados.mean()}')

# Calculando a variância
print(f'Variância: {np.var(conjunto_dados)}')

# Calculando o desvio padrão
print(f'Desvio padrão: {np.std(conjunto_dados)}')

# Calculando a distância entre variância e média
print(f'Distância entre variância e média: {np.var(conjunto_dados) / (conjunto_dados.mean()**2)}')

# Calculando o coeficiente de variação
print(f'Coeficiente de variação: {(np.std(conjunto_dados) / conjunto_dados.mean()) * 100:.2f}%')

