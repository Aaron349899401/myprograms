from collections import deque
def webpage(N, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
    
    visited = {1}
    q = deque([1])
    while q:
        curr = q.popleft()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    
    return "YES" if len(visited) != N else "NO"