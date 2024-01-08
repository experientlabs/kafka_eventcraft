from confluent_kafka import Consumer, KafkaError
import os
import json
from datetime import datetime

BASE_DIRECTORY = "data/message_storage"
# Configure the Kafka consumer
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest',  # Start reading from the beginning of the topic
}

consumer = Consumer(consumer_conf)
consumer.subscribe(['websocket_s3d'])  # Replace 'your_topic' with the actual Kafka topic


def process_and_store_message(message):
    current_time = datetime.now()

    # Build the directory structure based on the timestamp
    directory_path = os.path.join(
        BASE_DIRECTORY,
        current_time.strftime("%Y/%m/%d/%H/%M")
    )

    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)

    # Generate a unique filename based on the timestamp
    filename = current_time.strftime("%S.json")
    file_path = os.path.join(directory_path, filename)

    # Store the message as a JSON file
    with open(file_path, 'w') as file:
        json.dump({"message": message}, file)

    print(f"Stored message in: {file_path}")


def consume_message():
    # Poll for new messages
    try:
        while True:
            msg = consumer.poll(1.0)  # Adjust the timeout as needed
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print(f"Reached end of partition: {msg.partition()}")
                else:
                    print(f"Error: {msg.error()}")
            else:
                # Process and store the received message
                process_and_store_message(msg.value().decode('utf-8'))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == '__main__':
    consume_message()
