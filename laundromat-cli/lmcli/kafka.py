from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic



def create_topic_cmd(topic, servers='localhost:19092'):
  # Create an AdminClient with the given servers.
  admin_client = AdminClient({'bootstrap.servers': servers})
  # Create a new topic.
  create_topic(topic, admin_client)

def delete_topic_cmd(topic, servers='localhost:19092'):
  # Create AdminClient object
  admin_client = AdminClient({'bootstrap.servers': servers})
  # Delete topic
  delete_topic(topic, admin_client)

def check_topic_cmd(topic, servers='localhost:19092'):
  # Create AdminClient object
  admin_client = AdminClient({'bootstrap.servers': servers})

  # Check if topic exists
  check_topic(topic, admin_client)

def create_topic(topic, admclient):
  # Create a new topic.
  new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1)]
  #check if topic exists
  if check_topic(topic, admclient):
    print(f"Topic {topic} already exists")
    return
  # Create the topic. This is an asynchronous operation.
  futures = admclient.create_topics(new_topics)
  # Wait for the topic to be created.
  for topic, future in futures.items():
    try:
      future.result()  # The result itself is None
      print("Topic {} created".format(topic))
    except Exception as e:
      print("Failed to create topic {}: {}".format(topic, e))

def delete_topic(topic, admclient):
  #check if topic exists
  if not check_topic(topic, admclient):
    return
  # Delete topic
  fs = admclient.delete_topics([topic], operation_timeout=30)
  # Wait for each operation to finish
  for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} deleted".format(topic))
    except Exception as e:
        print("Failed to delete topic {}: {}".format(topic, e))

def check_topic(topic, admclient):
  # Check if topic exists
  topic_metadata = admclient.list_topics(timeout=10)
  if topic in set(t.topic for t in iter(topic_metadata.topics.values())):
    print(f"Topic {topic} exists")
    return True
  else:
    print(f"Topic {topic} does not exist")
    return False

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