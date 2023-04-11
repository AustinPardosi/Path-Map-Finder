import math
import networkx as nx

def distance(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2
    return math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)

def parse_into_adjacency_mtr(filename):
    # Parse nodes and coordinates
    nodes = {}
    with open(filename) as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        listnodes = []
        for line in lines[1:n+1]:
            label, lat, lon = line.strip().split()
            nodes[label] = (float(lat), float(lon))
            listnodes.append(label)


        m = n + 1

        matrix = lines[m:]
        mtr = [[int(x) for x in line.split()] for line in matrix]

        for i in range(n) :
            for j in range(n) :
                if mtr[i][j] == 1 :
                    p1 = nodes[listnodes[j]]
                    p2 = nodes[listnodes[i]]
                    mtr[i][j] = distance(p1, p2)

        # print(mtr)

    return mtr, nodes, listnodes

def parse_adjacency_matrix(adj_matrix, listnodes):
    graph = nx.Graph()
    count_nodes = len(adj_matrix)

    # Add nodes to graph
    for i in range(count_nodes):
        node = listnodes[i]
        graph.add_node(node)

    # Add edges to graph
    for i in range(count_nodes):
        for j in range(count_nodes):
            if adj_matrix[i][j] != 0:
                node1 = listnodes[i]
                node2 = listnodes[j]
                weight = adj_matrix[i][j]
                graph.add_edge(node1, node2, weight=weight)

    return graph

def print_graph(graph):
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        if len(neighbors) > 0:
            print("{} -> ".format(node), end="")
            for neighbor in neighbors[:-1]:
                weight = graph.get_edge_data(node, neighbor)['weight']
                print("{} ({})".format(neighbor, weight), end=", ")
            last_neighbor = neighbors[-1]
            weight = graph.get_edge_data(node, last_neighbor)['weight']
            print("{} ({})".format(last_neighbor, weight))
        else:
            print(node)

# mtr, nodes, listnodes = parse_into_adjacency_mtr('src/tes.txt')
# graph = parse_adjacency_matrix(mtr, listnodes)

# print_graph(graph)

# adj_matrix = [
#     [0, 2, 5, 0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 4, 0, 0, 0],
#     [5, 0, 0, 0, 0, 3, 0, 0],
#     [0, 1, 0, 0, 0, 0, 2, 0],
#     [0, 4, 0, 0, 0, 0, 0, 3],
#     [0, 0, 3, 0, 0, 0, 0, 2],
#     [0, 0, 0, 2, 0, 0, 0, 4],
#     [0, 0, 0, 0, 3, 2, 4, 0],
# ]

# graph = parse_adjacency_matrix(adj_matrix)

# print(graph)
