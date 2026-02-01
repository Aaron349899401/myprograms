def connected(N, roads):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    def dfs(city):
        stack = [city]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    
    connections = 0
    for city in range(1, N + 1):
        if city not in visited:
            connections += 1
            dfs(city)
    return connections