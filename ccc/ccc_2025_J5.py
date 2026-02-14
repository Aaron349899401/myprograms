import heapq
R, C = int(input("Enter: ").split())
M = int(input("Enter: "))

graph = []
temp = [1, 2, 3, 4, 5]
for num in temp:
    for r in range(R):
        graph[r] = []
        for c in range(C):
            graph[r][c] = num


def dijkstra(graph, M, R):
    INF = 10**18
    dist = [INF] * R 
    dist[0] = 0

    pq = [(0, 0)]

    while pq:
        curr_dist, curr = heapq.heappop(pq) 
        if curr_dist > dist[curr]:
            continue
        
        for weight in graph[curr]:
            new_dist = curr_dist + weight
            if new_dist < dist[weight]:
                we