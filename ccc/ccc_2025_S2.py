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

cipher = "a4b1c2d10"
target = 100






# Attempt 2
def rle(cipher, target):
    un_cipher = []
    count = ""
    char = ""
    for i in cipher:
        if i.isalpha():
            if char != "":
                un_cipher.append((char, int(count)))
                count = ""
            char = i
        else:
            count += i
    
    if char != "":
        un_cipher.append((char, int(count)))

    length = sum(y for x, y in un_cipher)
    target = target % length
    total = 0
    for char, amount in un_cipher:
        if total + amount >= target:
            return char
        total += amount

cipher = input().strip()
target = int(input())

print(rle(cipher, target))