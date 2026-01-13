def first_occurence(string):
    first = {}
    result = []
    for index, char in enumerate(string):
        if char not in first:
            first[char] = index
        result.append(first[char])
    return result

string = "abac"
print(first_occurence(string))

# remeber enumerate, what it does