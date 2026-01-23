P = int(input())
N = int(input())
M = int(input())

pos = P
for _ in range(M):
    cmd = input().split()
    if cmd[0] == "T":
        direction *= -1
    else:
        steps = int(cmd[1])
        for _ in range(steps):
            next_pos = pos + direction
            if next_pos < 0 or next_pos > N:
                break
            pos = next_pos

print(pos)
    