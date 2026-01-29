def exp(num, ex):
    result = 1
    if ex == 0:
        return 1
    elif ex == 1:
        return num
    else:
        return num * exp(num, ex - 1)

num = 2
ex = 4
print(exp(num, ex))

    