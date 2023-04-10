from heapq import heappop, heappush
import math
import parse_into_graph as parser

class UCS :
    def ucs(start, goal, graph):
        nodesToExplore = [(0, start)]
        visited = []
        cost = {start: 0}
        parents = {start: None}

        while nodesToExplore:
            currentCost, currentNode = heappop(nodesToExplore)
            if currentNode == goal:
                path = []
                while currentNode:
                    path.append(currentNode)
                    currentNode = parents[currentNode]
                return path[::-1], cost[goal]

            visited.append(currentNode)

            for neighbor in graph.neighbors(currentNode):
                total_cost = cost[currentNode] + graph[currentNode][neighbor]['weight']

                if neighbor in visited:
                    continue
                if (total_cost, neighbor) in nodesToExplore:
                    continue

                cost[neighbor] = total_cost
                parents[neighbor] = currentNode
                heappush(nodesToExplore, (total_cost, neighbor))

        return [], 0

class aStar :
    def find_euclidean_distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def astar(start, goal, graph, nodes, heuristic_func):
        exploreNodes = [(0, start)]
        parents = {start: None}
        currentPathWithCost = {start: 0}

        while exploreNodes:
            currentCost, currentNode = heappop(exploreNodes)

            if currentNode == goal:
                shortestPath = []
                gn = currentPathWithCost[currentNode]
                while currentNode:
                    shortestPath.append(currentNode)
                    currentNode = parents[currentNode]
                return shortestPath[::-1], gn

            for neighbor in graph.neighbors(currentNode):
                gn = currentPathWithCost[currentNode] + graph[currentNode][neighbor]['weight']

                if heuristic_func:
                    hn = aStar.find_euclidean_distance(nodes[neighbor], nodes[goal])
                    fn = gn + hn

                if (neighbor not in currentPathWithCost) or (gn < currentPathWithCost[neighbor]):
                    currentPathWithCost[neighbor] = gn
                    parents[neighbor] = currentNode
                    heappush(exploreNodes, (fn, neighbor))

        return [], 0

##### MAIN #####

# mtr, nodes, listnodes = parser.parse_into_adjacency_mtr('src/tes.txt')
# graph = parser.parse_adjacency_matrix(mtr)

# A*
# start = 'D'
# goal = 'G'
# heuristic = True
# path, cost = aStar.astar(start, goal, graph, nodes, heuristic)

# UCS
# start = 'A'
# goal = 'F'
# path, cost = UCS.ucs(start, goal, graph)

# print(path, cost)
