import typer
from lmcli.commands import *
from lmcli.kafka import *

app = typer.Typer()

#Laundromat Commands


#Laundromat Setup Commands
@app.command()
def check_topics(name: str):
  return

@app.command()
def create_topics(name: str):
  return

@app.command()
def create_topics(name: str):
  return

#Kafka Related Commands

@app.command()
def kafka_topic_create(name: str):
  create_topic(name)

@app.command()
def kafka_topic_delete(name: str):
  delete_topic(name)

@app.command()
def kafka_send_message(topic: str, value: str):
  send_message(topic, value)

@app.command()
def kafka_consume_messages(topic: str):
  consume_messages(topic)

if __name__ == "__main__":
  app()