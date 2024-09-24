'''
File that handles all the printing of details in the interface
'''

# Function to print out account details
def print_account_details (data):
    print(f"Account Number: {data['account_number']}")
    print(f"Status: {data['status']}")
    print(f"Buying Power: {round(float(data['buying_power']), 2)} {data['buying_power_currency']}")

# Function to output all the cryptos being monitored
def print_price_details (data):
    print("NAME      |  PRICE (USD)\n")
    for crypto in data:
        whitespace = 10 - len(crypto) # Whitespace creation for even look in terminal
        whitespace_string = "" 

        for x in range(whitespace):
            whitespace_string += " "
        
        print(f"{crypto}{whitespace_string}|  {data[crypto]}")

# Function to output over what period of time the cryptos are being monitored
def print_time_details (time_period):
    print(f"The trader is checking every {time_period} SECONDS for changes in currency")

# Function to output the amount of holdings of each crypto
def print_holding_details (data):
    print("NAME      |  HOLDING (USD)\n")
    for crypto in data:
        whitespace = 10 - len(crypto) # Whitespace creation for even look in terminal
        whitespace_string = "" 

        for x in range(whitespace):
            whitespace_string += " "
        
        print(f"{crypto}{whitespace_string}|  {data[crypto]}")