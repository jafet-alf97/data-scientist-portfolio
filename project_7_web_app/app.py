import streamlit as st
import pandas as pd
import sidetable as stb
import plotly.express as px
vehicles_data = pd.read_csv('notebooks/vehicles_us.csv', header=0)
# Crear la columna 'brand' extrayendo la primera palabra de 'model'
vehicles_data['brand'] = vehicles_data['model'].str.split(' ').str[0]
st.title('Vehicle sales ads application')
# Crea una tabla de nuestro DataFrame
st.dataframe(vehicles_data)
st.write('Analisis exploratorio inicial:')
st.write('Revisar primeras filas:')
st.dataframe(vehicles_data.head())
st.write('Revisar primeros valores ausentes:')
st.dataframe(vehicles_data.stb.missing(style=True))
# Encabezado
st.header('Exploratory Data Analysis: Vehicles')
# Botón para generar el histograma de distribución de precios
if st.button('Generate price histogram'):
    fig = px.histogram(vehicles_data, x='price',
                       title='Price distribution of vehicles', nbins=50)
    fig.update_xaxes(range=[0, 100000])
    fig.update_layout(xaxis_title='Price',
                      yaxis_title='Quantity', template='plotly_white')
    st.plotly_chart(fig)

# Botón para generar gráfico de boxplot: Condition vs Price
if st.button('Generar boxplot: Condition vs Price'):
    fig = px.box(vehicles_data, x='condition',
                 y='price', title='Condition vs Price')
    st.plotly_chart(fig)

# Button to generate price distribution by brand
if st.button('Generate price histogram by brand'):
    fig = px.histogram(vehicles_data, x='price', color='brand',
                       title='Price distribution by brand',
                       labels={'price': 'Price', 'brand': 'Brand'})
    st.plotly_chart(fig)

# Button to generate price distribution by model
if st.button('Generate price histogram by model'):
    fig = px.histogram(vehicles_data, x='price', color='model',
                       title='Price distribution by model',
                       labels={'price': 'Price', 'model': 'Model'})
    st.plotly_chart(fig)

# Button to generate the scatter plot of price vs odometer
if st.button('Generate scatter plot: Price vs Odometer'):
    fig = px.scatter(vehicles_data, x='odometer',
                     y='price', title='Price vs. Odometer')
    st.plotly_chart(fig)
