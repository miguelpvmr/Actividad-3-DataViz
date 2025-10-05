# === pages/3_Georreferenciacion.py ===
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from pathlib import Path

# --- Configuración general ---
st.set_page_config(page_title="Georreferenciación", page_icon="🗺️", layout="wide")
st.title("Georreferenciación de eventos deportivos por departamento")

# --- Carga de datos ---
data_path = Path(__file__).parent.parent / "data" / "deporte_eventos.csv"
if not data_path.exists():
    st.error(" No se encontró el archivo 'data/deporte_eventos.csv'. Verifica su ubicación.")
    st.stop()

df = pd.read_csv(data_path)

# --- Filtros dinámicos ---
st.sidebar.header("Filtros de visualización")

departamentos = st.sidebar.multiselect(
    "Selecciona los departamentos a mostrar:",
    options=sorted(df["Departamento"].unique())
)

eventos = st.sidebar.multiselect(
    "Selecciona los tipos de evento a mostrar:",
    options=sorted(df["Evento"].unique())
)

# --- Aplicación de filtros ---
if departamentos and eventos:
    filtered_df = df[(df["Departamento"].isin(departamentos)) & (df["Evento"].isin(eventos))]
elif departamentos:
    filtered_df = df[df["Departamento"].isin(departamentos)]
elif eventos:
    filtered_df = df[df["Evento"].isin(eventos)]
else:
    filtered_df = df.copy()

# --- Mapa base ---
st.subheader("Mapa interactivo de eventos deportivos")

m = folium.Map(location=[4.5, -74.1], zoom_start=6, tiles="CartoDB positron")

# --- Marcadores ---
for _, row in filtered_df.iterrows():
    popup = f"""
    <b>Departamento:</b> {row['Departamento']}<br>
    <b>Evento:</b> {row['Evento']}<br>
    <b>Participantes:</b> {row['Participantes']}<br>
    <b>Duración:</b> {row['Duración_Horas']} horas
    """
    folium.CircleMarker(
        location=[row["Latitud"], row["Longitud"]],
        radius=6,
        color="blue",
        fill=True,
        fill_opacity=0.6,
        popup=popup
    ).add_to(m)

# --- Capa de mapa de calor ---
if st.checkbox("Mostrar mapa de calor"):
    heat_data = filtered_df[["Latitud", "Longitud"]].values.tolist()
    if len(heat_data) > 0:
        HeatMap(heat_data, radius=15, blur=10).add_to(m)
    else:
        st.warning("No hay datos para mostrar en el mapa de calor.")

# --- Mostrar mapa ---
st_folium(m, width=900, height=550)

# --- Tabla resumen ---
st.subheader("Resumen de los eventos visibles en el mapa")
st.dataframe(filtered_df, use_container_width=True)


