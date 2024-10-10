'''
Connecting file between Robinhood API and program. Sending orders, fetching data, and other functions.
'''

import requests
import os
import json
import time
import uuid
from dotenv import load_dotenv
from auth.signature import sign_key
from data.data import *
from calcs import calc_quanity

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
        'x-signature': sign_key(url, time_stamp, method),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        return res.json()
        
    else:
        print("Error:", res.text)
        return None

# Function to fetch data on buy prices
def fetch_ask_price (symbol):
    url = f'https://trading.robinhood.com/api/v1/crypto/marketdata/best_bid_ask/?symbol={symbol}&side=ask'
    method = 'GET'
    time_stamp = str(int(time.time()))
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method, time_stamp),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.get(url, headers=headers)
    
    if res.status_code == 200:
        data = res.json()
        return data['results'][0]['price']
                
    else:
        print("Error: ", res.text)
        return None

# Function to fetch data on sell prices
def fetch_bid_price (symbol):
    url = f'https://trading.robinhood.com/api/v1/crypto/marketdata/best_bid_ask/?symbol={symbol}&side=bid'
    method = 'GET'
    time_stamp = str(int(time.time()))
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method, time_stamp),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.get(url, headers=headers)
    
    if res.status_code == 200:
        data = res.json()
        return round(float(data['results'][0]['price']), 4)
                
    else:
        print("Error: ", res.text)
        return None

# Function that places a buy order
def place_buy_order (symbol, paid_currency):
    url = f'https://trading.robinhood.com/api/v1/crypto/trading/orders/'
    method = 'POST'
    time_stamp = str(int(time.time()))
    symbol_price = fetch_ask_price(symbol)
    symbol_quantity = calc_quanity(symbol_price, paid_currency)
    data = {
        'client_order_id': str(uuid.uuid4()), # Random ID to prevent duplicates
        'side': 'buy',
        'symbol': symbol,
        'type': 'market',
        'market_order_config': {
            'asset_quantity': str(symbol_quantity)
        },
    }
    json_data = json.dumps(data)
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method, time_stamp, body=json_data),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.post(url, headers=headers, data=json_data)

    if res.status_code == 201:
        print(f"Buy order for {symbol_quantity} {symbol} placed at {time_stamp}")
        change_holdings(symbol, symbol_quantity, symbol_price)
                
    else:
        print("Error: ", res.text)

# Function that places a sell order
def place_sell_order (symbol, symbol_quantity):
    url = f'https://trading.robinhood.com/api/v1/crypto/trading/orders/'
    method = 'POST'
    time_stamp = str(int(time.time()))
    symbol_price = fetch_bid_price(symbol)

    data = {
        'client_order_id': str(uuid.uuid4()), # Random ID to prevent duplicates
        'side': 'sell',
        'symbol': symbol,
        'type': 'market',
        'market_order_config': {
            'asset_quantity': symbol_quantity
        },
    }
    json_data = json.dumps(data)
    headers = {
        'x-api-key': key,
        'x-timestamp': time_stamp,
        'x-signature': sign_key(url, method, time_stamp, body=json_data),
        'Content-Type': 'application/json; charset=utf-8',
    }

    res = requests.post(url, headers=headers, data=json_data)

    if res.status_code == 201:
        print(f"Sell order for {symbol_quantity} {symbol} placed at {time_stamp}")
                
    else:
        print("Error: ", res.text)