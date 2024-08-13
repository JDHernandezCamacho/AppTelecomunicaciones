import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import streamlit as st


# Variables para la DB
host = 'bn83gilwrcfotqoazybx-mysql.services.clever-cloud.com'
user = 'uc0tzjpbwmcv8ro5'
password = 'LaNI5u2ZjXzafghQRntP'
db = 'bn83gilwrcfotqoazybx'

#  Motor de la DB
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')


# Consulta SQL internet
consulta_sql = 'SELECT * FROM `total_data_internet_TV_dispMovil`'
df_internet = pd.read_sql(consulta_sql, engine)
# Consulta SQL conectividad
consulta_sql = 'SELECT * FROM `mapa_conectividad_total3`'
df_conectividad = pd.read_sql(consulta_sql, engine)
# Cerrar la conexi{on}
engine.dispose()






# Sección para visualización de datos
st.title("Previsualización de Datos transformados")
# Divisor
st.markdown("---")
st.header("Dataset de de Internet, TV y Telefonía móvil")
st.write(df_internet)  # Mostrar el DataFrame correspondiente a la hoja seleccionada


# Divisor
st.markdown("---")
st.header("Dataset de mapa de conectividad")
st.write(df_conectividad)  # Mostrar el DataFrame correspondiente a la hoja seleccionada