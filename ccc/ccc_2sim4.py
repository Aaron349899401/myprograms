H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

sr, sc = map(int, input().split())   # starting row, col (0-indexed)
direction = input().strip()          # U, D, L, R

# Direction vectors
dirs = {
    "U": (1, 0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
# Mirror reflections
# (incoming_direction, mirror) -> new_direction
reflect = {
    ("U", "/"): "R",
    ("U", "\\"): "L",
    ("D", "/"): "L",
    ("D", "\\"): "R",
    ("L", "/"): "D",
    ("L", "\\"): "U",
    ("R", "/"): "U",
    ("R", "\\"): "D"
}

r, c = sr, sc
steps = 0

# Track visited states: (row, col, direction)
visited = set()
visited.add((r, c, direction))

while True:
    dr, dc = dirs[direction]
    nr, nc = r + dr, c + dc

    # Out of bounds → stop
    if not (0 <= nr < H and 0 <= nc < W):
        break

    # Wall → stop
    if grid[nr][nc] == "#":
        break

    # Move
    r, c = nr, nc
    steps += 1

    # Mirror reflection
    if grid[r][c] in ("/", "\\"):
        direction = reflect[(direction, grid[r][c])]

    # Loop detection
    state = (r, c, direction)
    if state in visited:
        break
    visited.add(state)

print(steps)