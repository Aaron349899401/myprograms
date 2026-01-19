def no_overlap(intervals):
    intervals.sort(key=lambda x: x[0])
    count = 0
    last_end = float("-inf")
    for s, e in intervals:
        if s > last_end:
            count += 1
            last_end = e
    return count

N = int(input("Enter your number of intervals: "))
intervals = [tuple(map(int, input().split())) for _ in range(N)]

print(no_overlap(intervals))
        