def finn(target):
    solutions = 0
    lih = [0] * target
    for i in range(target):
        for fo in range(i):
            lih[fo] = 4
        for fi in range(i, target):
            lih[fi] = 5
        if sum(lih) == target:
            solutions += 1
    return solutions   

def ccc2022_s1(n):
    count = 0
    # b is the number of 5s
    for b in range(n // 5 + 1):
        remaining = n - 5 * b
        if remaining % 4 == 0:
            count += 1
    return count

target = 14
print(finn(target))