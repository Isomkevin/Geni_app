# app.py

from flask import Flask, request
from ussd_main_app import handle_ussd_request
from ussd_generator import ussd_menu

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to Geni'

@app.route("/welcome", methods=['GET'])
def welcome():
    return "Hello World"

@app.route("/ussd", methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    # Handle USSD request using the handle_ussd_request function
    response_text = handle_ussd_request(text)

    return response_text



if __name__ == '__main__':
    app.run()







