def count(text):
    dih = {}
    for char in text:
        if char in dih: # you need TO INITIALIZE THE KEY BEFORE YOU DO ANYTHING WITH IT!
            dih[char] += 1
        else:
            dih[char] = 1 # INITIALIZING KEY
    result = ""
    for key, value in dih.items():
        result += key + str(value)
    return result

text = input("Enter your text thingy: ")
print(count(text))
