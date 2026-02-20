def painting(roads, N):
    graph = {i: [] for i in range(N)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    stack = []
    states = ["R", "B"]
    def dfs(node):
        curr = stack.pop()

        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    
    for node in range(N):
        if node not in visited:
            dfs(node)
            
        
