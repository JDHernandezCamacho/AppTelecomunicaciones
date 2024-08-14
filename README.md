
# ``` | ✏️ APP - Analisis de datos de Telecomunicaciones ✏️ |🟢 Data Analytics 🟢|🔵 Business Intelligence 🔵| 🔴 Telecomunicaciones en Argentina 🔴 | 🚀 Henry 🚀 ```
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%2370399F.svg?style=for-the-badge&logo=seaborn&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=ffffff)
![venv](https://img.shields.io/badge/Virtualenv-venv-%2300FFFF?style=for-the-badge&logo=python)
![PowerBi](https://img.shields.io/badge/Power_Bi-100000?style=for-the-badge&logo=PowerBi&logoColor=white&labelColor=F7FF13&color=FFF700)
![PyMySQL](https://img.shields.io/badge/PyMySQL-100000?style=for-the-badge&logo=PowerBi&logoColor=white&labelColor=0DD3FF&color=00D9FF)
![MySQL](https://img.shields.io/badge/MySQL-100000?style=for-the-badge&logo=MySQL&logoColor=000000&labelColor=5EECFF&color=5EECFF)
![SQLAlquemy](https://img.shields.io/badge/SQLAlquemy-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=FF759F)
![StreamLit](https://img.shields.io/badge/streamlit-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=7593FF)
![MariaDB](https://img.shields.io/badge/maria_db-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=0073FF)


![Barner](/assets/BrnerInicial.png)

<div>
    <div align='center'>
    <a href="https://apptelecomunicaciones-anpynkqeoujjh4uvtwz9jx.streamlit.app/" target="_blank" target="_blank">
          <img  src="https://img.shields.io/badge/app-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=FF7C00"/>
       </a>
    </div>
</div>



# ✔️``Introducción``

En la era digital actual, la toma de decisiones informadas es crucial para el éxito de cualquier organización. Con la creciente cantidad de datos disponibles, es esencial poder analizar y interpretar esta información para obtener insights valiosos que impulsen el crecimiento y la innovación. Este proyecto de Data Analytics y Business Intelligence tiene como objetivo desarrollar una plataforma integral que permita a las organizaciones recopilar, analizar y visualizar datos de manera efectiva, para tomar decisiones informadas y mejorar su desempeño. A través de la combinación de técnicas de análisis de datos, visualización de información y tecnologías de inteligencia empresarial, este proyecto busca proporcionar una solución completa que permita:

- Recopilar y integrar datos de diversas fuentes
- Analizar y procesar datos para obtener insights valiosos
- Visualizar información de manera clara y efectiva
- Tomar decisiones informadas basadas en datos

Con este proyecto, se pretende ayudar a la empresa de Telecomunicaciones a aprovechar el poder de los datos para impulsar su crecimiento, mejorar su eficiencia y tomar decisiones informadas que les permitan mantenerse competitivas en un mercado en constante evolución.



# ✔️```Los Datos```

Los datos fueron obtenidos de la página oficial de ENACOM (Ente Nacional de Comunicaciones) es el organismo que se encarga de regular los medios y las comunicaciones en Argentina, los datos disponibles incluyen:
- Indicadores de mercado: datos sobre los distintos servicios regulados por ENACOM, como televisión por suscripción y televisión satelital.
- Indicadores de mercado: datos sobre Accesibilidad a servicios de internet por provincias, partidos y localidades.
- Indicadores de mercado: Ingresos en pesos por TV e internet.
- Indicadores de accesibilidad y penetración de los servicios de telecomunicaciones.
- Indicadores geográficos: que indican las ubicaciones y los servicios prestados.

### **Fuente de datos**
Los datos originales los puedes descargar de los siguientes enlaces:
+ [Internet](https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Internet.xlsx) Dataset de Internet
+ [Telefonia móvil](https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Telefonia_movil.xlsx) Dataset de telefonía móvil
+ [Televisión](https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/Television.xlsx) Dataset de Televisión
+ [Conectividad](https://indicadores.enacom.gob.ar/Files/Datos_Abiertos/mapa_conectividad.xlsx) Dataset de conectividad
+ [Diccionario de datos](/Info/Diccionario de datos PIDA.docx) Diccionario con algunas descripciones de las columnas disponibles en el dataset



# ✔️```Objetivos del proyecto```

- Orientar a las empresas a brindar una buena calidad en sus servicios.
- Identificar oportunidades de crecimiento
- Plantear soluciones personalizadas a sus posibles clientes



# ✔️```Proceso del proyecto```
El siguiente gráfico muestra cual fue el desarrollo del proyecto: 
![Esquema gráfico](/assets/procesoAPP.png)




1. ## ⚙️ ETL 
Durante esta etapa del proyecto, de llevó a cabo la extracción, transformación y carga de los datos, todas las transformaciones que se creyeron pertinentes se encuentran en el archivo ``ETL.ipybn`` y  algunos de los procedimientos realizados como pruebas de transformación están en ``ETL_indivisual(no_utilizado).ipybn`` ambos archivos alojados en la carpeta ``ETL``. todas las transformaciones están documentadas paso a paso dentro del archivo para evitar confusiones. El resultado de este proceso llevo a construir una base de datos alojada en CleverCloud
> [!IMPORTANT]
> Ten cuidado al ejecutar este script, ten en cuenta que si ejecutas el archivo, se editan las bases de datos ya cargadas.
> En caso de replicar, es importante ejecutar el archivo ``ETL.ipynb`` con las librerias previamente instaladas. 👀
### ✔️```Resultados```
![ETL](/assets/ETL.png)



2. ## 📉 EDA
Tras haber completado las tareas de ETL, se realiza el EDA (Análisis Exploratorio de Datos) den este paso del proceso se extraen los datos de las bases de datos que previamente fueron cargadas. El archivo ``EDA.ipynb`` ubicado dentro de la carpeta ``EDA`` contiene los pasos detallados de este punto del proceso y el objetivo principal es entender como estan estructurados los datos mediante graficos, tratamiento de tablas, datos, etc.
> [!IMPORTANT]
> De igual forma es importante no borrar las bases de datos ya previamnete cargadas en el proyecto. 👀
### ✔️```Resultados```
![EDA](/assets/EDA_0.png)
![EDA](/assets/EDA_1.png)
![EDA](/assets/EDA_2.png)
![EDA](/assets/EDA_3.png)



3. ## 🧠 Power Bi
tras realizar el analisis de los datos y sabiendo que se encuentran en las bases de datos listos para ser consumidos, se traen desde la web de clever cloud a la herramienta de power bi una poderosa aplicación para realizar visualizaciones, en ella se trabajan los datos y se genera como resultado final un dashboard con todos los insights que se pudieron encontrar.
El Dashboard esta dividido en 4 secciones importantes para el análisis de los datos:
1. Analisis Temporal del servicio Internet
2. Análisis temporal del servicio de TV y Telefonía móvil
3. Analisis geográfico por ubicación
4. KPI o Indicadores Claves de Desempeño
El dashboard elaborado se encuentra en la carpeta ``PowerBi`` y el arhivo con el nombre ``Dashboard_Telecomunicaciones_Diego.pbix``
### ✔️```Resultados```
![Dashboard](/assets/Dash_1.png)
![Dashboard](/assets/Dash_2.png)
![Dashboard](/assets/Dash_3.png)
![Dashboard](/assets/Dash_4.png)
![Dashboard](/assets/Dash_5.png)


4. ## ✏️ Streamlit (Visualización)
streamlit es una poderosa libreria para realizar visualizaciones mediante codigo python. El objetivo de su uso en este proyecto  es para poder compartir la información que proporciona el dashboard a usuarios finales mediante la web, con ello es posible que la comunicación de los logros obtenidos sea comunicada con quien este interesado en conocerla.
La carpeta ``Streamlit`` dentro de este proyecto contiene un archivo ``main.py``, este contieen los códigos necesarios para ejecutar la ventana principal de la app.
De igual forma se tiene una carpeta llamada ``pages`` que contiene 3 archivos, el primero de ellos deploya Una página con enlaces hacia los datos de la ENACOM, el segundo archivo muestra tablas con los datos transformados, estos provienen directamente de la base de datos donde fueron cargados después de realizar el ETL, ahí se puede visualizar como se estructurarron los datos para el siguiente paso y por último el archivo con el nombre dashboard, contiene el dashboard realizado en Power Bi.
> [!IMPORTANT]
> El resultado de la app lo puedes visualizar aquí.  👀

<div>
    <div align='center'>
    <a href="https://apptelecomunicaciones-anpynkqeoujjh4uvtwz9jx.streamlit.app/" target="_blank" target="_blank">
          <img  src="https://img.shields.io/badge/app-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=FF7C00"/>
    </a>
    </div>
</div>

### ✔️```Resultados```
![Streamlit](/assets/streamlit_1.png)
![Streamlit](/assets/streamlit_2.png)




# ✔️```Herramientas y librerías utilizadas```

Para el desarrollo de este proyecto se manipularon las siguientes herramientas:

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%2370399F.svg?style=for-the-badge&logo=seaborn&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=ffffff)
![venv](https://img.shields.io/badge/Virtualenv-venv-%2300FFFF?style=for-the-badge&logo=python)
![PowerBi](https://img.shields.io/badge/Power_Bi-100000?style=for-the-badge&logo=PowerBi&logoColor=white&labelColor=F7FF13&color=FFF700)
![PyMySQL](https://img.shields.io/badge/PyMySQL-100000?style=for-the-badge&logo=PowerBi&logoColor=white&labelColor=0DD3FF&color=00D9FF)
![MySQL](https://img.shields.io/badge/MySQL-100000?style=for-the-badge&logo=MySQL&logoColor=000000&labelColor=5EECFF&color=5EECFF)
![SQLAlquemy](https://img.shields.io/badge/SQLAlquemy-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=FF759F)
![StreamLit](https://img.shields.io/badge/streamlit-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=7593FF)
![MariaDB](https://img.shields.io/badge/maria_db-100000?style=for-the-badge&logo=&logoColor=A78A8A&labelColor=BA9A9A&color=0073FF)


# ✔️```Replicación del proyecto```
La app que se encuentra en este repositorio puedes replicarlo por tí mismo, así como corroborar código, realizar modificaciones, realizar consultas, ejecutar pruebas, como base de estudio e incluso mejorarlo. Para ello es necesario que sigas los siguientes pasos:
1. Forkea este repositorio.
2. Sincronizarlo en tu ordenador.
3. Configura tu entorno virtual.
4. Activa tu entorno virtual.
5. Asegurate de tener los archivos necesarios: carpeta ``Streamlit`` con su archivo ``main.py``, carpeta ``pages`` con 3 archivos importantes en formato py.
6. Instala las dependencias especificadas en el archivo ``requirements.txt``.
7. Crea y ejecuta tu entorno virtual ``py venv venv``, ``venv/Scripts/activate ``
7. Ejecuta el comando ``streamlit run .\streamlit\main.py`` para iniciar la aplicación.
8. Despliega el Streamlit en tu ordenador accediendo a tu localhost y el puerto dedicado mismo que te será proporcionado cuando ejecutes el paso anterior.



# ✔️```Conclusiones y recomendaciones:```

1. Para el tipo de servicio de internet es recomendable proporcionar servicios de velocidades de 30 Mbps o mayores.
2. Para los partidos con población mayor al 10K habitantes y menor a 25% de accesos, incrementar el porcentaje en un 10%.
3. Para el incremento de ingresos por accesos de internet, telefonía y televisión, realizar promociones o paquetes de los tres servicios.


# ✔️```Sobre mi```

[<img src="https://media.licdn.com/dms/image/D5603AQEnBacsLH1pnA/profile-displayphoto-shrink_800_800/0/1715214794765?e=1727913600&v=beta&t=2UKwQG8Hd4qK4Ac_R40acaT1UojfqqtOkECmPSpxs4s" width=150><br><sub>Juan DIego Hernández Camacho</sub>](https://www.linkedin.com/in/juan-diego-hernandez-camacho-5176022aa/)


Gracias por leer este repositorio 💛

No olvides dejar tu estrellita ⭐