# omnis/scripts/data_pipeline.py

import yfinance as yf
import pandas as pd
import os

def fetch_market_data(ticker, period='5y', interval='1h'):
    data = yf.download(ticker, period=period, interval=interval)
    data.reset_index(inplace=True)
    data.to_csv(f'data/{ticker}.csv', index=False)
    print(f"Data for {ticker} saved to data/{ticker}.csv")

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    fetch_market_data('BTC-USD')
    fetch_market_data('ETH-USD')
