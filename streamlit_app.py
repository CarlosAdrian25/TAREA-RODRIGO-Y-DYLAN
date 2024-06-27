import streamlit as st
import pandas as pd

selected = st.sidebar.selectbox("Menu Principal", ["Total de ventas", "Total ventas cliente","Ventas por Dia","Ventas por Fecha"])

if selected == "Total de ventas":
    st.title("Bienvenido a la pagina de ventas")
elif selected == "Total ventas cliente":
    st.title("Bienvenido a la pagina de ventas por cliente")
elif selected=="Ventas por Dia":
    st.title("Bienvenido a la pagina de ventas por dia")
elif selected=="Ventas por Fecha":
    st.title("Bienvenido a la pagina de ventas por fecha")



