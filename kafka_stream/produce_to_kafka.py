import asyncio
import websockets
from confluent_kafka import Producer


# Note: Create a Topic Before Producing:
# kafka-topics.sh --create --topic websocket_s3d --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


# async def consume_websocket(url):
#     async with websockets.connect(url) as websocket:
#         while True:
#             event_data = await websocket.recv()
#             # Process or send the data to Kafka here
#             print(f"Received WebSocket event: {event_data}")
#
# asyncio.get_event_loop().run_until_complete(consume_websocket("ws://0.0.0.0:8765"))


def produce_to_kafka(topic, event_data):
    producer = Producer({"bootstrap.servers": "localhost:9092"})

    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

    producer.produce(topic, key=None, value=event_data, callback=delivery_report)
    producer.poll(0)  # Trigger any message callbacks


# Usage within the WebSocket consumer loop:
async def consume_websocket_and_produce_to_kafka(url, kafka_topic):
    async with websockets.connect(url) as websocket:
        while True:
            event_data = await websocket.recv()
            produce_to_kafka(kafka_topic, event_data)


if __name__ == '__main__':
    url = "ws://0.0.0.0:8765"
    kafka_topic = "websocket_s3d"
    # Create an event loop and run the coroutine within it
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume_websocket_and_produce_to_kafka(url, kafka_topic))

