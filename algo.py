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
                # place_sell_order(symbol, holding['quantity']) # Selling crypto that has increased in value
                delete_holdings(symbol, holding['price_bought'], holding['quantity'])
                print(f"{holding['quanity']} {symbol} sold at {best_bid}")
            else:
                print(f"Best bid {best_bid} is lower than price bought {holding['price_bought']}")

def buy (symbol):
    holdings = fetch_holdings(symbol)
    buy_threshold = fetch_buy_threshold()
    
    if len(holdings) <= 3: # Only buy up to 3 holdings
        price = fetch_ask_price(symbol)
        quantity = buy_threshold/float(price)
        print(f"{quantity} {symbol} bought at {price}")
        
    
# Main Function that runs the algorithm
def run_algo ():
    time_period = fetch_time_period()
    symbols = fetch_symbols()
    while True:
        stocks_to_sell = price_compare() # Comparing already bought stocks to see if sell
        for symbol in symbols: # Buying crypto listed
            buy(symbol)
        
        time.sleep(time_period)