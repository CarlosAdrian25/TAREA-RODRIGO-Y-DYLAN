import streamlit as st
from inicio import mostrar
from total_ventas_cliente import mostrar_py

st.sidebar.title("MENU DE OPCIONES")
selected = st.sidebar.selectbox("SELECCIONA UNA OPCION", ["INICIO", "Total de ventas", "Total ventas cliente", "Ventas por Dia", "Ventas por Fecha"])

if selected == "INICIO":
    mostrar()
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


