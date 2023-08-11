import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('data/base_corrigida.csv')


## _________________________________________________________
col = ['municipio', 'classificacao']
relatorio = df.loc[:,col].groupby(['municipio','classificacao',]).size().reset_index()

## _________________________________________________________
colunas = ['Municipio', 'Classificação', 'Contagem']
relatorio.columns = colunas
relatorio

## _________________________________________________________
fig = px.bar(relatorio, x='Municipio', y='Contagem', color='Classificação', barmode='group',
             text='Contagem')  # Usar a coluna 'Contagem' para os rótulos dos dados



# Ativar a exibição dos valores nas barras
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')  # Posição e formato dos rótulos

app.layout = html.Div( children=[
    html.H1(children='Dashboard'),

    html.Div(children='Análisando dados das propriedades com coordenadas incorretas'),
    dcc.Graph(
        id='grafico_bar',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)