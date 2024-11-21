import os

os.system("cls")

dados = {1, 2, 3, 4, 5}

# Calcula media
media = sum(dados)/ len(dados)
print (f'Media: {media}')

# Calculando as diferenças entre cada valor e a média
diferencas = [x - media for x in dados]
print (diferencas)

# Elevando as diferenças ao quadrado
quadrados_diferencas = [x**2 for x in diferencas]
print (quadrados_diferencas)

# Média dos quadrados das diferenças
media_quadrados_diferencas = sum(quadrados_diferencas)/ len (quadrados_diferencas)
print (f'variância: {media_quadrados_diferencas}')

desvio_padrao = media_quadrados_diferencas ** 0.5 # raiz quadrada
print (desvio_padrao)