# omnis/scripts/update_model.py

from data_pipeline import fetch_market_data
from models.transformer_model import train_model

def update_model(ticker):
    fetch_market_data(ticker)
    train_model(ticker)

if __name__ == "__main__":
    update_model('BTC-USD')
