import re
def is_email(text):
    if not text:
        return False
    pattern = r"^[\w\.]+@[\w\.]+\.\w+$"
    return re.match(pattern, text, re.IGNORECASE) is not None

text = input("Enter your email: ")

if is_email(text):
    print("SUCCESS!")
else:
    print("NOPE!")
