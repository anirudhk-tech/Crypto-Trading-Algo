'''
The central file that runs the trading algorithm.
The bot is running a simple price comparison.
'''

import time
from data.data import fetch_time_period, fetch_symbols, fetch_holdings, delete_holdings, fetch_buy_threshold
from api.api import fetch_bid_price, fetch_ask_price, place_buy_order, place_sell_order

# Tracking --------------------------------------------------------------------------------------------------------
def price_compare ():
    symbols = fetch_symbols()

    for symbol in symbols:
        holdings = fetch_holdings(symbol)
        best_bid = fetch_bid_price(symbol)
        for holding in holdings:
            if best_bid > float(holding['price_bought']):
                place_sell_order(symbol, holding['quantity']) # Selling crypto that has increased in value
                delete_holdings(symbol, holding['price_bought'], holding['quantity'])
            else:
                print(f"Best bid {best_bid} is lower than price bought ${holding['price_bought']}")

def buy (symbol):
    holdings = fetch_holdings(symbol)
    symbols = fetch_symbols()
    if len(holdings) < 3: # Only buy up to 3 holdings
        buy_threshold = fetch_buy_threshold()        
        for symbol in symbols:
            place_buy_order(symbol, buy_threshold) # Buying 10 cents of crypto
        
    
# Main Function that runs the buying algorithm
def buy_algo ():
    time_period = fetch_time_period()
    symbols = fetch_symbols()
    while True:
        for symbol in symbols: # Buying crypto listed
            buy(symbol)
        
        time.sleep(time_period)

# Main Function that runs the selling algorithm
def sell_algo():
    while True:
        price_compare()
        time.sleep(120)