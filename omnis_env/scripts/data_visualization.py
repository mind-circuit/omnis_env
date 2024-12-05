# omnis/scripts/data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_market_data(ticker):
    df = pd.read_csv(f'data/{ticker}.csv')
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title(f'{ticker} Market Data')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_model_predictions(ticker):
    # Load actual data and predictions
    df = pd.read_csv(f'data/{ticker}.csv')
    # Assuming predictions are saved in a separate file
    predictions = pd.read_csv(f'data/{ticker}_predictions.csv')

    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Actual Price')
    plt.plot(predictions['Date'], predictions['Predicted'], label='Predicted Price')
    plt.title(f'{ticker} Model Predictions')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_market_data('BTC-USD')
    plot_model_predictions('BTC-USD')
