'''
File that contains necessary calculations throughout the bot
'''

# Calculate the quantity of coin based on currency paid
def calc_quanity (symbol_price, paid_currency):
    quantity = paid_currency / float(symbol_price)

    return round(quantity, 4)