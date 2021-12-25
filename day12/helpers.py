import copy

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

def trace_paths(graph: dict[str, list[str]], source_cave: str, path: list[str] = [], counter = 0):
    
    if source_cave.islower() and source_cave in path:
        return counter

    path.append(source_cave)

    if source_cave == end_cave:
        return counter + 1

    links = graph[source_cave]
    for link in links:
        if link != start_cave:
            counter = trace_paths(graph, link, copy.deepcopy(path), counter)

    return counter
