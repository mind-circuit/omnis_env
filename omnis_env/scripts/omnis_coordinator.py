# omnis/scripts/omnis_coordinator.py

import pika
import json

class OmnisCoordinator:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='omnis_queue')

    def receive_data(self):
        def callback(ch, method, properties, body):
            message = json.loads(body)
            agent = message['agent']
            data = message['data']
            print(f"Received data from {agent}: {data}")
            # Process data and send instructions
            instructions = self.process_data(data)
            self.send_instructions(agent, instructions)

        self.channel.basic_consume(queue='omnis_queue', on_message_callback=callback, auto_ack=True)
        print("OmnisCoordinator waiting for data.")
        self.channel.start_consuming()

    def send_instructions(self, agent, instructions):
        message = json.dumps({'agent': agent, 'instructions': instructions})
        self.channel.basic_publish(exchange='', routing_key='omnis_queue', body=message)
        print(f"Sent instructions to {agent}.")

    def process_data(self, data):
        # Implement data processing logic
        return "Proceed with action X"

if __name__ == "__main__":
    coordinator = OmnisCoordinator()
    coordinator.receive_data()
