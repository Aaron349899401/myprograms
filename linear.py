"""
let x represent a string, T be a target charcater to search
let I repres
"""
def str_lin_search(text, target):
    if not text: # same as len(text) == 0
    # checks if text is empty
        return -1
    else:
        i = 0
        while i < len(text):
            if text[i] == target:
                return i
            i += 1
        return -1 # declares something wasn't found

print("Jasper... where is p?", str_lin_search("Jasper", "p"))