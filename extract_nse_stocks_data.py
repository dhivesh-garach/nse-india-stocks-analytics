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

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'HDFCBANK.BSE',
    'outputsize': 'full',
    'apikey': API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    print(data) # Check if the response contains the expected data


    

