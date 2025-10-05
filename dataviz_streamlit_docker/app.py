# === app.py ===
import streamlit as st
from datetime import date

# --- Configuración general ---
st.set_page_config(
    page_title="Dashboard de Eventos Deportivos",
    page_icon="🏟️",
    layout="centered"
)

# --- Estilo personalizado ---
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: white;
            margin-bottom: 0px;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #d1d1d1;
            margin-top: 5px;
            margin-bottom: 30px;
        }
        .info-box {
            background-color: #262730;
            padding: 25px 50px;
            border-radius: 12px;
            width: 70%;
            margin: 0 auto;
            text-align: left;
            line-height: 2;
            color: #f2f2f2;
        }
        .info-box b {
            color: #ffffff;
        }
        .footer {
            font-size: 14px;
            color: #a0a0a0;
            text-align: center;
            margin-top: 60px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Contenido principal ---
st.markdown('<div class="title">DASHBOARD DE EVENTOS DEPORTIVOS EN COLOMBIA</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Actividad #3</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="info-box">
<b>Autor:</b> Miguel Ángel Pérez Vargas<br>
<b>Programa:</b> Ciencia de Datos<br>
<b>Materia:</b> Visualización de Datos y Toma de Decisiones<br>
<b>Institución:</b> Universidad del Norte<br>
<b>Docente:</b> Keyla Vanessa Alba Molina<br>
<b>Fecha:</b> {date.today().strftime("%d/%m/%Y")}
</div>
""", unsafe_allow_html=True)

# --- Pie de página ---
st.markdown("""
<div class="footer">
Este dashboard fue desarrollado como parte del curso de Visualización de Datos y es netamente académico.<br>
Incluye análisis descriptivo, mapas interactivos y representación geográfica de eventos deportivos en Colombia.
</div>
""", unsafe_allow_html=True)



