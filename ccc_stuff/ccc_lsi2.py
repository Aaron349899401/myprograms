import sys, re

# input_stuff = sys.stdin.read()

# word = ""
# result = ""
# for letter in input_stuff:
#     if re.search(r"[a-zA-Z]", letter):
#         word += letter
#     elif re.search(r"\s", letter):
#         word = word[::-1]
#         result += word + " "
#         word = ""

# if word:
#     result += word[::-1]

# sys.stdout.write(result)

# attempt 2
# 3 mistakes: no if place, didnt return back to places' original value, forgot to add space, 
def reverser(stuff):
    place = ""
    lih = []
    for char in stuff:
        if char == " ":
            lih.append(place[::-1] + " ")
            place = ""
        else:
            place += char
    if place:
        lih.append(place[::-1])
    return "".join(lih)
stuff = "ccc is fun"
print(reverser(stuff))