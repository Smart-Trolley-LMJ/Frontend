import re

def validate_phone_number(input_str):
    # Regular expression pattern for a 10-digit phone number
    pattern = r'^\d{10}$'
    return re.match(pattern, input_str) is not None

user_input = input("Enter a 10-digit phone number: ")

# Limit input to 10 characters
user_input = user_input[:10]

if validate_phone_number(user_input):
    print("Valid phone number:", user_input)
else:
    print("Invalid phone number")
