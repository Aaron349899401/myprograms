import heapq
def dijkstra(N, edges, start):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b, w in edges:
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    dist = {i: float("inf") for i in range(1, N + 1)}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if curr_dist > dist[node]:
            continue
        
        for weight, neighbor in graph[node]:
            new_dist = curr_dist + weight
            
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist