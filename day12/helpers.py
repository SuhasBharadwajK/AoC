start_cave = "start"
end_cave = "end"

def construct_graph(cave_paths):
    graph = {}
    for path in cave_paths:
        a = path[0]
        b = path[1]

        if a in graph:
            graph[a].append(b)

        else:
            graph[a] = [b]

        if b in graph:
            graph[b].append(a)

        else:
            graph[b] = [a]

    return graph
