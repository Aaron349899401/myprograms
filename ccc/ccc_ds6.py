def substrings(string):
    seen = set()
    for i in range(len(string) - 2):
        seen.add(string[i:i+3])
    return len(seen)

string = "ababa"
print(substrings(string))