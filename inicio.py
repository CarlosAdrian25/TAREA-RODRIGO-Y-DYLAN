import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def mostrar():
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    st.write(ventas_df)
    st.write(ventas_df.shape)

def mostrar_grafico_pie():
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    # Agrupar datos por 'Descripcion' y sumar la 'Cantidad'
    data = ventas_df.groupby('Descripcion')['Cantidad'].sum()
    
    # Crear gráfico de pie
    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para asegurar que el gráfico es un círculo.

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)


