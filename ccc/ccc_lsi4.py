import re

P = input("Enter pattern: ")
T = input("Enter interable: ")

pattern = fr"(?={re.escape(P)})"
matchs = re.findall(pattern, T)

print(len(matchs))



# attempt 2
# dis one involved a regex thing that i forgot
# its very important, so i should remeber for next time
# the meaning of fr, "?=", re.escape(), which just makes a string in regex form (r"pattern")
# the "?=" allows the patterns to overlap, lookahead, allwoing us to find matches without using up 
# any of the characters before it
def finder(text, target):
    count = 0
    for char in text:
        if target == char:
            count += 1