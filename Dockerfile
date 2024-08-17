
# Usa una imagen base de Python
FROM python:3.11.2

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .

# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instala ffmpeg
RUN apt-get update && \
  apt-get install -y ffmpeg

# Comando por defecto para ejecutar tu aplicación cuando el contenedor se inicie
CMD ["python", "main.py"]
