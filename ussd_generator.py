# ussd_generator.py

# Example mapping from flowchart states to USSD format
ussd_mapping = {
    "": "CON What would you want to check \n1. My Account \n2. My phone number",
    "1": "CON Choose account information you want to view \n1. Account number",
    "2": "END Your phone number is {phone_number}",
    "1*1": "END Your account number is {account_number}",
    "Invalid": "END Invalid choice"
}

# Function to create USSD menu from the mapping
def create_ussd_menu(mapping):
    ussd_menu = {}
    for key, value in mapping.items():
        ussd_menu[key] = {"res": value}
    return ussd_menu

# Generate USSD menu format
ussd_menu = create_ussd_menu(ussd_mapping)

if __name__ == "__main__":
    print(ussd_menu)  # This will print the generated USSD menu when ussd_generator.py is executed directly
