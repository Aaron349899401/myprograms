import math
N = int(input("Enter: ")).strip()
K = int(input("Enter: ")).strip()
if math.gcd(N, K) == 1:
    print("YES")
else:
    print("NO")