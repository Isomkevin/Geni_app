import os
from flask import Flask, request
import json
from ussd_generator import ussd_menu

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to Geni'

# JSON configuration for response logic
response_options = ussd_menu
response_options2 = {
    "": {
        "res": "CON What would you want to check \n1. My Account \n2. My phone number"
    },
    "1": {
        "res": "CON Choose account information you want to view \n1. Account number"
    },
    "2": {
        "res": "END Your phone number is {phone_number}"
    },
    "1*1": {
        "res": "END Your account number is {account_number}"
    },
    "default": {
        "res": "END Invalid choice"
    }
}

@app.route("/welcome", methods=['GET'])
def welcome():
    response_text = "Hello World"
    return response_text

@app.route("/ussd", methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    # Get the response configuration based on the received text
    response_config = response_options.get(text, response_options['default'])
    response_text = response_config['res']

    # Process response text if placeholders are present
    if '{phone_number}' in response_text:
        response_text = response_text.format(phone_number=phone_number)
    if '{account_number}' in response_text:
        # Hardcoded account number for demonstration
        account_number = "ACC1001" # Query Backend
        response_text = response_text.format(account_number=account_number)

    return response_text

if __name__ == '__main__':
    app.run()
