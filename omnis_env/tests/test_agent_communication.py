# omnis/tests/test_agent_communication.py

import unittest
from agents.agent import Agent
from unittest.mock import patch

class TestAgentCommunication(unittest.TestCase):
    @patch('agents.agent.pika.BlockingConnection')
    def test_send_data(self, mock_connection):
        agent = Agent('TestAgent')
        agent.send_data({'test': 'data'})
        self.assertTrue(mock_connection.called)

    @patch('agents.agent.pika.BlockingConnection')
    def test_receive_instructions(self, mock_connection):
        agent = Agent('TestAgent')
        with patch.object(agent.channel, 'start_consuming', return_value=None):
            agent.receive_instructions()
            self.assertTrue(agent.channel.start_consuming.called)

if __name__ == '__main__':
    unittest.main()
