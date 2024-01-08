from confluent_kafka.admin import AdminClient, NewTopic


def create_kafka_topic(bootstrap_servers, topic_name, partitions=1, replication_factor=1):
    # Configure the AdminClient with the Kafka bootstrap servers
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Create a NewTopic object with the desired topic configuration
    new_topic = NewTopic(topic_name, num_partitions=partitions, replication_factor=replication_factor)

    # Create the topic using the AdminClient.create_topics method
    admin_client.create_topics([new_topic])

    # Wait for the topic creation to complete
    admin_client.poll(timeout=5)


def list_kafka_topics(bootstrap_servers):
    # Configure the AdminClient with the Kafka bootstrap servers
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Use the list_topics method to retrieve the list of topics
    topics_metadata = admin_client.list_topics(timeout=5)

    # Extract the topic names from the metadata
    topic_names = [topic for topic, metadata in topics_metadata.topics.items()]

    # Print the list of topics
    print("Existing Kafka topics:")
    for topic_name in topic_names:
        print(topic_name)


if __name__ == "__main__":
    # Define Kafka bootstrap servers and topic information
    kafka_bootstrap_servers = "localhost:9092"
    topic_to_create = "example_topic"
    num_partitions = 3
    replication_factor = 1

    # Call the function to create the Kafka topic
    # create_kafka_topic(kafka_bootstrap_servers, topic_to_create, num_partitions, replication_factor)
    # print(f"Kafka topic '{topic_to_create}' created successfully.")

    list_kafka_topics(kafka_bootstrap_servers)
