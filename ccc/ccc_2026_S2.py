N = int(input())
L = int(input())
Q = int(input())

diff = [0] * (N + 3)

for _ in range(L):
    a, b = map(int, input().split())
    l = max(1, a - b)
    r = min(N, a + b)
    diff[l] += 1
    diff[r+1] -= 1

ill = [0] * (N + 1)
curr = 0
for i in range(1, N + 1):
    curr += diff[i]
    ill[i] = curr

result = []
for _ in range(Q):
    x = int(input())
    if ill[x] > 0:
        result.append("Y") 
    else:
        result.append("N")

for i in result:
    print(i)