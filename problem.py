wow_list = [1, 1, 2, 3, 4, 5, 6, 9]
target = 6

# method 2
def poop(wow_list, target):
    for x in range(len(wow_list)-1):
        for y in range(x+1, len(wow_list)):
            if x + y == target:
                return True
    return False
# print(poop(wow_list, target))

# method 3
def lin(wow_list, target):
    for value in range(len(wow_list)-1):
        diff = target - wow_list[value]
        for j in range(i+1, len(wow_list)):
            if wow_list[j] == diff:
                return True

# method 3.5
def lin2(wow_list, target):
    for x in wow_list:
        if x != target/2 and any(lambda x: target - x in wow_list)(x):
            return True

# method 3.75
def lin3(wow_list, target):
    result = any(
        (lambda x: target - x in wow_list)(x)
        for x in wow_list
    )
    return result

# print(lin2(wow_list, target))

# method 5
def meth5(wow_list, target):
    h = len(wow_list)-1
    l = 0
    while l < h:
        total = wow_list[l] + wow_list[h]
        if target == total:
            return True
        else:
            if total < target:
                l += 1
            else:
                h -= 1
    return False
print(meth5(wow_list, target))