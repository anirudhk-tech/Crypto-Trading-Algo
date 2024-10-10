'''
File to turn requested APIs into secure keys
'''

import os
import ed25519
import base64
import time
import json
from dotenv import load_dotenv

load_dotenv()

public = os.environ.get('PUBLIC_KEY')
private = os.environ.get('PRIV_KEY')
key = os.environ.get('API_KEY')

def sign_key (url, method, time_stamp, body=None):
    path = url.split('.com')[1]

    private_byte = base64.b64decode(private)
    public_byte = base64.b64decode(public)

    private_key = ed25519.SigningKey(private_byte)
    public_key = ed25519.VerifyingKey(public_byte)

    if body:
        message = f'{key}{time_stamp}{path}{method}{str(body)}' 
    else:
        message = f'{key}{time_stamp}{path}{method}' 

    signature = private_key.sign(message.encode('utf-8'))
    base64_signature = base64.b64encode(signature).decode('utf-8')
    public_key.verify(signature, message.encode('utf-8'))

    return base64_signature