graph = {
    "A": ["B": 5, "C": 1],
    "B": ["A": 5, "C": 2, "D": 1],
    "C": ["A": 1, "B": 2, "D": 4, "E": 8],
    "D": ["B": 1, "C": 4, "E": 3, "F": 6],
    "E": ["C": 8, "D": 3],
    "F": ["D": 6]
}


def dijkstar(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


if __name__ == "__main__":
    parent = dijkstar(graph, "E")
    for key in parent:
        print(key, parent[key])

    v = "B"
    while v is not None:
        print(v)
        v = parent[v]
