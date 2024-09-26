'''
The central file that runs the trading algorithm.
The bot is running a simple price comparison.
'''

import time
from data.fetch_data import fetch_time_period, change_price, change_diff, fetch_previous_prices, fetch_thresholds
from api.api import fetch_price_details

# Function to compare current prices to previous prices
def price_compare ():
    prev_prices = fetch_previous_prices()
    coin_prices = fetch_price_details()

    for coin in coin_prices:
        diff = coin_prices[coin] - prev_prices[coin]['last_price'] # Current - Previous price
        change_diff(coin, diff) # Changing trend data JSON
        decide_crypto_action(coin, diff) # Deciding whether to buy or sell
    
    for coin in coin_prices: # Updating prices
        change_price(coin, coin_prices[coin])

# Function that decides whether to buy/sell/hold the crypto
def decide_crypto_action (coin, diff):
    coin_prices = fetch_price_details()
    thresholds = fetch_thresholds(coin)
    if diff < 0:
        if abs(diff) >= coin_prices[coin] * thresholds['buy']:
            print('BUY! ', coin)
        else:
            print('HOLD. ', coin)
    elif diff == 0:
        print('HOLD. ', coin)
    else:
        if diff >= coin_prices[coin] * thresholds['sell']:
            print('SELL! ', coin)
        else:
            print('HOLD. ', coin)
    
    print("\nCurrent difference: ", diff)
    print("BUY when under: ", coin_prices[coin] * thresholds['buy'])
    print("SELL when over: ", coin_prices[coin] * thresholds['sell'], "\n")
    
# Main Function that runs the algorithm
def run_algo ():
    prev_prices = fetch_price_details() # Initializing starting prices
    time_period = fetch_time_period() # Fetching time interval for monitoring

    while True:
        price_compare()
        time.sleep(time_period)