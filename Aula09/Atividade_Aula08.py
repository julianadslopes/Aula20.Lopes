import os
import pandas as pd
import numpy as np

os.system ("cls")


try:
    print('\n Obtendo dados...')

    # OBTENDO CSV: VENDAS 2017 MIRANDA
    df_dados_vendas = pd.read_csv('tb_Vendas2017_Miranda.csv', sep=';', encoding='iso-8859-1')

    # Delimitando as variáveis - dataframe Vendas:
    df_vendas = df_dados_vendas[['Numero da Venda', 'ID Produto', 'ID Cliente', 'Quantidade Vendida']]
    print(df_vendas.head())

    # OBTENDO CSV: CADSTRO DE PRODUTOS 2017 MIRANDA
    df_dados_produtos = pd.read_csv('tb_CadastroProdutos2017_Miranda.csv', sep=';', encoding='utf-8')
    print(df_dados_produtos.head())
    
    # Delimitando as variáveis - dataframe de Produtos:
    df_produtos = df_dados_produtos[['Nome da Marca', 'Categoria', 'Preco Unitario', 'ID Produto']]
    print(df_produtos.head())
    
    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    print('\n Preparando os dataframes')

    # # Converter 'ID Produto' em ambos os DataFrames para string usando .loc
    df_produtos.loc[:, 'Preco Unitario'] = df_produtos['Preco Unitario'].str.replace(',', '.').astype(float)

    # Configurando o formato de exibição de números decimais p/ 2 casas decimais
    pd.options.display.float_format = '{:.2f}'.format

    # Aplicando o Merge nos dataframes df_vendas e df_produtos
    # Usando a coluna 'ID Produto' como o compo em comum nos dois dataframe
    # Método pd.merge()
    df_produtos_vendidos = pd.merge(df_vendas, df_produtos, on='ID Produto')

    # Criando a coluna 'Valor Total' 
    # Calculando o 'Valor Total' = Preco Unitario * Quantidade Vendida
    df_produtos_vendidos['Valor Total'] = (df_produtos_vendidos['Quantidade Vendida'] * df_produtos_vendidos['Preco Unitario'])

    # Agrupando por ID ou Categoria do Produto
    # No agrupamento, algumas (atributos ou variáveis) "ou seja, COLUNAS" de cada registro, podem desaparecer.
    # Isso é umm efeito colateral do agrupamento. Exemplo: Em um agrupamento por Categoria, o ID Produto pode desaparecer.
    # O método .gg() "agregação" é necessário para calcular a soma da 'Quantidade Vendida' e 'Valor Total' para cada categoria.
    # No caso do 'ID Produto', não faz sentido calcular a soma de cada ID. O ID é uma variável Qualitativa.
    # No entanto, poderia fazer sentido contarmos quantos IDs existem em cada categoria. 
    # Para isso, usariamos o método .count() em vez de .sum().
    # Neste caso obteríamos o número de produtos vendidos em cada categoria.
    df_produtos_vendidos = df_produtos_vendidos.groupby('Categoria').agg({
        'Quantidade Vendida': 'sum',
        'Valor Total': 'sum'
    }).reset_index()

    # Exibindo as primeiras linhas do DataFrame resultante
    print(df_produtos_vendidos.head(20).sort_values(by='Valor Total', ascending=False))

except ImportError as e:
    print(f'Erro ao formatar e juntar os dataframes: {e}')
    exit()


try:
    print("\n Analisando...")
    array_produtos_vendidos = np.array(df_produtos_vendidos["Valor Total"])

    media_produtos_vendidos = np.mean (array_produtos_vendidos)
    mediana_produtos_vendidos = np.median (array_produtos_vendidos)
    distancia = abs ((media_produtos_vendidos-mediana_produtos_vendidos)/mediana_produtos_vendidos)*100

    print("\n Medidas de tendência Central: ")
    print(f' Média: {media_produtos_vendidos:.2f}')
    print(f' Mediana: {mediana_produtos_vendidos:.2f}')
    print(f' Distância (entre a Média e a Mediana): {distancia:.2f}')

    # Medidas de Dispersão
    maximo = np.max(array_produtos_vendidos)
    minimo = np.min(array_produtos_vendidos)
    amplitude = maximo - minimo

    print("\n Medidas de Dispersão: ")
    print('Mínimo:', minimo)
    print('Máximo: ', maximo)
    print(f'Amplitude: {amplitude}')

    # Quartis - Uso Método Weibull
    q1 = np.quantile(array_produtos_vendidos, 0.25, method="weibull")
    q2 = np.quantile(array_produtos_vendidos, 0.50, method="weibull")
    q3 = np.quantile(array_produtos_vendidos, 0.75, method="weibull")
    iqr = q3-q1
    lim_superior = q3 + (1.5*iqr)
    lim_inferior = q1 - (1.5*iqr)

    print(f' Limite Inferior: {lim_inferior}')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')
    print(f'IQR: {iqr}')
    print(f' Limite Superior: {lim_superior}')

# Filtrando os outliers
    # Inferiores
    df_produtos_vendidos_outliers_inferiores = df_produtos_vendidos[df_produtos_vendidos["Valor Total"]< lim_inferior]
    # Superiores
    df_produtos_vendidos_outliers_superiores = df_produtos_vendidos[df_produtos_vendidos["Valor Total"]> lim_superior]

    print ('\n Produtos com outliers inferiores: ')    
    if len(df_produtos_vendidos_outliers_inferiores)==0:
        print ("Não existem outliers inferiores!")
    else:
        print (df_produtos_vendidos_outliers_inferiores.sort_values(by='Valor Total', ascending=True))
    
    print ('\n Produtos com outliers superiores: ')
    if len(df_produtos_vendidos_outliers_superiores)==0:
        print ("Não existem outliers superiores!")
    else:
        print (df_produtos_vendidos_outliers_superiores.sort_values(by='Valor Total', ascending=False))

except Exception as e:
    print (f'Erro ao obter dados: {e}')
    exit()
    
    
try:
    print("\n Medidas de Dispersão...")
# Calculando a variância
    variancia = np.var(array_produtos_vendidos)
    print (f'Variância: {variancia:.2f}')

# Calculando o desvio padrão
    desvio_padrao = np.std(array_produtos_vendidos)
    print (f'Desvio padrão: {desvio_padrao:.2f}')

    distancia_var_media = variancia / (media_produtos_vendidos**2)
    print (f'Distância entre variância e média: {distancia_var_media:.2f}')

    coef_variacao = (desvio_padrao/media_produtos_vendidos)*100
    print (f'Coeficiente de variação: {coef_variacao:.2f}')
    
except Exception as e:
    print (f'Erro ao obter dados: {e}')
    exit()


try:
    print("\n Medidas de Dispersão Amostrais...")
# Calculando a variância
    variancia_amostral = np.var(array_produtos_vendidos, ddof=1)
    print (f'Variância: {variancia_amostral:.2f}')

# Calculando o desvio padrão
    desvio_padrao_amostral = np.std(array_produtos_vendidos, ddof=1)
    print (f'Desvio padrão: {desvio_padrao_amostral:.2f}')
    
except Exception as e:
    print (f'Erro ao obter dados: {e}')
    exit()    
