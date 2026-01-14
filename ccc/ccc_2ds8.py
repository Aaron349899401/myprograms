def distance(arr, k):
    count = {}
    for i, num in enumerate(arr):
        if num in count and i - count[num] <= k:
            return True
        count[num] = i
    return False

arr = [1, 2, 3, 1, 4, 5]
k = 3
print(distance(arr, k))
