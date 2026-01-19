def min_diff(arr):
    arr.sort()
    diff = {}
    for i in range(1, len(arr)):
        x = arr[i] - arr[i-1]
        if x not in diff:
            diff[(arr[i], arr[i-1])] = x
    return min(diff.values())

# Copilot Solution:
def min_diff(arr):
    arr.sort()
    best = float("inf")
    for i in range(1, len(arr)):
        diff = arr[i] = arr[i-1]
        if diff < best:
            best = diff
    return best
    
arr = list(map(int, input("Enter your list of integers: ").split()))
print(min_diff(arr))