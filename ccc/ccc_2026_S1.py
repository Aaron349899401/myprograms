A = int(input())
B = int(input())
K = int(input())
T = int(input())


d = abs(B - A)
var = d // K
# base case
if d == 0:
    if T == 1:
        print(0)
    else:
        print(2)
    exit() # Note: break

consider = set()
for t in range(var - 3, var + 4):
    consider.add(t)
consider.add(0)
hoppity = set()
for t in consider:
    hoppity.add(abs(t) + abs(d - t * K))

hoppity = sorted(hoppity)
best = hoppity[0]

if T == 1:
    print(best)
else:
    if len(hoppity) > 1:
        sec = hoppity[1]
    else:
        sec = 10**30
    print(min(sec, best + 2))