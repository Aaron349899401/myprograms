def first(dmojistan, pegland, N):
    dmojistan.sort()
    pegland.sort()
    total = 0
    for i in range(N):
        total += min(dmojistan[i], pegland[i])
    return total

def second(dmojistan, pegland, N):
    dmojistan.sort(reverse=True)
    pegland.sort()
    total = 0
    for i in range(N):
        total += max(dmojistan[i], pegland[i])
    return total
# CORRECT!
task = int(input())
N = int(input())
dmojistan = list(map(int, input().split()))
pegland = list(map(int, input().split()))

if task == 1:
    print(first(dmojistan, pegland, N))
else:
    print(second(dmojistan, pegland, N))
    