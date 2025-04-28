import pandas as pd
import streamlit as st

# Carregar CSV
@st.cache_data
def carregar_dados():
    return pd.read_csv('produtos.csv', delimiter=';', encoding='utf-8')  # Ajuste o delimitador e encoding conforme seu CSV

# Interface do app
st.title('Consulta de Saldo de Produtos')

dados = carregar_dados()

# Mostrar somente colunas relevantes
dados = dados[['Produto', 'Produto Fornecedor', 'Descricao', 'Saldo', 'Multiplo', 'Fator Conversao', 'Data Ult. Compra', 'Qtde Ult. Compra']]

# Entrada de busca
consulta = st.text_input('Digite o Código ou parte da Descrição do Produto:')

if consulta:
    # Filtro de busca
    resultado = dados[dados.apply(lambda row: 
                                  consulta.lower() in str(row['Produto']).lower() or 
                                  consulta.lower() in str(row['Descricao']).lower() or
                                  consulta.lower() in str(row['Produto Fornecedor']).lower(), 
                                  axis=1)]
    
    if not resultado.empty:
        st.write('Resultados encontrados:')
        st.dataframe(resultado)
    else:
        st.warning('Nenhum produto encontrado.')
