from collections import deque
N = int(input("Enter: "))
M = int(input())
connections = [tuple(map(int, input("Enter: ").split())) for _ in range(M)]

if len(connections) != (N - 1):
graphs = {i: [] for i in range(1, N + 1)}
prev = 0
for a, b in paths:
    if 
    graphs[a].append(b)
    graphs[b].append(a)

queue = deque([1])
visited = {1}

while queue:
    curr = queue.popleft()
    for neighbor in graph[curr]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

if len(visited) == N:
    print("YES")
else:
    print("NO")