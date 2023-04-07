import math
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
        print(m)

        matrix = lines[9:]
        mtr = [[int(x) for x in line.split()] for line in matrix]

        for i in range(n) :
            for j in range(n) :
                if mtr[i][j] == 1 :
                    p1 = nodes[listnodes[j]]
                    p2 = nodes[listnodes[i]]
                    mtr[i][j] = distance(p1, p2)

        # print(mtr)

    return mtr

def parse_adjacency_matrix(adj_matrix):
    graph = {}
    countNodes = len(adj_matrix)

    for i in range(countNodes):
        node = chr(ord('A') + i)
        edges = {}
        for j in range(countNodes):
            if adj_matrix[i][j] != 0:
                neighbor = chr(ord('A') + j)
                edges[neighbor] = adj_matrix[i][j]
        graph[node] = edges

    return graph

def print_graph(graph):
    for node, edges in graph.items():
        print(f"{node} -> ", end="")
        if not edges:
            print("None")
        else:
            for neighbor, weight in edges.items():
                print(f"{neighbor} ({weight}), ", end="")
            print()

mtr = parse_into_adjacency_mtr('src/tes.txt')
graph = parse_adjacency_matrix(mtr)

print_graph(graph)

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
