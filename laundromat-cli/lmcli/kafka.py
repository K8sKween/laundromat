from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

def send_message(topic, value, servers='localhost:19092'):
    # Create a producer
    producer = Producer({'bootstrap.servers': servers})

    # Send the message
    producer.produce(topic, value=value)

    # Wait until the message is sent
    producer.flush()

def consume_messages(topic, servers='localhost:19092'):
    # Create a Kafka consumer
    consumer = Consumer({
      'bootstrap.servers': servers,
      'group.id': 'laundromat-cli',
      'auto.offset.reset': 'earliest'
    })

    # Subscribe to a Kafka topic
    consumer.subscribe([topic])

    # Consume messages from the Kafka topic
    while True:
      msg = consumer.poll(1.0)

      # If the message is None, continue to the next message
      if msg is None:
        continue

      # If there is an error, print it
      if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

      # If the message is a tombstone, move on to the next message
      if msg.value() is None:
        print("Received tombstone, moving on...")
        continue

      # Otherwise, print the message
      print(f"Received message: {msg.value().decode('utf-8')}")

def create_topic(topic, servers='localhost:19092'):
  # Create an AdminClient with the given servers.
  admin_client = AdminClient({'bootstrap.servers': servers})
  # Create a new topic.
  new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1)]
  # Create the topic. This is an asynchronous operation.
  futures = admin_client.create_topics(new_topics)
  # Wait for the topic to be created.
  for topic, future in futures.items():
    try:
      future.result()  # The result itself is None
      print("Topic {} created".format(topic))
    except Exception as e:
      print("Failed to create topic {}: {}".format(topic, e))

def delete_topic(topic, servers='localhost:19092'):
  # Create AdminClient object
  admin_client = AdminClient({'bootstrap.servers': servers})

  # Delete topic
  fs = admin_client.delete_topics([topic], operation_timeout=30)

  # Wait for each operation to finish
  for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} deleted".format(topic))
    except Exception as e:
        print("Failed to delete topic {}: {}".format(topic, e))

