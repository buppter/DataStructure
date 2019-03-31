graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def DFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


if __name__ == "__main__":
    DFS(graph,"E")
