H = int(input())
W = int(input())
Q = int(input())

row = [0] * (H + 1)
col = [0] * (W + 1)

for _ in range(Q):
    t, x = input().split()
    x = int(x)
    if t == 'R':
        row[x] ^= 1  # toggle parity
    else:  # 'C'
        col[x] ^= 1

R = sum(row)
C = sum(col)

gold = R * (W - C) + (H - R) * C  # determines the depth/number of Gs per row/column
print(gold)


