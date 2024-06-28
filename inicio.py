import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def mostrar():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    st.write(ventas_df)
    st.write(ventas_df.shape)

def total_ventas_por_producto():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    total_ventas = ventas_df.groupby('Descripcion')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Descripcion', 'TotalVentas']
    st.write(total_ventas)

def total_ventas_por_CLIENTE():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    total_ventas = ventas_df.groupby('IdCliente')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Descripcion', 'TotalVentas']
    st.title('Nº DE VENTAS POR CLIENTE')
    st.write(total_ventas)

def total_Factura():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    Cantidad = ventas_df['NoFactura'].value_counts().reset_index()
    Cantidad.columns = ['NoFactura', 'Cantidad']
    st.title('TOTAL DE VENTAS (UNIDADES) FACTURA')
    st.write(Cantidad)

def total_ventas_por_Fecha():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    total_ventas = ventas_df.groupby('Fecha')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Descripcion', 'TotalVentas']
    st.title('CANTIDAD DE VENTAS POR FECHA')
    st.write(total_ventas)

def total_ventas_por_dia():
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])
    ventas_df['Dia'] = ventas_df['Fecha'].dt.day
    total_ventas = ventas_df.groupby('Dia')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Dia', 'TotalVentas']
    st.title('CANTIDAD DE VENTAS POR DÍA')
    st.write(total_ventas)

def total():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    
    # Agrupar por 'NoFactura' y calcular la suma de 'Total' para cada factura
    total_por_factura = ventas_df.groupby('NoFactura').agg({'Total': 'sum'}).reset_index()
    
    # Mostrar el título utilizando st.title si estás usando Streamlit
    st.title('TOTAL DE VENTAS POR FACTURA')
    
    # Mostrar los resultados utilizando st.write
    st.write(total_por_factura)
