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

target = 14
print(finn(target))