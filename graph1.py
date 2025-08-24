def BFS(graph, start):
    # Initialization
    color = {u: "WHITE" for u in graph}
    distance = {u: float("inf") for u in graph}
    parent = {u: None for u in graph}

    # Start node setup
    color[start] = "GRAY"
    distance[start] = 0
    parent[start] = None

    # Queue initialization
    Q =[]
    Q.append(start)

    # BFS loop
    while Q:
        u = Q.pop(0)
        for v in graph[u]:
            if color[v] == "WHITE":
                color[v] = "GRAY"
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.append(v)
        color[u] = "BLACK"

    return distance, parent
dict1={"c":["F"],"E":["F"],"B":["D"],"A":["B","C"],"F":[],"D":[]}
BFS(dict1,"A")

     