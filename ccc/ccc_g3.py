from collections import deque

N = int(input("Enter: "))
M = int(input("Enter your number of doors: "))
doors = [tuple(map(int, input("Enter your doorways: ").split())) for _ in range(M)]

graph = {i: [] for i in range(1, N + 1)}
for a, b in doors:
    graph[a].append(b)
    #graph[b].append(a) (don't do this because the doors are one way not two!)

def bfs(N, graph):
    queue = deque([1])
    visited = {1}
    #distance = {1: 0} (don't need this either because the problem is boolean; yes or no, not shortest path)
    while queue:
        curr = queue.popleft()

        if curr == N:
            return "YES"
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return "NO"

print(bfs(N, graph))