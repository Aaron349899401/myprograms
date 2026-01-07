import sys

S = sys.stdin.read()

a_count = 0
for letter in S:
    if letter == "A":
        a_count += 1

sys.stdout.write(str(a_count))