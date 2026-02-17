from collections import deque
def pathfind(roads, N, pho):
    graph = {i: [] for i in range(N)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(pho_node, graph, pho):
        visited = set()
        distance = {}
        q = deque([pho_node])
        count = 0
        while q:
            curr = q.popleft()
            if count == len(pho):
                return distance[curr]
            for neighbor in graph[curr]:
                if neigbor not in visited:
                    visited.add(neigbor)
                    distance[neighbor] = distance.get(curr, 0) + 1
                    q.append(neighbor)
                if neighbor in pho:
                    count += 1
        return 10**18
    dists = {}
    for p in pho:
        dists[p] = bfs(p, graph, pho)
    
    return min(dists.values())
N, M = int(input().split())
pho = int(input().split())
roads = []
for _ in range(N):
    a, b = map(int, input().split())
    roads.append((a, b))

# Copilot
from collections import deque

N, M = map(int, input().split())
pho = list(map(int, input().split()))
is_pho = [False] * N
for p in pho:
    is_pho[p] = True

# Build graph
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Step 1: prune tree (remove branches not leading to pho)
degree = [len(graph[i]) for i in range(N)]
q = deque()

for i in range(N):
    if degree[i] == 1 and not is_pho[i]:
        q.append(i)

removed = [False] * N

while q:
    node = q.popleft()
    removed[node] = True
    for nei in graph[node]:
        degree[nei] -= 1
        if degree[nei] == 1 and not is_pho[nei]:
            q.append(nei)

# Step 2: BFS to find one endpoint of diameter
def bfs(start):
    visited = [-1] * N
    visited[start] = 0
    q = deque([start])
    far = start

    while q:
        u = q.popleft()
        far = u
        for v in graph[u]:
            if visited[v] == -1 and not removed[v]:
                visited[v] = visited[u] + 1
                q.append(v)
    return far, visited[far]

# find any pho node still in tree
start = pho[0]
while removed[start]:
    start += 1

# Step 3: find diameter
u, _ = bfs(start)
v, diameter = bfs(u)

# Step 4: count edges in pruned tree
edges = sum(1 for i in range(N) if not removed[i]) - 1

# Step 5: answer
print(2 * edges - diameter)