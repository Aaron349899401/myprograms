from collections import deque
def influences(N, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
    
    visited = {1}
    q = deque([1])
    distance = {1: 0}
    while q:
        curr = q.popleft()

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[curr] + 1
                q.append(neighbor)
    
    return max(distance.values())