import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Carregar o modelo treinado
model = joblib.load('data/cars_price_model.pkl')

# Título da aplicação
st.title('Previsão de Preço de Carros')

# Entrada de dados do usuário
year = st.slider('Ano de Fabricação', 2010, 2020, 2015)
engine_size = st.number_input('Tamanho do Motor (L)', min_value=1.0, max_value=5.0, step=0.1)
price_eur = st.number_input('Preço (EUR)', min_value=1000.0, max_value=100000.0, step=100.0)

# Botão para previsão
if st.button('Prever Preço (USD)'):
    # Preparar os dados de entrada
    input_data = np.array([[year, engine_size, price_eur]])
    
    # Fazer a previsão
    prediction = model.predict(input_data)
    
    # Exibir o resultado
    st.write(f'Preço Previsto (USD): {prediction[0]:.2f}')
