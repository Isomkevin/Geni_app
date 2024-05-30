
import json
import os

from flask import Flask, redirect, request

app = Flask(__name__)


# Load JSON configuration for response logic from external file
with open('response_options.json', 'r') as file:
    response_options = json.load(file)


@app.route('/')
def hello_world():
    return redirect("/welcome")

@app.route("/welcome", methods=['GET'])
def welcome():
    response_text = "<h2>Karibuni Beneficiaries<h2>,\n <p>Welcome to the SustainAShare App<p/>"
    return response_text

@app.route("/ussd", methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    Geni_points = int(1)

    # Get the response configuration based on the received text
    response_config = response_options.get(text, response_options['default'])
    response_text = response_config['res']

    # Process response text if placeholders are present
    if '{phone_number}' in response_text:
        response_text = response_text.format(phone_number=phone_number)
    if '{customer_name}' in response_text:
        response_text = response_text.format(customer_name=phone_number)
    if '{Geni_points}' in response_text:
        response_text = response_text.format(Geni_points=Geni_points) 
    if '{account_number}' in response_text:
        # Hardcoded account number for demonstration
        account_number = "ACC1001" # Query Backend
        response_text = response_text.format(account_number=account_number)

    return response_text

if __name__ == '__main__':
    app.run()
