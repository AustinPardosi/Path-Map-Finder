from heapq import heappop, heappush
import math
import parse_into_graph as parser

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
            for neighbor in graph.neighbors(currentNode):
                # Calculate the total cost of reaching the neighbor from the start node
                total_cost = node_cost[currentNode] + graph[currentNode][neighbor]['weight']

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
                return path[::-1], jarak

            # Check neighbors of currentNode node
            for neighbor in graph.neighbors(currentNode):
                # Calculate g-score of neighbor
                jarak = gn[currentNode] + graph[currentNode][neighbor]['weight']

                # Calculate f-score of neighbor
                h_score = heuristic(neighbor, goal)
                f_score = jarak + h_score

                # If neighbor is not in open set or has lower f-score, update values
                if neighbor not in gn or jarak < gn[neighbor]:
                    gn[neighbor] = jarak
                    parents[neighbor] = currentNode
                    heappush(open_set, (f_score, neighbor))

        # If goal is not reachable, return empty path
        return [], 0

##### MAIN #####

# mtr, nodes, listnodes = parser.parse_into_adjacency_mtr('src/tes.txt')
# graph = parser.parse_adjacency_matrix(mtr)

# A*
# start = 'A'
# goal = 'F'
# heuristic = lambda a, b : aStar.euclidean_distance(nodes['A'], nodes['B'])
# path = aStar.astar(start, goal, graph, heuristic)

# UCS
# start = 'A'
# goal = 'F'
# path = UCS.ucs(start, goal, graph)

# print(path)
