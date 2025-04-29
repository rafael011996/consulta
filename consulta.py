import pandas as pd
import streamlit as st
st.set_page_config(page_title="Consulta de Produtos", layout="wide")  # <-- AQUI
# Carregar CSV
@st.cache_data(ttl=0)
def carregar_dados():
    url = 'https://raw.githubusercontent.com/rafael011996/consulta/main/produtos.csv'
    return pd.read_csv(url, delimiter=';', encoding='utf-8')


# Interface do app
st.title('Consulta de Saldo de Produtos')

dados = carregar_dados()

# Mostrar somente colunas relevantes
dados = dados[['Produto', 'Produto Fornecedor', 'Descricao', 'Saldo', 'Multiplo', 'Fator Conversao', 'Data Ult. Compra', 'NCM', 'CEST', '% IPI']]

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
