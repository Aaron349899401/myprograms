from collections import deque
def rumor(friendships, N):
    graphs = {i: [] for i in range(1, N + 1)}
    for a, b in friendships:
        graphs[a].append(b)
        graphs[b].append(a)

    queue = deque([1])
    visited = {1}
    distance = {1: 0}
    while queue:
        curr = queue.popleft()

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[curr] + 1
                queue.append(neighbor)
    
    return max(distance.values())