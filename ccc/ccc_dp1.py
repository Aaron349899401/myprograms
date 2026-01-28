N = int(input())

if N == 0 or N == 1:
    print(1)
else:
    a, b = 1, 1  # ways(0), ways(1)
    for _ in range(2, N + 1):
        a, b = b, a + b
    print(b)