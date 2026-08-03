import re

text = "My email is student123@gmail.com and my phone number is 9876543210."

# Search for email
email = re.search(r'\S+@\S+', text)

# Search for 10-digit phone number
phone = re.search(r'\d{10}', text)

if email:
    print("Email Found:", email.group())

if phone:
    print("Phone Number Found:", phone.group())