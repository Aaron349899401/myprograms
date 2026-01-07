import re

P = input("Enter pattern: ")
T = input("Enter interable: ")

pattern = fr"(?={re.escape(P)})"
matchs = re.findall(pattern, T)

print(len(matchs))