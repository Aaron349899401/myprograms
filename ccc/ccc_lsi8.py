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



# attempt 2
# 2 mistakes: I did "if char in text" rather than "in dih"; "I didn't output the string correctly"
# also, you should name your dictionaries "my_dih"

def compress(text):
    dih = {}
    for char in text:
        if char in dih:
            dih[char] += 1
        else:
            dih[char] = 1
    return dih
text = "aaabbc"
res = compress(text)
thing = "".join(f"{key}{value}" for key, value in res.items())
print(thing)