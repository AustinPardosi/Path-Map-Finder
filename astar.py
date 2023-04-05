from heapq import heappop, heappush
from math import sqrt

def euclidean_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def astar(start, goal, graph, heuristic):
    # Initialize start node and open set
    open_set = [(0, start)]
    # Keep track of parent nodes for each visited node
    parents = {start: None}
    # Cost of getting to start node is zero
    g_scores = {start: 0}

    while open_set:
        # Get the node with the lowest f-score
        current_g, current = heappop(open_set)

        # If current is goal, return the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        # Check neighbors of current node
        for neighbor, cost in graph[current]:
            # Calculate g-score of neighbor
            g_score = g_scores[current] + cost

            # Calculate f-score of neighbor
            h_score = heuristic(neighbor, goal)
            f_score = g_score + h_score

            # If neighbor is not in open set or has lower f-score, update values
            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                parents[neighbor] = current
                heappush(open_set, (f_score, neighbor))

    # If goal is not reachable, return empty path
    return []

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 1), ('F', 9)],
    'D': [('F', 5)],
    'E': [('F', 2)]
}

heuristic = lambda a, b: 0 # Use zero heuristic for simplicity
start = 'A'
goal = 'F'

# --------------------------------------------------------------------------------

graph2 = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],
    (1, 0): [((2, 0), 1), ((1, 1), 1)],
    (2, 0): [((2, 1), 1)],
    (0, 1): [((0, 2), 1)],
    (1, 1): [((2, 1), 1)],
    (0, 2): [((1, 2), 1)],
    (1, 2): [((2, 2), 1)],
    (2, 1): [((2, 2), 1)]
}

heuristic2 = lambda a, b : euclidean_distance(a, b)
start2 = (0, 0)
goal2 = (2, 1)

path = astar(start, goal, graph, heuristic)
path2 = astar(start2, goal2, graph2, heuristic2)
print(path) # Output: ['A', 'C', 'D']
print(path2)
