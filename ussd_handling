def handle_ussd_request(user_input):
    response_config = ussd_menu.get(user_input, ussd_menu['default'])
    response_text = response_config['res']

    if '{phone_number}' in response_text:
        response_text = response_text.format(phone_number="1234567890")  # Replace with actual phone number

    if '{account_number}' in response_text:
        account_number = "ACC1001"  # Replace with actual account number
        response_text = response_text.format(account_number=account_number)

    return response_text
