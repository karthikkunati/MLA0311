import re

# Input text
text = "My name is Karthik. My phone number is 9876543210 and my email is karthik123@gmail.com."

# Search for a phone number
phone = re.search(r"\d{10}", text)

# Search for an email address
email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

# Search for the word 'Karthik'
name = re.search(r"Karthik", text)

print("Input Text:")
print(text)

print("\nSearch Results:")

if name:
    print("Name Found:", name.group())

if phone:
    print("Phone Number:", phone.group())

if email:
    print("Email Address:", email.group())
