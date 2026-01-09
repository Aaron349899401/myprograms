# import sys

# input_stuff = sys.stdin.read().strip()

# dih = {}

# for char in input_stuff:
#     dih[char] = dih.get(char, 0) + 1

# for key, value in sorted(dih.items()):
#     print(f"{key} {value}")




# Attempt 2
# Success!: no mistakes, but my code is more chunky than the original
# nevermind, 1 mistake: forgot to .split() the input
# .get() is awesome, if the key is not found, it returns a default value: .get(key, {default value})
# should have used .get(), doesn't really count as a mistake though
def brohemian(rhapsody):
    dih = {}
    for index in range(len(rhapsody)):
        if rhapsody[index] == rhapsody[index-1]:
            dih[rhapsody[index]] += 1
        else:
            dih[rhapsody[index]] = 1
    return dih

rhapsody = "aaabbccd"
result = brohemian(rhapsody)
for key, value in result.items():
    print(f"{key}: {value}")