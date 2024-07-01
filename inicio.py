import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def mostrar():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    st.write(ventas_df)
    st.write(ventas_df.shape)

def total_ventas_por_factura():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    
    
    total_ventas = ventas_df.groupby('NoFactura')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['NumeroFactura', 'TotalVentas']
    
    
    total_ventas['NumeroFactura'] = total_ventas['NumeroFactura'].astype(str)
    
   
    total_ventas_10 = total_ventas.head(10)
   
    plt.figure(figsize=(10, 6))
    plt.bar(total_ventas_10['NumeroFactura'], total_ventas_10['TotalVentas'], edgecolor='k', alpha=0.7)
    plt.title('Total de Ventas por Factura (Top 10)')
    plt.xlabel('Número de Factura')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=90) 
    plt.grid(True)
    
    
    st.pyplot(plt)

def total_ventas_por_cliente():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    
    
    total_ventas = ventas_df.groupby('IdCliente')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['IdCliente', 'TotalVentas']
    
  
    total_ventas['IdCliente'] = total_ventas['IdCliente'].astype(str)
    
    
    total_ventas_10 = total_ventas.head(10)
    st.title('Nº DE VENTAS POR CLIENTE (Top 10)')
    # st.write(total_ventas_10)
    # st.write(total_ventas_10.shape)
    
    plt.figure(figsize=(10, 6))
    plt.bar(total_ventas_10['IdCliente'], total_ventas_10['TotalVentas'],color='green', edgecolor='k', alpha=0.7)
    plt.title('NUMERO DE VENTAS POR CLIENTE')
    plt.xlabel('ID de Cliente')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=90)  
    plt.grid(True)
    
    
    st.pyplot(plt)

def total_Factura():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    Cantidad = ventas_df['NoFactura'].value_counts().reset_index()
    Cantidad.columns = ['NoFactura', 'Cantidad']
    
    st.write(Cantidad)

def total_ventas_por_fecha():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    
   
    total_ventas = ventas_df.groupby('Fecha')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Fecha', 'TotalVentas']
    
    
    total_ventas_10 = total_ventas.head(10)
    st.title('CANTIDAD DE VENTAS POR FECHA (Top 10)')
    st.write(total_ventas_10)
    st.write(total_ventas_10.shape)
    
    
    plt.figure(figsize=(10, 6))
    plt.bar(total_ventas_10['Fecha'], total_ventas_10['TotalVentas'], color='skyblue', edgecolor='k', alpha=0.7)
    plt.title('Cantidad de Ventas por Fecha (Top 10)')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=90) 
    plt.grid(True)
    
   
    st.pyplot(plt)

def total_ventas_por_dia():
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    
    
    ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])
    
    
    ventas_df['Dia'] = ventas_df['Fecha'].dt.day
    
   
    total_ventas = ventas_df.groupby('Dia')['Cantidad'].sum().reset_index()
    total_ventas.columns = ['Dia', 'TotalVentas']
    
   
    total_ventas_10 = total_ventas.head(10)
    st.title('CANTIDAD DE VENTAS POR DÍA (Top 10)')
    st.write(total_ventas_10)
    st.write(total_ventas_10.shape)
    
    
    plt.figure(figsize=(10, 6))
    plt.bar(total_ventas_10['Dia'], total_ventas_10['TotalVentas'], color='skyblue', edgecolor='k', alpha=0.7)
    plt.title('Cantidad de Ventas por Día (Top 10)')
    plt.xlabel('Día del Mes')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=90)  
    plt.grid(True)
    
   
    st.pyplot(plt)

def total():
    file_path = 'data/ventas_traducido.csv'
    ventas_df = pd.read_csv(file_path)
    
    total_por_factura_10 = ventas_df[['NoFactura', 'Total']].head(10)
    
    st.title('TOTAL DE VENTAS POR FACTURA (Top 10)')
    
    st.write(total_por_factura_10)
    st.write(total_por_factura_10.shape)
    
    plt.figure(figsize=(10, 6))
    
    numeros_factura = total_por_factura_10['NoFactura'].unique()
    
    # Graficar las barras
    plt.bar(numeros_factura, 
            total_por_factura_10.groupby('NoFactura')['Total'].sum(),  
            edgecolor='orange',    
            alpha=0.7,
            linewidth=9)      
    plt.title('Total de Ventas por Factura (Top 10)')
    plt.xlabel('Número de Factura')
    plt.ylabel('Total Vendido')
    plt.xticks(rotation=90)  
    plt.grid(True)

    st.pyplot(plt)
