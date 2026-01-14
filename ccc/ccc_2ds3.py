# my solution:
def anagram(a, b):
    freq_a = {}
    freq_b = {}
    for char in a:
        freq_a[char] = freq_a.get(char, 0) + 1
    for char in b:
        freq_b[char] = freq_b.get(char, 0) + 1
    if freq_a == freq_b:
        return "YES"
    return "NO"

# Copilot solution:
def copilot(a, b):
    freq = {}
    for char in a:
        freq[char] = freq.get(char, 0) + 1
    for char in b:
        freq[char] = freq.get(char, 0) - 1
    return "YES" if all(values == 0 for values in freq.values()) else "NO"
    
a = input("Enter your word: ")
b = input("Enter your second word: ")
print(copilot(a, b))