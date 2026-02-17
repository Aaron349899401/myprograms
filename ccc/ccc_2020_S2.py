from collections import deque
def factors(M, N, x):
    result = []
    for r in range(1, M + 1):
        if x % r == 0:
            c = x // r 
            if (1 <= c <= N):
                result.append((r, c))
    return result

M = int(input())
N = int(input())
graph = []
for _ in range(M):
    x = list(map(int, input("Enter: ").split()))
    graph.append(x)

q = deque([(1, 1)])
visited = set()
found = False

while q:
    r, c = q.popleft()
    if (r, c) in visited:
        continue
    visited.add((r, c))
    if (r, c) == (M, N):
        found = True
        break
    curr = graph[r-1][c-1]
    for fr, fc in factors(M, N, curr):
        if (fr, fc) not in visited:
            q.append((fr, fc))

print("YES" if found else "NO")

# Copilot Solution
from collections import deque

M = int(input())
N = int(input())

grid = [list(map(int, input().split())) for _ in range(M)]

# BFS starting at (1,1)
q = deque([(1, 1)])
visited = set()

while q:
    r, c = q.popleft()

    if (r, c) in visited:
        continue
    visited.add((r, c))

    # If we reached the bottom-right cell
    if (r, c) == (M, N):
        print("yes")
        break

    value = grid[r-1][c-1]

    # Try all factor pairs of value
    for fr in range(1, int(value**0.5) + 1):
        if value % fr == 0:
            fc = value // fr

            # Check both factor orientations
            if 1 <= fr <= M and 1 <= fc <= N:
                q.append((fr, fc))
            if 1 <= fc <= M and 1 <= fr <= N:
                q.append((fc, fr))

else:
    print("no")