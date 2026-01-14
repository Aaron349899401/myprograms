def bruh(arr):
    pairs = {}
    for num in arr:
        pairs[num] = pairs.get(num, 0) + 1
    total_count = 0
    for k in pairs.values():
        total_count += k * (k - 1) // 2 
    # we use floor div because normal produces a float and floor produces an int
    return total_count

inputty = "1 2 1 1 2"
arr = list(map(int, inputty.split()))
print(bruh(arr))