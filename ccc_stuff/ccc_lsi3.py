import sys

input_stuff = sys.stdin.read().strip()

dih = {}

for char in input_stuff:
    dih[char] = dih.get(char, 0) + 1

for key, value in sorted(dih.items()):
    print(f"{key} {value}")

