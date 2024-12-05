# omnis/models/transformer_model.py

import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class TimeSeriesTransformer(nn.Module):
    def __init__(self, input_size, num_layers=3, d_model=128, nhead=8, dim_feedforward=512):
        super(TimeSeriesTransformer, self).__init__()
        self.model_type = 'Transformer'
        self.pos_encoder = nn.Sequential(
            nn.Linear(input_size, d_model),
            nn.ReLU()
        )
        encoder_layers = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_layers)
        self.decoder = nn.Linear(d_model, 1)

    def forward(self, src):
        src = self.pos_encoder(src)
        output = self.transformer_encoder(src)
        output = self.decoder(output)
        return output


def load_data(ticker, look_back=60):
    df = pd.read_csv(f'data/{ticker}.csv')
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))

    sequences = []
    targets = []
    for i in range(len(data) - look_back):
        sequences.append(data[i:i + look_back])
        targets.append(data[i + look_back])

    sequences = torch.FloatTensor(sequences)
    targets = torch.FloatTensor(targets)
    return sequences, targets, scaler


def train_model(ticker):
    sequences, targets, scaler = load_data(ticker)
    model = TimeSeriesTransformer(input_size=1)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    epochs = 20

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(sequences)
        loss = criterion(output.squeeze(), targets)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

    # Save the model and scaler
    torch.save(model.state_dict(), f'models/{ticker}_transformer.pth')
    torch.save(scaler, f'models/{ticker}_scaler.pth')
    print(f"Model and scaler saved for {ticker}.")


if __name__ == "__main__":
    train_model('BTC-USD')
