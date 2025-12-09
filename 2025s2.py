def youre(buns, target):
    bun = []
    nums = 0
    for i in range(1, len(buns), 2):
        if buns[i].isdigit():
            count = 0
            pee = int(buns[i])
            nums += pee
            while count < pee:
                bun.append(buns[i-1])
                count += 1
        else:
            bun.append(buns[i])
    while True:
        try:
            return bun[target]
        except IndexError:
            if target > nums:
                target -= nums
            else:
                None

buns = "r2d2"
target = 8
print(youre(buns, target))

