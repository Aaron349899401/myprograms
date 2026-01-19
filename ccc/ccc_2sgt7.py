def coverage(intervals):
    intervals.sort(key=lambda x: x[0])
    max_leng = float("-inf")
    for i in range(len(intervals)):
        for j in range(i, len(intervals)):
            if intervals[i][1] < intervals[j][0]:
                x = intervals[j][1] - intervals[j][0]
                y = intervals[i][1] - intervals[i][0]
                if x + y > max_leng:
                    max_leng = x + y
    return max_leng

#Copilot Solution:
def max_coverage(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end
    total = 0
    last_end = -10**18

    for l, r in intervals:
        if l >= last_end:
            total += r - l
            last_end = r
    return total

# Best Solution From Copilot:
import bisect

def max_coverage(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    starts = [l for l, r in intervals]
    ends = [r for l, r in intervals]

    n = len(intervals)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        l, r = intervals[i-1]
        length = r - l

        # Find the last interval that ends <= l
        j = bisect.bisect_right(ends, l) - 1

        # Option 1: skip interval i
        # Option 2: take interval i + best before it
        dp[i] = max(dp[i-1], length + dp[j+1])

    return dp[n]

N = int(input("Enter your number of intervals: "))
intervals = []
for _ in range(N):
    s, e = map(int, input("Enter your interval: ").split())
    intervals.append((s, e))

print(coverage(intervals))