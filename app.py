import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



app = Flask(__name__)

# JSON configuration for response logic
response_options = {
    "": {
        "res": "CON Welcome to Geni Loyalty program \nLog In as: \n1. Customer \n2. Shop Owner"
    },
    "1": {
        "res": "CON Welcome {Customer_name} \n1. Top up \n2. My Points \n3. Opt out"
    },
    "1*1": {
        "res": "CON Welcome {Customer_name} \n1. Top up \n2. My Points \n3. Opt out"
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
