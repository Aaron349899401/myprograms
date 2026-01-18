def overlap_merge(arr):
    arr.sort()
    merged = []
    for start, end in arr:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

N = int(input("Enter your number of intervals: "))
arr = []
for _ in range(N):
    s, e = input("Enter your interval: ").split()
    arr.append((int(s), int(e)))

print(overlap_merge(arr))