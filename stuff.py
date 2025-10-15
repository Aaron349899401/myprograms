text = input("Enter your stuff: ")

def cleaner(text):
    while
    for i in len(text):
        list = []
        if i.islower():
            text = text.replace(i, "")
        elif i in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
            if text[i+1] in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}:
                for someting in i:
                    list.append(int(someting))
                    poopoo = sum(list)
            text = text.replace(i, f"{poopoo}")
    return text

result = cleaner(text)
print(result)
