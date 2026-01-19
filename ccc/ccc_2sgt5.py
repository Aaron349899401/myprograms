def priorities(pv):
    return sorted(pv, key=lambda x: (x[0], -x[1]))
# by making x[1] negative, we can sort pv by smallest p and largest v

N = int(input("Enter your number of pairs: "))
pv = []
for _ in range(N):
    p, v = map(int, input("Enter your pair: ").split())
    pv.append((p, v))

result = priorities(pv)
for p, v in result:
    print(f"{p} {v}")