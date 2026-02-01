from collections import deque
def message(cables, N, start, K):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in cables:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = {start}
    q = deque([start])
    distance = {start: 0}

    while q:
        curr = q.popleft()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[curr] + 1
                q.append(neighbor)
    
    count = sum(1 for x in distance.values() if x <= K)
    return count
    