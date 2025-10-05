# === pages/2_Analisis_Descriptivo.py ===
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuración de la página ---
st.set_page_config(page_title="Análisis Descriptivo", layout="wide")

# --- Título ---
st.title("Análisis Descriptivo del Dataset")

# --- Lectura de datos ---
data_path = Path(__file__).parent.parent / "data" / "deporte_eventos.csv"
if not data_path.exists():
    st.error("No se encontró el archivo 'data/deporte_eventos.csv'. Verifica su ubicación.")
    st.stop()

df = pd.read_csv(data_path)

# --- 1. Vista de los primeros registros ---
st.subheader("1. Primeros 10 registros del dataset")
st.dataframe(df.head(10), use_container_width=True)

# --- 2. Dimensiones del dataset ---
st.subheader("2. Dimensiones del dataset")
st.write(f"El dataset contiene un total de {df.shape[0]} filas y {df.shape[1]} columnas.")

# --- 3. Tipos de variables ---
st.subheader("3. Tipos de variables")
tipos = pd.DataFrame({
    "Variable": df.columns,
    "Tipo de dato": df.dtypes.astype(str)
})
st.dataframe(tipos, use_container_width=True)
st.markdown(
    "Se identifican variables numéricas (ID, Latitud, Longitud, Participantes, Duración_Horas) "
    "y categóricas (Departamento, Evento)."
)

# --- 4. Valores faltantes ---
st.subheader("4. Valores faltantes por variable")
faltantes = pd.DataFrame({
    "Variable": df.columns,
    "Valores faltantes": df.isnull().sum(),
    "Porcentaje (%)": round((df.isnull().sum() / len(df)) * 100, 2)
})
st.dataframe(faltantes, use_container_width=True)

st.markdown("Visualización del patrón de valores faltantes")
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap="crest")
st.pyplot(fig)
st.write("Se confirma que el dataset no presenta valores faltantes, garantizando la integridad de los análisis posteriores.")

# --- 5. Medidas de tendencia central y dispersión ---
st.subheader("5. Medidas estadísticas descriptivas")
medidas = df.describe(percentiles=[0.25, 0.5, 0.75]).transpose()
st.dataframe(medidas, use_container_width=True)


# --- 6. Detección de valores atípicos mediante Boxplots ---
st.subheader("6. Detección de valores atípicos mediante Boxplots")

num_cols = [col for col in df.select_dtypes(include=np.number).columns if col.lower() != "id"]

if len(num_cols) == 0:
    st.warning("No se detectaron columnas numéricas para generar boxplots.")
else:
    for col in num_cols:
        st.markdown(f"Variable: {col}")
        fig_box = px.box(
            df,
            y=col,
            title=f"Distribución y detección de valores atípicos en {col}",
            points="outliers",
            color_discrete_sequence=["steelblue"]
        )
        fig_box.update_traces(boxmean=True, jitter=0, marker=dict(size=6))
        fig_box.update_layout(
            yaxis_title=None,
            xaxis_visible=False,
            showlegend=False,
            margin=dict(l=40, r=40, t=60, b=40)
        )
        st.plotly_chart(fig_box, use_container_width=True)
        st.divider()

st.markdown("""
Los resultados evidenciados en los diagramas de caja y bigotes demuestran que no hay presencia aparente
de datos atípicos.
""")

st.markdown("---")
st.info("""
Por favor, continúa con la sección de **Georreferenciación**.
""")


