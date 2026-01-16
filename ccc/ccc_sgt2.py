def pair_sum(arr):
    arr = sorted(arr)
    n = len(arr)
    max_pair = 0
    for i in range(n // 2):
        pair = arr[i] + arr[n - 1 - i]
        max_pair = max(max_pair, pair)
    return max_pair

arr = [1, 3, 5, 9]
print(pair_sum(arr))