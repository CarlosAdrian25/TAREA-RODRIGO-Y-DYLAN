import streamlit as st

st.sidebar.title("MENU DE OPCIONES")
selected = st.sidebar.selectbox("SELECCIONA UNA OPCION", ["Total de ventas", "Total ventas cliente","Ventas por Dia","Ventas por Fecha"])

if selected == "Total de ventas":
    where_to= st.sidebar.selectbox("Total de ventas:", ["Unidades Factura", "Valor por Factura"])
    if where_to == "Unidades Factura":
        st.title("Total de ventas por Unidades Factura")
    elif where_to=="Valor por Factura":
        st.title("Total de ventas por Valor por Factura")
elif selected == "Total ventas cliente":
    st.title("Bienvenido a la pagina de ventas por cliente")
elif selected=="Ventas por Dia":
    st.title("Bienvenido a la pagina de ventas por dia")
elif selected=="Ventas por Fecha":
    st.title("Bienvenido a la pagina de ventas por fecha")

