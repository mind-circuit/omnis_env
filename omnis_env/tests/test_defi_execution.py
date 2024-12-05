# omnis/tests/test_defi_execution.py

import unittest
from scripts.defi_execution import execute_defi_strategy
from unittest.mock import patch

class TestDefiExecution(unittest.TestCase):
    @patch('scripts.defi_execution.execute_trade')
    def test_execute_defi_strategy_buy(self, mock_execute_trade):
        prediction = 'BUY'
        execute_defi_strategy(prediction)
        mock_execute_trade.assert_called_with('BUY')

    @patch('scripts.defi_execution.execute_trade')
    def test_execute_defi_strategy_sell(self, mock_execute_trade):
        prediction = 'SELL'
        execute_defi_strategy(prediction)
        mock_execute_trade.assert_called_with('SELL')

if __name__ == '__main__':
    unittest.main()
