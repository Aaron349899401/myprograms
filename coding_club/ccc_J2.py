def shifty(num, k):
    lih = [num]
    for _ in range(k):
        lih.append(num * 10)
        num = lih[-1]
    return sum(lih)

num = int(input("Enter your number: "))
k = int(input("Enter your number of shifts: "))
print(shifty(num, k))