N = 18
for i in range(1, N // 2 + 1):
    if N % i == 0 and i % 2 != 0:
        print("YES")

