import heapq

def ucs(start, goal, graph):
    frontier = [(0, start)]  # (cost, node)
    explored = set()
    parent = {start: None}
    cost = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]

        explored.add(current_node)

        for neighbor, neighbor_cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = cost[current_node] + neighbor_cost
                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    parent[neighbor] = current_node
                    heapq.heappush(frontier, (new_cost, neighbor))

    return None, float('inf')

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 3},
    'D': {'G': 2, 'J': 1},
    'E': {'H': 3},
    'F': {'H': 2},
    'G': {'H': 4},
    'H': {'J': 1},
    'J': {}
}

path, cost = ucs('A', 'H', graph)
print(path)
print(cost)
