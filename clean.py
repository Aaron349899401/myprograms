# cleaning a string
import re
def clean(text):
    result = re.findall(r"[a-zA-Z ]", text)
    return "".join(result)

text = input("Enter you text: ")
poop = clean(text)
best_poop = re.sub(r"\s+", " ", poop).strip()
print(best_poop)