R, C = map(int, input().split())

grid = []
for _ in range(R):
    row = list(input().strip())
    grid.append(row)

directives = input().strip()

# find starting position
for r in range(R):
    for c in range(C):
        if grid[r][c] == "R":
            sr, sc = r, c

moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

visited = set()
visited.add((sr, sc))

r, c = sr, sc

for d in directives:
    dr, dc = moves[d]
    nr, nc = r + dr, c + dc

    # check bounds and walls
    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
        r, c = nr, nc

    # check revisit
    if (r, c) in visited:
        break
    visited.add((r, c))

print(r, c)