import re 
def cleaning(product_codes):
    cleaned = []
    for code in product_codes:
        digits = re.sub(r"[^\d]", "", code)
        letters = re.findall(r"[A-Z]", code)
        summed = str(sum(int(num) for num in digits))
        uppercases = "".join(letters)
        cleaned.append(uppercases + summed)
    return cleaned

product_codes = ["AbC3c2Cd9"]
print(cleaning(product_codes))
        