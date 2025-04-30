from edgegraph import *
import math


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL):
    # BC
    if graph is None:
        return None, None
    if start is None:
        return None, None
    if end is None:
        return None, None
    if start.name not in [vertex.name for vertex in graph.vertices()]:
        return None, None
    if end.name not in [vertex.name for vertex in graph.vertices()]:
        return None, None

    # INI
    distances = {vertex.name: float('inf') for vertex in graph.vertices()}
    distances[start.name] = 0
    predecessors = {vertex.name: None for vertex in graph.vertices()}
    used = {vertex.name: None for vertex in graph.vertices()}

    # RLX
    for _ in range(graph.num_vertices() - 1):
        for edge in graph.edges():
            u = edge.tail()
            v = edge.head()
            weight = edge.get_value()
            if distances[u.name] + weight < distances[v.name]:
                distances[v.name] = distances[u.name] + weight
                predecessors[v.name] = u.name
                used[v.name] = edge

    print("Distances after relaxation:", distances)
    print("Predecessors:", predecessors)

    # NWC
    for edge in graph.edges():
        u = edge.tail()
        v = edge.head()
        weight = edge.get_value()
        if distances[u.name] + weight < distances[v.name]:
            return None, None

    # PTH
    path = []
    current = end.name
    while current != start.name and current is not None:
        if used[current] is not None:
            path.append(used[current])
        current = predecessors[current]
    path.reverse()  # S->F

    print("Path found:", path)

    # GTH
    remain = []
    if distances[end.name] < float('inf'):
        remain = [edge for edge in graph.edges() if edge.tail().name ==
                  end.name]

    return tuple(path), tuple(remain)


if __name__ == "__main__":
    graph = GraphEL()
    v1 = VertexEL("A")
    v2 = VertexEL("B")
    v3 = VertexEL("C")
    v4 = VertexEL("D")
    v5 = VertexEL("E")
    v6 = VertexEL("F")

    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_vertex(v3)
    graph.add_vertex(v4)
    graph.add_vertex(v5)
    graph.add_vertex(v6)

    e1 = EdgeEL("edge1", v1, v2)
    e1.set_value(1)
    graph.add_edge(e1)

    e2 = EdgeEL("edge2", v2, v4)
    e2.set_value(2)
    graph.add_edge(e2)

    e3 = EdgeEL("edge3", v6, v1)
    e3.set_value(3)
    graph.add_edge(e3)

    e4 = EdgeEL("edge4", v3, v1)
    e4.set_value(4)
    graph.add_edge(e4)

    e5 = EdgeEL("edge5", v5, v6)
    e5.set_value(2)
    graph.add_edge(e5)

    e6 = EdgeEL("edge6", v5, v3)
    e6.set_value(3)
    graph.add_edge(e6)

    e7 = EdgeEL("edge7", v4, v6)  # D to F
    e7.set_value(2)
    graph.add_edge(e7)

    path_edges, remaining_edges = bellman_ford(graph, v1, v6)

    print("Path edges:", path_edges)
    print("Remaining edges:", remaining_edges)
