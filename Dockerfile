
# Usa una imagen base con Python 3.11.2
FROM python:3.11.2-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias necesarias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define el comando por defecto para ejecutar la aplicación
CMD ["python3", "main.py"]
