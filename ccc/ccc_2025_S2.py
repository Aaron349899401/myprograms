def cipher(output, target):
    char = ""
    cleaned = []
    curr = ""
    for x in output:
        if x.isalpha():
            if curr != "":
                cleaned.append((char, int(curr)))
                curr = ""
            char = x
        else:
            curr += x
    
    if curr != "":
        cleaned.append((char, int(curr)))

    length = sum(count for char, count in cleaned)
    target = (target - 1) % length + 1
    total = 0
    for char, amount in cleaned:
        if total + amount >= target:
            return char
        total += amount
    return None

output = "a4b1c2d10"
target = 100
print(cipher(output, target))