from logging import exception
from confluent_kafka import Producer


def create_producer():
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
    return Producer(conf)


# Define el mensaje y el topic al que quieres enviarlo


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
        pass
