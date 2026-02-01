from collections import deque
def safe_zones(N, edges, zones):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    if zones[0] == 0:
        return "NO"

    visited = {1}
    q = deque([1])
    while q:
        curr = q.popleft()
        for neighbor in graph[curr]:
            if zones[neighbor - 1] == 1 and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    
    return "YES" if N in visited else "NO"