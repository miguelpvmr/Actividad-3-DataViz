# Imagen base ligera de Python
FROM python:3.11-slim

# Evita escribir .pyc y mantiene los logs visibles
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para Streamlit
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 libsm6 libxext6 libxrender-dev libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al contenedor
COPY . .

# Configurar variable de puerto
ENV PORT=8501
EXPOSE 8501

# Comando para ejecutar Streamlit (clave: el host 0.0.0.0)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]



