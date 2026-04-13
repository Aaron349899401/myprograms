import heapq

# Define a Node class to store state, parent information, and heuristic value
class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic

    # Comparison method for the priority queue (heapq)
    # Compares nodes based on their heuristic value (f(n) = h(n) in Greedy BFS)
    def __lt__(self, other): # "less than" -> overloading the < operator
        return self.heuristic < other.heuristic

def greedy_best_first_search(graph, start, goal, heuristics):
    # Priority queue to store nodes to be explored, ordered by heuristic value
    priority_queue = [Node(start, heuristic=heuristics[start])]
    heapq.heapify(priority_queue)
    
    # Set to keep track of visited states
    visited = set()
    
    while priority_queue:
        # Get the node with the lowest heuristic value (most promising)
        current_node = heapq.heappop(priority_queue)
        current_state = current_node.state

        # Check if the goal is reached
        if current_state == goal:
            return reconstruct_path(current_node)

        if current_state in visited:
            continue

        visited.add(current_state)

        # Explore neighbors
        for neighbor, cost in graph.get(current_state, []):
            if neighbor not in visited:
                # Calculate the heuristic for the neighbor
                neighbor_heuristic = heuristics[neighbor]
                # Create a new node and push it to the priority queue
                heapq.heappush(priority_queue, Node(neighbor, current_node, neighbor_heuristic))
    
    # If the loop finishes without finding the goal
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1] # Return reversed path from start to goal

# --- Example Usage ---
# Graph definition (adjacency list with edge weights, although weights are ignored by GBFS)
graph_data = {
    'A': [('B', 75), ('C', 118), ('E', 140)],
    'B': [],
    'C': [('E', 19), ('F', 17)], # Example with edge weights
    'E': [('F', 90), ('G', 80)],
    'F': [('I', 211)],
    'G': [('H', 97)],
    'H': [('I', 101)],
    'I': []
}

# Heuristic values (estimated straight-line distance to goal 'I')
heuristics_data = {
    'A': 366, 'B': 374, 'C': 329, 'E': 253,
    'F': 178, 'G': 193, 'H': 98, 'I': 0
}

start_node = 'A'
goal_node = 'I'

path_found = greedy_best_first_search(graph_data, start_node, goal_node, heuristics_data)

if path_found:
    print(f"Path found: {' -> '.join(path_found)}")
else:
    print("No path found.")

