N = int(input("Enter your number of signals: "))
signals = list(map(int, input("Enter your signals: ").split()))
Q = int(input("Enter your number of queries: "))

pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + signals[i - 1]

result = []

for _ in range(Q):
    l, r, x = map(int, input("Enter your querie")).split()
    queries.append((l, r, x))
    if pref[r] - pref[l - 1] > x:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)