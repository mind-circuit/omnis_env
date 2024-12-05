# omnis/agents/agent.py

import pika
import json

class Agent:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='omnis_queue')

    def send_data(self, data):
        message = json.dumps({'agent': self.agent_name, 'data': data})
        self.channel.basic_publish(exchange='', routing_key='omnis_queue', body=message)
        print(f"{self.agent_name} sent data.")

    def receive_instructions(self):
        def callback(ch, method, properties, body):
            message = json.loads(body)
            if message['agent'] == self.agent_name:
                print(f"{self.agent_name} received instructions: {message['instructions']}")

        self.channel.basic_consume(queue='omnis_queue', on_message_callback=callback, auto_ack=True)
        print(f"{self.agent_name} waiting for instructions.")
        self.channel.start_consuming()

# Simulate agent operation
if __name__ == "__main__":
    agent = Agent('AgentA')
    agent.send_data({'metric': 42})
    agent.receive_instructions()
