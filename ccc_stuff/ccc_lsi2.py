import sys, re

input_stuff = sys.stdin.read()

word = ""
result = ""
for letter in input_stuff:
    if re.search(r"[a-zA-Z]", letter):
        word += letter
    elif re.search(r"\s", letter):
        word = word[::-1]
        result += word + " "
        word = ""

if word:
    result += word[::-1]

sys.stdout.write(result)