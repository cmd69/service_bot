# Dockerfile para JellyBot MVP
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app/ ./app/

# Crear usuario no-root
RUN useradd --create-home --shell /bin/bash jellybot
RUN chown -R jellybot:jellybot /app
USER jellybot

# Exponer puerto (opcional para webhooks futuros)
EXPOSE 8000

# Comando por defecto
CMD ["python", "-m", "app.main"]