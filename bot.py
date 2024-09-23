'''
Main file that runs the entire algorithm and UI
'''

from api import *

query = ''


# Starting menu control for the entire algorithm
def prompt ():
    print("\nWhat would you like to do?\n")
    print("(1) View account details")
    print("(q) Quit\n")

    global query
    query = input()

# --------------------------------------------------------

print("Welcome to Robinhood Trader Control!")

while query != 'q':
    prompt()
    if query == '1':
        print("\n-----------------------------------------------------")
        fetch_account_details()
        print("-----------------------------------------------------")
