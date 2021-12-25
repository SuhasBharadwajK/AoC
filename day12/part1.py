import day12.helpers as helpers

def program(cave_paths):
    path_count = 0
    graph = helpers.construct_graph(cave_paths)
    path_count = helpers.trace_paths(graph, helpers.start_cave)
    return path_count
