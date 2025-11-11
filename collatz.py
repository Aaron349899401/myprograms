def collatz_leng(num):
    leng = 1
    place = num
    while place > 1:
        if place not in cache:
            if place % 2 == 0:
                place //= 2
            else:
                place *= 3
                place += 1
            leng += 1
            cache[num] = leng
    return leng

max_leng = 0
corresponding_key = 0
cache = {}

for num in range(1, 1000000):
    result = collatz_leng(num)
    if result > max_leng:
        max_leng = result
        corresponding_key = num
print(f"{corresponding_key}: {max_leng}")