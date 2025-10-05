# DataViz Dashboard – Streamlit + Docker + Railway

Plantilla base para el **taller**: 3 páginas (Home, Mapa, Dashboard), Dockerfile, requirements y .dockerignore listos.

## Estructura
```
dataviz_streamlit_docker/
├─ app.py
├─ pages/
│  ├─ 1_Mapa.py
│  └─ 2_Dashboard.py
├─ data/
│  └─ data.csv   # coloca aquí tu dataset
├─ requirements.txt
├─ Dockerfile
├─ .dockerignore
└─ README.md
```

## Ejecutar localmente (sin Docker)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Probar con Docker (local)
```bash
docker build -t dataviz-app .
docker run -p 8501:8501 dataviz-app
```
Abre http://localhost:8501

## Despliegue en Railway (resumen)
1. Sube este proyecto a **GitHub**.
2. En **Railway**, crea un **New Project → Deploy from GitHub Repo**.
3. Variables/Build:
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - **PORT** se define automáticamente en Railway.
4. Despliega y toma la **URL pública** desde **Settings → Domains**.

> Ajusta las páginas para cumplir con tu rúbrica: análisis descriptivo, mapa con `folium`, gráficos con `plotly`, y texto explicativo.
