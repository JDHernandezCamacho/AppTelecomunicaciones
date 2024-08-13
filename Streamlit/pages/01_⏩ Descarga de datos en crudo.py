import streamlit as st
import pandas as pd

# URLs de los libros de Excel
url_internet = "https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Internet.xlsx"
url_telefonia_movil = "https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Telefonia_movil.xlsx"
url_tv = "https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Television.xlsx"
url_conectividad = "https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/mapa_conectividad.xlsx"


# Sección para visualización de datos
st.title("Información y descarga de los dataset con datos en crudo")

# Divisor
st.markdown("---")
st.markdown('Descarga directa')
st.markdown(url_internet)

# Divisor
st.markdown("---")
st.markdown('Descarga directa')
st.markdown(url_telefonia_movil)

# Divisor
st.markdown("---")
st.markdown('Descarga directa')
st.markdown(url_tv)

# Divisor
st.markdown("---")
st.markdown('Descarga directa')
st.markdown(url_conectividad)

# Divisor
st.markdown("---")
st.markdown('Ir a la página oficial')
st.markdown('https://indicadores.enacom.gob.ar/datos-abiertos')
