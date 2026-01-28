from collections import deque
# make directions, make new pos, and check if new pos fits conditions, then pos = new pos
H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]
T = int(input())

# queue holds (row, col, time)
q = deque()

# initialize queue with all starting water cells
for r in range(H):
    for c in range(W):
        if grid[r][c] == "W":
            q.append((r, c, 0))

# BFS spread
directions = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    r, c, t = q.popleft() # deque popleft can be used as an unpacker

    if t == T:
        continue  # stop spreading after T minutes

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        # check bounds and empty land
        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == ".":
            grid[nr][nc] = "W"       # becomes water
            q.append((nr, nc, t + 1))

# count water cells
count = sum(row.count("W") for row in grid)
print(count)