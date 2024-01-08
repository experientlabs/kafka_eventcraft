import asyncio
import websockets
from confluent_kafka import Producer, KafkaException
from confluent_kafka.admin import AdminClient
from utils.create_topic import create_kafka_topic


def produce_to_kafka(bootstrap_servers, topic, event_data):
    # Configure the AdminClient with the Kafka bootstrap servers
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Check if the topic already exists
    if topic not in admin_client.list_topics().topics:
        # If the topic does not exist, create it
        create_kafka_topic(bootstrap_servers, topic, partitions=1, replication_factor=1)

    # Create a Kafka producer
    producer = Producer({"bootstrap.servers": bootstrap_servers})

    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

    try:
        # Produce to the specified topic
        producer.produce(topic, key=None, value=event_data, callback=delivery_report)
        producer.poll(0)  # Trigger any message callbacks
    except KafkaException as e:
        if e.args[0].code() == KafkaException._PARTITION_EOF:
            print(f"Topic '{topic}' not found. Failed to produce message.")
        else:
            raise
    finally:
        # Flush the producer and close the AdminClient
        producer.flush()


async def consume_websocket_and_produce_to_kafka(bootstrap_servers, url, kafka_topic):
    async with websockets.connect(url) as websocket:
        while True:
            event_data = await websocket.recv()
            produce_to_kafka(bootstrap_servers, kafka_topic, event_data)


if __name__ == '__main__':
    url = "ws://0.0.0.0:8765"
    kafka_topic = "websocket_s3d"
    bootstrap_servers = "localhost:9092"
    # Create an event loop and run the coroutine within it
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume_websocket_and_produce_to_kafka(bootstrap_servers, url, kafka_topic))

