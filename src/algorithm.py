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
            currentCost, currentNode = heappop(frontier)

            # Check if the currentNode node is the goal node
            if currentNode == goal:
                path = []
                # Reconstruct the path from the start node to the goal node using the parent dictionary
                while currentNode:
                    path.append(currentNode)
                    currentNode = parent[currentNode]
                return list(reversed(path)), node_cost[goal]

            # Add the currentNode node to the explored set
            explored.add(currentNode)

            # Explore the neighbors of the currentNode node
            for neighbor, neighbor_cost in graph[currentNode].items():
                # Calculate the total cost of reaching the neighbor from the start node
                total_cost = node_cost[currentNode] + neighbor_cost

                # Check if the neighbor is already explored or in the frontier queue with a lower cost
                if neighbor in explored:
                    continue
                if (total_cost, neighbor) in frontier:
                    continue

                # If the neighbor is not already explored or in the frontier queue with a lower cost,
                # update its cost and parent in the node_cost and parent dictionaries, and add it to the frontier queue
                node_cost[neighbor] = total_cost
                parent[neighbor] = currentNode
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
        gn = {start: 0}

        while open_set:
            # Get the node with the lowest f-score
            currentCost, currentNode = heappop(open_set)

            # If currentNode is goal, return the path
            if currentNode == goal:
                path = []
                while currentNode:
                    path.append(currentNode)
                    currentNode = parents[currentNode]
                return path[::-1], gn

            # Check neighbors of currentNode node
            for neighbor, cost in graph[currentNode]:
                # Calculate g-score of neighbor
                gn = gn[currentNode] + cost

                # Calculate f-score of neighbor
                hn = heuristic(neighbor, goal)
                fn = gn + hn

                # If neighbor is not in open set or has lower f-score, update values
                if neighbor not in gn or gn < gn[neighbor]:
                    gn[neighbor] = gn
                    parents[neighbor] = currentNode
                    heappush(open_set, (fn, neighbor))

        # If goal is not reachable, return empty path
        return []
