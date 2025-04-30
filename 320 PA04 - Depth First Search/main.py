
# GraphEL, VertexEL

from edgegraph import GraphEL, VertexEL, EdgeEL


def dfs(graph, start):
    if graph is None:
        return ()
    if start is None:
        return ()
    if start.name not in graph._vertices:
        return ()

    # all visited false
    visited = {vertex.name: False for vertex in graph.vertices()}
    result = []

    dfs_rec(graph, visited, graph._vertices[start.name], result)
    return tuple(result)


def dfs_rec(graph, visited, vertex, result):
    visited[vertex.name] = True
    result.append(vertex)

    for neighbor in graph.adjacent_vertices(vertex):
        if not visited[neighbor.name]:
            dfs_rec(graph, visited, neighbor, result)
