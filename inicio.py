import streamlit as st
import pandas as pd
import numpy as np
def mostrar():
    file_path = 'data/ventas_traducido_completo.csv'
    ventas_df = pd.read_csv(file_path)
    st.write(ventas_df)
    st.write(ventas_df.shape)

# Ejecutar la función mostrar en la aplicación de Streamlit
if __name__ == "__main__":
    mostrar()

