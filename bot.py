'''
Main file that runs the entire algorithm and UI
'''

from api.api import *
from algo import buy_algo, sell_algo
import threading

query = ''
buy_thread = threading.Thread(target=buy_algo) # Running the trading algorithm in the background
sell_thread = threading.Thread(target=sell_algo) # Runing the selling algorithm continiously
buy_thread.daemon = True
sell_thread.daemon = True
buy_thread.start()
sell_thread.start()

print("Welcome to Robinhood Trader Control!")

while True:
    pass