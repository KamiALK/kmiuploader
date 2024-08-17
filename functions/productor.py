from logging import exception
from confluent_kafka import Producer


def create_producer():
    conf = {
        "bootstrap.servers": "kafka:9092",
        # "client.id": "myclientid",
        # "auto.offset.reset": "earliest",
        # "default.topic.config": {"auto.offset.reset": "earliest"},
    }
    return Producer(conf)


def mensajero_producer(topic, mensaje):
    # llamar a productor
    producer = create_producer()

    try:
        producer.produce(topic, value=mensaje.encode("UTF-8"))
        producer.flush()
        print(f"el video al topic{topic}:envio del mensaje {mensaje}")
    except exception as e:
        print(f"error al enviar al topic {topic}:{str(e)}")

    finally:
        producer.flush()
