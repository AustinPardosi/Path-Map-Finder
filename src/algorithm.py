from heapq import heappop, heappush
import math

class UCS :
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
            cost, current = heappop(frontier)

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
                heappush(frontier, (total_cost, neighbor))

        # If the goal node is not found and the frontier queue is empty, return None
        return None

class aStar :
    def euclidean_distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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
