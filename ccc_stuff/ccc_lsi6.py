def cleaner(text):
    for index in range(1, len(text)):
        if text[index] == text[index-1]:
            text.remove(text[index])
            text.remove(text[index-1])
    return text

text = "abbaca"
print(cleaner(text))
