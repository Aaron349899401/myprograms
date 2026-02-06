from collections import deque
import sys
def escape(edges, N):

    graph = {i: [] for i in range(1, N + 1)}
    for a, b in edges:
        graph[a].append(b)
    
    count = 0
    def bfs(node):
        visited = set([node])
        q = deque([node])
        while q:
            curr = q.popleft()
            if curr == N:
                return True
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
            return False
    for node in range(1, N + 1):
        if bfs(node):
            count += 1
    return count
input = sys.stdin.readline
N = int(input("Enter: "))
M = int(input())
edges = [tuple(map(int, input("Enter your edges: ").split())) for _ in range(M)] 
print(escape(edges, N))    