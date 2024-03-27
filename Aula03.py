import pandas as pd
import plotly_express as px

dados = pd.read_excel('vendas.xlsx')

# (análise exploratória) verificando inicio e fim da tabela
print(dados.head())
print(dados.tail())

# estatística de preço
print(dados.preco.describe().to_frame())

# análises: venda por loja, por cidade, por forma de pagamento, faturamento por loja, estado e cidade
print(dados.loja.value_counts().to_frame())
print(dados.cidade.value_counts().to_frame())
print(dados.forma_pagamento.value_counts().to_frame())
print(dados.groupby(['loja','estado','cidade']).preco.sum().to_frame())

# Salvando os dados em um arquivo Excel
dados.to_excel('teste_planilha.xlsx', index=False)

# Criando e salvando histogramas para cada coluna especificada
colunas = ['loja', 'cidade', 'estado', 'regiao', 'local_consumo']
for coluna in colunas:
    grafico = px.histogram(dados,
                           x=coluna,
                           y='preco',
                           text_auto=True,
                           title=f'Faturamento por {coluna}',
                           color='forma_pagamento')
    print(grafico.show())
    #criando arquivo HTML
    grafico.write_html(f'Gráfico-{coluna}.html')