import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Remove espaços extras dos nomes das colunas
df_top_100_books.columns = df_top_100_books.columns.str.strip()
df_reviews.columns = df_reviews.columns.str.strip()

# Preço máximo
price_max = df_top_100_books["book price"].max()

# Preço mínimo
price_min = df_top_100_books["book price"].min()

# Sidebar com preços
max_price = st.sidebar.slider(
    "Drag to the price you want to check.",
    price_min,
    price_max,
    price_max
)

# Filtra os livros pelo preço
df_books = df_top_100_books[
    df_top_100_books["book price"] <= max_price
]

# Exibe a tabela no navegador primeiro
st.dataframe(df_reviews)

# Gráfico de barras
fig = px.bar(
    df_books["year of publication"].value_counts()
)

# grafico ao lado
fig2 = px.histogram(
    df_books["book price"]
)

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
