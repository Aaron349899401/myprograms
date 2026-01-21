M = int(input("Enter your canvas width: "))
N = int(input("Enter your canvas height: "))
K = int(input("Enter your number of choices: "))

count = 0
for _ in range(K):
    rc, n = input("Enter your choice: ").split()
    if rc == "R":
        seen.add({**dict.fromkeys(range(n, M), "R")})
        count += len(seen)
    elif rc == "C":
        seen.add({**dict.fromkeys(range(n, N), "C")})
        count += len(seen)

seen = set()