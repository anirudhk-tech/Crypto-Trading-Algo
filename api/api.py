'''
Connecting file between RobinHood API and program. Sending orders, fetching data, and other functions.
'''

import requests
import os
import time
from dotenv import load_dotenv
from auth.signature import sign_key
from data.fetch_data import *

load_dotenv()

key = os.environ.get('API_KEY')

# Function to fetch data regarding personal Robinhood account
def fetch_account_details ():
    url = 'https://trading.robinhood.com/api/v1/crypto/trading/accounts/'
    method = 'GET'
    time_stamp = str(int(time.time()))
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.json()
        
    else:
        print("Error:", res.text)
        return None

# Function to fetch data on prices
def fetch_price_details ():
    symbols = fetch_symbols() 
    url = f'https://trading.robinhood.com/api/v1/crypto/marketdata/best_bid_ask/?symbol={symbols}&side=ask'
    method = 'GET'
    time_stamp = str(int(time.time()))
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method),
        'Content-Type': 'application/json; charset=utf-8',
    }
    results = {}

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        for crypto in data['results']:
            results[crypto['symbol']] = float(crypto['price'])
        
        return results
        
    else:
        print("Error: ", res.text)
        return None

# Function that fetches the time period that the bot monitors the crypto
def fetch_time_details():
    time_period = fetch_time_period()
    return time_period

# Function that fetches details on how many stocks user owns
def fetch_holding_details():
    holdings = fetch_crypto_holdings()
    return holdings

# Function that fetches the thresholds for buy and sell
def fetch_threshold_details():
    buy_sell = fetch_thresholds()
    return buy_sell