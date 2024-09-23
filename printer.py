'''
File that handles all the printing of details in the interface
'''

# Function to print out account details
def print_account_details (data):
    print(f"Account Number: {data['account_number']}")
    print(f"Status: {data['status']}")
    print(f"Buying Power: {round(float(data['buying_power']), 2)} {data['buying_power_currency']}")