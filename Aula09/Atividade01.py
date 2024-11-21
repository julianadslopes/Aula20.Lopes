# Calcular a variância entre a idade de 5 pessoas de uma mesma família (5, 10, 12, 35, 38)
import pandas as pd
import numpy as np
import os 

os.system ("cls")
dados = pd.Series ([5, 10, 12, 35, 38])
conjunto_dados = np.array (dados)
print (f'Conjunto de dados {conjunto_dados}')

# Transforma dados em array
conjunto_dados = np.array(dados)
print (f'Conjunto de dados {conjunto_dados}')

# Calculando média
media = conjunto_dados.mean()
print (f'Média: {media}')

# Calculando a variância
variancia = np.var(conjunto_dados)
print (f'Variância: {variancia}')

# Calculando o desvio padrão
desvio_padrao = np.std(conjunto_dados)
print (f'Desvio padrão: {desvio_padrao}')

distancia_var_media = variancia / (media**2)
print (f'Distância entre variância e média: {distancia_var_media}')

coef_variacao = (desvio_padrao/media)*100
print (f'Coeficiente de variação: {coef_variacao}')

# Cálculo para as amostras

print("\n******Cálculo para amostras*******")
variancia_amostral = np.var(dados, ddof=1)  # ddof=1 faz o cálculo para amostras
print(f' Variância amostral: {variancia_amostral}')

desvio_padrao_amostral = np.std(dados, ddof=1)
print (f' Desvio Padrão entre as idades {desvio_padrao_amostral}')