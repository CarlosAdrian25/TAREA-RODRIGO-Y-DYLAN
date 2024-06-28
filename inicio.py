import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico_torta(file_path):
    # Cargar el archivo CSV
    ventas_df = pd.read_csv(file_path)
    
    # Agregar las ventas por descripción de producto
    sales_by_product = ventas_df.groupby('Descripcion')['Cantidad'].sum()
    
    # Calcular porcentajes
    sales_by_product_percentage = sales_by_product / sales_by_product.sum() * 100
    
    # Crear el gráfico de torta
    fig, ax = plt.subplots(figsize=(10, 8))
    sales_by_product_percentage.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title('Porcentaje de Ventas por Producto')
    ax.set_ylabel('')  # Ocultar etiqueta del eje y
    st.pyplot(fig)

# Usar Streamlit para mostrar el gráfico
st.title("Gráfico de Torta de Ventas por Producto")

file_path = 'data/ventas_traducido_completo.csv'
generar_grafico_torta(file_path)

