import day12.helpers as helpers

def program(cave_paths):
    graph = helpers.construct_graph(cave_paths)
    path_count = helpers.trace_paths_with_small_caves(graph, helpers.start_cave)
    return path_count