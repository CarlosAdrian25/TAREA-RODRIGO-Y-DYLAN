import streamlit as st
from inicio import mostrar,mostrar_grafico_pie
from total_ventas_cliente import mostrar_py
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("MENU DE OPCIONES")
selected = st.sidebar.selectbox("SELECCIONA UNA OPCION", ["INICIO", "Total de ventas", "Total ventas cliente", "Ventas por Dia", "Ventas por Fecha"])

if selected == "INICIO":
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)

    # Agrupar datos por 'Descripcion' y sumar la 'Cantidad'
    data = ventas_df.groupby('Descripcion')['Cantidad'].sum()

# Crear gráfico de pie
    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Para asegurar que el gráfico es un círculo.

# Guardar el gráfico de pie como una imagen
    output_image_path = 'ventas_pie_chart.png'
    fig.savefig(output_image_path)

    print(f"Gráfico de pastel guardado en {output_image_path}")
elif selected == "Total de ventas":
    where_to = st.sidebar.selectbox("Total de ventas:", ["Unidades Factura", "Valor por Factura"])
    if where_to == "Unidades Factura":
        st.title("Unidades Factura")
        mostrar_py()
    elif where_to == "Valor por Factura":
        st.title("Valor por Factura")
elif selected == "Total ventas cliente":
    where_to_dos = st.sidebar.selectbox("Total ventas cliente", ["Ventas por Cliente", "Distribucion V.Clientes"])
    if where_to_dos == "Ventas por Cliente":
        st.title("Ventas por Cliente")
    elif where_to_dos == "Distribucion V.Clientes":
        st.title("Distribucion V.Clientes")
elif selected == "Ventas por Dia":
    where_to_tres = st.sidebar.selectbox("Ventas por Dia:", ["Unidad", "Valor"])
    if where_to_tres == "Unidad":
        st.title("Unidad")
    elif where_to_tres == "Valor":
        st.title("Valor")
elif selected == "Ventas por Fecha":
    st.title("Bienvenido a la pagina de ventas por fecha")


