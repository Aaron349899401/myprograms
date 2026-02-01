from collections import deque

# Read input
N = int(input())
M = int(input())

# Build adjacency list
graph = {i: [] for i in range(N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

S, T = map(int, input().split())

# BFS to find shortest path
def bfs(start, target):
    if start == target:
        return 0
    
    queue = deque([start])
    visited = {start}
    distance = {start: 0}
    
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[curr] + 1
                queue.append(neighbor)
                
                if neighbor == target:
                    return distance[neighbor]
    
    return -1

print(bfs(S, T))