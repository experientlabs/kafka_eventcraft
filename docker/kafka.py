from confluent_kafka import Producer, Consumer

# Kafka producer example
producer = Producer({'bootstrap.servers': 'localhost:9092'})
producer.produce('my_topic', key='key', value='value')
producer.flush()

# Kafka consumer example
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['my_topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
    else:
        print(f"Received message: {msg.value().decode('utf-8')}")
