# === Dockerfile ===
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app completa
COPY . .

# Exponer puerto
ENV PORT=8501
EXPOSE 8501

# Ejecutar Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=${PORT:-8501}", "--server.address=0.0.0.0"]

