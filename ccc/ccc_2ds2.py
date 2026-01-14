def repeat_checker(string_list):
    freq = {}
    for string in string_list:
        freq[string] = freq.get(string, 0) + 1
    maxi = max(freq.values())
    if maxi >= 2:
        return "YES"
    return "NO"

N = int(input("Enter your number of strings: "))
string_list = []
for _ in range(N):
    string_list.append(input("Enter your string: "))

print(repeat_checker(string_list))