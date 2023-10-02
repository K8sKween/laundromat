from lmcli.kafka import *


def check_setup_topics_cmd(topics: list[str]):
  for topic in topics:
    check_topic_cmd(topic)

def create_setup_topics_cmd(topics: list[str]):
  for topic in topics:
    create_topic_cmd(topic)

def delete_setup_topics_cmd(topics: list[str]):
  for topic in topics:
    delete_topic_cmd(topic)
