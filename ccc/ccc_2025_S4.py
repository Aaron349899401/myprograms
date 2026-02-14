import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
maxT = 0

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    graph[v].append((u, t))
    maxT = max(maxT, t)

# Dijkstra on (room, chilling_level)
INF = 10**18
dist = [[INF] * (maxT + 1) for _ in range(N + 1)]

# Start at room 1, chilling level 0
dist[1][0] = 0
pq = [(0, 1, 0)]  # (cost, room, chill)

while pq:
    cost, room, chill = heapq.heappop(pq)
    if cost != dist[room][chill]:
        continue

    # If we reached room N, we can stop early
    if room == N:
        print(cost)
        break

    # 1. Adjust chilling level
    if chill + 1 <= maxT:
        nc = chill + 1
        if dist[room][nc] > cost + 1:
            dist[room][nc] = cost + 1
            heapq.heappush(pq, (cost + 1, room, nc))

    if chill - 1 >= 0:
        nc = chill - 1
        if dist[room][nc] > cost + 1:
            dist[room][nc] = cost + 1
            heapq.heappush(pq, (cost + 1, room, nc))

    # 2. Move through tunnels (free)
    for nxt, temp in graph[room]:
        if temp == chill:  # can only cross if chilling level matches
            if dist[nxt][chill] > cost:
                dist[nxt][chill] = cost
                heapq.heappush(pq, (cost, nxt, chill))