import heapq # min-heap
def dijkstra(N, edges, start):
    graph = [i: [] for i in range(1, N + 1)]
    for a, b, w in edges:
        graph[a].append((b, w))
        graph[b].append((a, w))

    INF = 10**18
    distance = [INF] * (N)
    distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current = heapq.heappop(priority_queue)

        if current_dist > distance[current]:
            continue

        for neighbor, weight in graph[current]:
            new_dist = current_dist + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor)) # sorts by first item in tuple

    return distance