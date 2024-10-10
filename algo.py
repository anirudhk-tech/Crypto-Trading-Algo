'''
The central file that runs the trading algorithm.
The bot is running a simple price comparison.
'''

import time
from data.data import fetch_time_period, fetch_symbols, fetch_holdings, delete_holdings
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
                print(f"Best bid {best_bid} is lower than price bought {holding['price_bought']}")
    
# Main Function that runs the algorithm
def run_algo ():
    time_period = fetch_time_period()
    while True:
        stocks_to_sell = price_compare()
        time.sleep(time_period)