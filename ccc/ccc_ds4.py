def bruh(arr):
    count = 0
    pairs = {}
    maxi = len(arr)
    i = 0
    while i < maxi-1:
        for j in range(i, maxi):
            if arr[j] == arr[i] and j not in pairs:
                count += 1
                pairs[j] = i
        i += 1
    return count

inputty = "1 2 1 1 2"
arr = list(map(int, inputty.split()))
print(bruh(arr))