# omnis/tests/test_transformer_model.py

import unittest
from models.transformer_model import TimeSeriesTransformer

class TestTransformerModel(unittest.TestCase):
    def test_model_forward_pass(self):
        model = TimeSeriesTransformer(input_size=1)
        import torch
        input_tensor = torch.randn(10, 60, 1)  # Batch size 10, sequence length 60
        output = model(input_tensor)
        self.assertEqual(output.shape, (10, 60, 1))

if __name__ == '__main__':
    unittest.main()
