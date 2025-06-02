import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = os.environ['ALPHA_VANTAGE_API_KEY']
BASE_URL = 'https://www.alphavantage.co/query'


#List of India NSE Top 15 by market capitalization stock symbols
nifty_15_stocks = [
    "RELIANCE.BSE", "HDFCBANK.BSE", "TCS.BSE", "BHARTIARTL.BSE", "ICICIBANK.BSE",
    "SBIN.BSE", "INFY.BSE", "BAJFINANCE.BSE", "HINDUNILVR.BSE", "ITC.BSE",
    "LICI.BSE", "LT.BSE", "KOTAKBANK.BSE", "SUNPHARMA.BSE", "HCLTECH.BSE"
]

for element in nifty_15_stocks:
    symbol = element
    print(f"Fetching data for {symbol}...")

    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        pd.json_normalize(data['Time Series (Daily)']).to_csv(f"{symbol}_daily_data.csv")

        print(f"Data for {symbol} saved successfully.")
    else:
        print(f"Error fetching data for {symbol}: {response.status_code}")

    

