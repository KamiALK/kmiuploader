
FROM bitnami/kafka:latest

# Copia el script create_topics.sh al contenedor
COPY create_topics.sh /scripts/create_topics.sh

# Asegúrate de que el script tenga permisos de ejecución
RUN chmod +x /scripts/create_topics.sh

# Configura el entrypoint
ENTRYPOINT ["/scripts/create_topics.sh"]
