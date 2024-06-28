import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def mostrar():
    # Cargar datos desde el archivo CSV
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    
    # Agrupar datos por 'Descripcion' y sumar la 'Cantidad'
    data = ventas_df.groupby('Descripcion')['Cantidad'].sum()
    
    # Preparar datos para etiquetas y tamaños de secciones del gráfico de pastel
    labels = data.index  # Usamos los índices de 'data' como etiquetas
    sizes = data.values  # Usamos los valores de 'data' como tamaños
    
    # Crear gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Para asegurar que el gráfico es un círculo.
    
    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

def mostrar_grafico_pie():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
