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
