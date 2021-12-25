import day12.helpers as helpers
import copy

def program(cave_paths):
    path_count = 0
    graph = helpers.construct_graph(cave_paths)
    path_count = trace_paths(graph, helpers.start_cave)
    return path_count

def trace_paths(graph: dict[str, list[str]], source_cave: str, path: list[str] = [], counter = 0):
    
    if source_cave.islower() and source_cave in path:
        return counter

    path.append(source_cave)

    if source_cave == helpers.end_cave:
        return counter + 1

    links = graph[source_cave]
    for link in links:
        if link != helpers.start_cave:
            counter = trace_paths(graph, link, copy.deepcopy(path), counter)

    return counter