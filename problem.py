wow_list = [1, 1, 2, 3, 4, 5, 6, 9]
target = 6
result = any(
    (lambda x: target - x in wow_list)(x)
    for x in wow_list
)
print(result)
