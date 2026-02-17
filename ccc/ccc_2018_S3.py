from collections import deque # Fail
def caution(cameras, grid, directions):
    result = []
    for r, c in cameras:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] not in {"L", "R", "U", "D"}:
                result.append((nr, nc)) 
    return result

def main(not_safe, grid, target, directions, moves):
    visited = set()
    q = deque([start])
    steps = 0
    tr, tc = target
    while q:
        r, c = q.popleft()
        if (r, c) == (tr, tc):
            return steps
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if grid[nr][nc] == "W" or (nr, nc) in visited or (nr, nc) in not_safe:
                continue

            elif grid[nr][nc] in {"L", "R", "U", "D"}:
                mr, mc = moves[grid[nr][nc]]
                nr, nc += mr, mc
            
            q.append((nr, nc))
            visited.add((nr, nc))
            steps += 1
    return -1

N, M = int(input().split())

moves = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = [0] * N
targets = deque([])
cameras = []
for n in range(N):
    grid[n] = list(input().split())

    for i in range(M):
        if grid[n][i] == "S":
            start = n, i
        if grid[n][i] == "C":
            cameras.append((n, i))
        if grid[n][i] == ".":
            targets.append((n, i))
        
not_safe = caution(cameras, grid, directions)

for target in targets:
    print(main(not_safe, grid, target, directions, moves))