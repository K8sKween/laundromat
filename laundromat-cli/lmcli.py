import typer
from lmcli.commands import *
from lmcli.kafka import *
from lmcli.setup import *

app = typer.Typer()

#Laundromat Commands

#Laundromat Setup Commands
@app.command()
def check_setup_topics(file_path: str):
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
  check_setup_topics_cmd(lines)

@app.command()
def create_setup_topics(file_path: str):
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
  create_setup_topics_cmd(lines)

@app.command()
def delete_setup_topics(file_path: str):
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
  delete_setup_topics_cmd(lines)


#Kafka Related Commands

@app.command()
def kafka_topic_create(name: str):
  create_topic_cmd(name)

@app.command()
def kafka_topic_delete(name: str):
  delete_topic_cmd(name)

@app.command()
def kafka_send_message(topic: str, value: str):
  send_message(topic, value)

@app.command()
def kafka_consume_messages(topic: str):
  consume_messages(topic)

@app.command()
def kafka_topic_check(topic: str):
  check_topic_cmd(topic)

if __name__ == "__main__":
  app()