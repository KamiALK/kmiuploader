# consumer/consumer.py
from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import functions.descarga
from confluent_kafka.admin import AdminClient, NewTopic


# def create_consumer():
#     conf = {
#         "bootstrap.servers": "kafka:9092",
#         "group.id": "mygroup",
#         "auto.offset.reset": "earliest",
#     }
# return Consumer(conf)


def create_consumer():
    conf = {
        "bootstrap.servers": "kafka:9092",
        "group.id": "mygroup",
        "client.id": "myclientid",
        "enable.auto.commit": True,
        "auto.commit.interval.ms": 1000,
        "session.timeout.ms": 6000,
        # "auto.offset.reset": "earliest",
        "default.topic.config": {"auto.offset.reset": "earliest"},
    }
    return Consumer(conf)


def process_message(message):
    try:
        data = json.loads(message)
        # Obtener la última entrada del diccionario
        last_entry = list(data.items())[-1]
        key, value = last_entry

        if key == "1":
            # print("Entro exitosamente a la opción 1")
            functions.descarga.descargar_videos(value)
        elif key == "2":
            # print("Entro exitosamente a la opción 2")
            functions.descarga.descargar_audios(value)
        elif key == "3":
            # print("Entro exitosamente a la opción 3")
            functions.descarga.descargar_playlist(value)
        elif key == "4":
            # print("Entro exitosamente a la opción 4")
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
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            # print(f'Received message: {msg.value().decode("utf-8")}')
            process_message(msg.value().decode("utf-8"))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    consumer = create_consumer()
    consume_messages(consumer, ["prueba"])
