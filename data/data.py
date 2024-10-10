'''
Central file that interacts with JSON storage
'''

import json
import time 

with open('data/crypto.json', 'r') as f:
    data = json.load(f)


# POST requests ----------------------------------------------------------------------------------------------------
def change_holdings(symbol, quantity, price):
    new_holding_entry = {
        'quantity': quantity,
        'price_bought': price,
    }
    data['active_crypto'][symbol]['holdings'].append(new_holding_entry)

    with open('data/crypto.json', 'w') as f:
        json.dump(data, f, indent=4)

def delete_holdings(symbol, price_bought, quantity):
    for holding in data['active_crypto'][symbol]['holdings']:
        if holding['price_bought'] == price_bought and holding['quantity'] == quantity:
            data['active_crypto'][symbol]['holdings'].remove(holding)
        
    with open('data/crypto.json', 'w') as f:
        json.dump(data, f, indent=4)
        
# GET requests -----------------------------------------------------------------------------------------------------
def fetch_holdings(symbol):
    return data['active_crypto'][symbol]['holdings']

def fetch_time_period():
    return data['time_period']

def fetch_symbols():
    return data['active_crypto']

def fetch_buy_threshold():
    return data['buy_threshold']