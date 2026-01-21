def dijkstra(start, graph):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    