import sys
input = sys.stdin.readline
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Q = 4

result = []
pref = [0] * (len(nums) + 1)
for i in range(1, len(nums) + 1):
    pref[i] = pref[i - 1] + nums[i - 1]

for _ in range(Q):
    s, e = map(int, input().split()) # FASTER THAN LIST OF TUPLES
    result.append(pref[e] - pref[s - 1])

print(result)

