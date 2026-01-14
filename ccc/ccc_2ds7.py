def diff(integers, target):
    seen = set(integers)
    for num in integers:
        if (num + target) in seen or (num - target) in seen:
            return True
    return False
integers = [1, 7, 5, 9, 2]
target = 4
print(diff(integers, target))