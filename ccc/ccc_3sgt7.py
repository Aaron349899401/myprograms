def combine_overlap(intervals):
    intervals.sort(key=lambda x: x[0])
    # sort by start, when you want to merge or detect overlaps
    # and sort by end, when you want to avoid overlaps; for interval questions
    start, end = intervals[0]
    result = []
    for s, e in intervals[1:]:
        if s <= end:
            end = max(e, end)
        else:
            result.append((start, end))
            start, end = s, e
    result.append((start, end)) #you need to append the last interval manually
    return result

N = int(input("Enter your number of intervals: "))
intervals = []
for _ in range(N):
    s, e = map(int, input("Enter your interval: ").split())
    intervals.append((s, e))

result = combine_overlap(intervals)
for s, e in result:
    print(f"{s} {e}")