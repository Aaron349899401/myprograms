import heapq
def astar(num_nodes, start, goal, graph, heuristic):
    INF = 10**18
    g_cost = [INF] * num_nodes
    g_cost[start] = 0
    parent = [-1] * num_nodes
    # priority queue stores (f_cost, g_cost, node)
    priority_queue = [(heuristic(start), 0, start)]

    while priority_queue:
        f_cost, current_g, current = heapq.heappop(priority_queue)

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_g = current_g + weight

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(priority_queue, (new_f, new_g, neighbor))
    return parent

def heuristic(node):
    x, y = node
    gx, gy = goal
    return abs(x - gx) + abs(y - gy)