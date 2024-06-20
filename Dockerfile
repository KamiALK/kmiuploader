
# Dockerfile

FROM python:3.11.2

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .



# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar tu aplicación cuando el contenedor se inicie
CMD ["python", "main.py"]

# docker build -t mi-app-kafka .
# docker run --rm --network kafka_kafkanet mi-app-kafka

