def BFS(graph, start):
    color = {u: "WHITE" for u in graph}
    distance = {u: float("inf") for u in graph}
    parent = {u: None for u in graph}
    
    color[start] = "GRAY"
    distance[start] = 0
    parent[start] = None
    
    Q = []
    Q.append(start)
    
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

dict1 = {"C":["F"], "E":["F"], "B":["D"], "A":["B","C"], "F":[], "D":[]}

dist, parent = BFS(dict1,"A")
print("Distance:", dist)
print("Parent:", parent)
