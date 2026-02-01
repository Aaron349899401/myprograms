def has_cycle(N, edges): # iterative version (non-recursive)
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()

    for start in range(1, N + 1):
        if start in visited:
            continue
        
        stack = [(start, -1)]
        while stack:
            curr, parent = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    stack.append((neighbor, curr))
                elif neighbor != parent:
                    return True
    return False

def has_cycle_recursive(N, edges): # recursive version
    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited and dfs(neighbor, node):
                return True
            elif neighbor != parent: # making sure it only detects cycles that dont come from where you just were
                return True
        return False
    
    for start in range(1, N + 1):
        if start not in visited:
            if dfs(start, -1):
                return True
    return False
