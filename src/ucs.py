import heapq

def ucs(start, goal, graph):
    # Initialize the frontier queue with the start node and its priority
    frontier = [(0, start)]
    # Initialize the explored set to an empty set
    explored = set()
    # Initialize the cost of the start node to 0
    node_cost = {start: 0}
    # Initialize the parent of the start node to None
    parent = {start: None}

    # Keep searching until the frontier queue is empty
    while frontier:
        # Get the node with the lowest cost from the frontier queue
        cost, current = heapq.heappop(frontier)

        # Check if the current node is the goal node
        if current == goal:
            path = []
            # Reconstruct the path from the start node to the goal node using the parent dictionary
            while current:
                path.append(current)
                current = parent[current]
            return list(reversed(path)), node_cost[goal]

        # Add the current node to the explored set
        explored.add(current)

        # Explore the neighbors of the current node
        for neighbor, neighbor_cost in graph[current].items():
            # Calculate the total cost of reaching the neighbor from the start node
            total_cost = node_cost[current] + neighbor_cost

            # Check if the neighbor is already explored or in the frontier queue with a lower cost
            if neighbor in explored:
                continue
            if (total_cost, neighbor) in frontier:
                continue

            # If the neighbor is not already explored or in the frontier queue with a lower cost,
            # update its cost and parent in the node_cost and parent dictionaries, and add it to the frontier queue
            node_cost[neighbor] = total_cost
            parent[neighbor] = current
            heapq.heappush(frontier, (total_cost, neighbor))

    # If the goal node is not found and the frontier queue is empty, return None
    return None

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 3},
    'D': {'G': 2},
    'E': {'H': 3},
    'F': {'H': 2},
    'G': {'H': 4},
    'H': {}
}

path, cost = ucs('A', 'H', graph)
print(path)
print(cost)
