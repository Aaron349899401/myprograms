dic = {}
def alpha(num):
    lis = []
    for i in range(1, num//2):
        if num % i == 0:
            lis.append(i)
    return lis

num = 16

for key in range(2, num + 1):
    value = alpha(num)
    dic[key] = value

print(dic)
