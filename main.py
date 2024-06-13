import functions.descarga
import json

# consumer/consumer.py
from confluent_kafka import Consumer, KafkaException, Message

functions.descarga.descargar_videos("https://youtu.be/_Yhyp-_hX2s?si=BDwgIiGMnEJrteR5")


def create_consumer():
    conf = {
        "bootstrap.servers": "kafka:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
    return Consumer(conf)


def process_message(message):
    try:
        data = json.loads(message)
        # Obtener la última entrada del diccionario
        last_entry = list(data.items())[-1]
        key, value = last_entry
        # print("este es data key", key)
        # print("este es data value", value)

        # Realizar el procesamiento basado en el primer parámetro
        if key == "1":
            print("entro exitosamente")
            functions.descarga.descargar_videos(value)
        elif key == "2":
            functions.descarga.descargar_audios(value)
        elif key == "3":
            functions.descarga.descargar_playlist(value)

        elif key == "4":
            functions.descarga.descargar_series(value)
        else:
            print(f"Clave {key} no reconocida")

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("Error processing message:", e)


def consume_messages(consumer, topics):
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            # print(f'Received message: {msg.value().decode("utf-8")}')
            # Decodificar el mensaje JSON
            # Obtener la clave y el valor
            # print(msg.value().decode("utf-8"), "aqui estoy imprimiendo valores")
            process_message(msg.value().decode("utf-8"))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    consumer = create_consumer()
    consume_messages(consumer, ["prueba"])
