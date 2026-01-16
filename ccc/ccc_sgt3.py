def max_non_overlapping(tasks):
    # Sort by end time
    tasks.sort(key=lambda x: x[1])

    count = 0
    current_end = -float('inf') #just ensures start is >= current_end, since -inf is smallest value

    for start, end in tasks:
        if start >= current_end:
            count += 1
            current_end = end

    return count

N = int(input())
tasks = []
for _ in range(N):
    s, e = map(int, input().split())
    tasks.append((s, e))

print(max_non_overlapping(tasks))