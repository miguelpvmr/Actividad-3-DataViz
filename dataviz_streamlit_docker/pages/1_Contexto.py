# === pages/1_Contexto.py ===
import streamlit as st
from pathlib import Path
from PIL import Image

# --- Configuración de la página ---
st.set_page_config(page_title="Contexto del Dataset", layout="wide")

# --- Título ---
st.title(" Contexto del Dataset")

st.markdown("""
### Introducción
El presente proyecto tiene como propósito analizar información relacionada con **eventos deportivos realizados en Colombia**.  
            
El dataset utilizado recopila datos sobre diferentes disciplinas deportivas, su ubicación geográfica, el número de participantes
y la duración de cada evento.

Estos datos permiten realizar una exploración tanto **estadística** como **geográfica**, identificando tendencias, patrones y posibles
concentraciones de actividad deportiva en distintas regiones del país.
""")

# --- Imagen  ---
st.divider()
image_path = Path(__file__).parent.parent / "osoanteojos.png"

if image_path.exists():
    st.image(image_path, caption="Eventos deportivos en Colombia", use_container_width=400)
else:
    st.warning(" No se encontró la imagen alusiva. Asegúrate de colocarla en la misma carpeta que `app.py`.")

st.divider()

# --- Contexto  ---
st.markdown("""
### Descripción del dataset
El conjunto de datos fue diseñado con fines académicos para demostrar el uso de técnicas de **visualización de datos**.  
Cada fila representa un evento deportivo, con variables que permiten caracterizar aspectos como:

- **Departamento:** región donde tuvo lugar el evento.  
- **Evento:** disciplina deportiva registrada.  
- **Participantes:** número total de asistentes o competidores.  
- **Duración_Horas:** tiempo estimado del evento.  
- **Latitud / Longitud:** coordenadas geográficas utilizadas para georreferenciación.  

Este contexto servirá como punto de partida para los análisis estadísticos y mapas que se desarrollarán  
en las siguientes secciones del dashboard.
""")

st.info("Por favor, continúa con la sección **Análisis Descriptivo** para comenzar la exploración estadística del dataset.")

