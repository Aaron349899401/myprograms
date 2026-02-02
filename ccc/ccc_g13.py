def tree(N, edges, target):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
    
    visited = set()
    edges = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr == target:
                continue
            if curr not in visited:
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
    
    for node in range(1, N + 1):
        if node not in visited:
            edges += 1
            dfs(node)
    
    return edges