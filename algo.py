'''
The central file that runs the trading algorithm.
The bot is running a simple price comparison.
'''

import time
from data.fetch_data import fetch_time_period, change_price
from api.api import fetch_price_details

time_period = fetch_time_period()
coins_dict = {}

# Function to fetch initial prices
def fetch_prices ():
    coin_prices = fetch_price_details()
    for coin in coin_prices: # Setting initial values on system start up
        coins_dict[coin] = 0.00

# Function to compare current prices to previous prices
def price_compare ():
    coin_prices = fetch_price_details()
    for coin in coins_dict:
        diff = coin_prices[coin] - coins_dict[coin] # Current - previous price
        decide_crypto_action(diff)
        coins_dict[coin] = coin_prices[coin] # Updating prices
    
    for coin in coins_dict:
        change_price(coin, coins_dict[coin])

# Function that decides whether to buy/sell/hold the crypto
def decide_crypto_action (diff):
    if diff > 5:
        print("Hold.")
    elif diff < 0:
        print("Sell!")
    else: 
        print("Buy.")
    
# Main Function that runs the algorithm
def run_algo ():
    fetch_prices()

    while True:
        price_compare()
        time.sleep(time_period)