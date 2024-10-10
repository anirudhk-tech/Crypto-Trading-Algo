'''
Main file that runs the entire algorithm and UI
'''

from api.api import *
from algo import run_algo
import threading

query = ''
algo_thread = threading.Thread(target=run_algo) # Running the trading algorithm in the background
algo_thread.daemon = True # Makes sure background task ends when program quits
algo_thread.start()

print("Welcome to Robinhood Trader Control!")

while True:
    pass