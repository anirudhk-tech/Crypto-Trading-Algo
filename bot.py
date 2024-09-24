'''
Main file that runs the entire algorithm and UI
'''

from api.api import *
from printer import * 
from algo import run_algo
import threading

query = ''
algo_thread = threading.Thread(target=run_algo) # Running the trading algorithm in the background
algo_thread.daemon = True # Makes sure background task ends when program quits
algo_thread.start()


# Starting menu control for the entire algorithm
def prompt ():
    print("\nWhat would you like to do?\n")
    print("(1) View account details")
    print("(2) View current holdings")
    print("(3) View monitored crypto")
    print("(4) Adjust period of monitoring")
    print("(q) Quit\n")

    global query
    query = input()

print("Welcome to Robinhood Trader Control!")

while query != 'q':
    prompt()

    if query == '1':
        print("\n-----------------------------------------------------")
        results = fetch_account_details()
        print_account_details(results)
        print("-----------------------------------------------------")
    
    if query == '2':
        print("\n-----------------------------------------------------")
        results = fetch_holding_details()
        print_holding_details(results)
        print("-----------------------------------------------------")

    if query == '3':
        print("\n-----------------------------------------------------")
        results = fetch_price_details()
        print_price_details(results)
        print("-----------------------------------------------------")  
    
    if query == '4':
        print("\n-----------------------------------------------------")
        results = fetch_time_details()
        print_time_details(results)
        print("-----------------------------------------------------") 
