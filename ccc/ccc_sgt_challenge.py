def minimize_max_diff(arr, K):
    arr.sort()
    diffs = []

    for i in range(1, len(arr)):
        diffs.append(arr[i] - arr[i-1])

    diffs.sort(reverse=True)

    # Remove the K-1 largest gaps
    for _ in range(K - 1):
        diffs.pop(0)

    # The remaining largest gap determines the answer
    return sum(diffs)


N = int(input())
arr = list(map(int, input().split()))
K = int(input())

print(minimize_max_diff(arr, K))
