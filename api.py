'''
Connecting file between RobinHood API and program. Sending orders, fetching data, and other functions.
'''

import requests
import os
import time
from dotenv import load_dotenv
from signature import sign_key
from printer import *

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
        print_account_details(res.json())
        
    else:
        print("Error:", res.text)
        return None

# Function to fetch data on prices
def fetch_price_details (symbol):
    url = f'https://trading.robinhood.com/api/v1/crypto/marketdata/best_bid_ask/?symbol={symbol}'
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
        print_price_details(res.json())
        
    else:
        print("Error: ", res.text)
        return None