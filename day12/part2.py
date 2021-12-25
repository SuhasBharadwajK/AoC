import day12.helpers as helpers
import copy

def program(cave_paths):
    graph = helpers.construct_graph(cave_paths)
    path_count = trace_paths_with_small_caves(graph, helpers.start_cave)
    return path_count

def trace_paths_with_small_caves(graph: dict[str, list[str]], source_cave: str, path: list[str] = [], counter = 0, limiter = 0):
    current_cave_occurrances = len([x for x in path if x == source_cave])
    if source_cave.islower() and is_any_small_cave_visited_twice(path) and (current_cave_occurrances == 2 or current_cave_occurrances == 1):
        return counter

    path.append(source_cave)

    if source_cave == helpers.end_cave:
        return counter + 1

    links = graph[source_cave]
    for link in links:
        if link != helpers.start_cave:
            counter = trace_paths_with_small_caves(graph, link, copy.deepcopy(path), counter, limiter + 1)

    return counter

def get_path_dictionary(path) -> dict[str:int]:
    path_dict = {}
    for item in path:
        if item in path_dict:
            path_dict[item] += 1
        else:
            path_dict[item] = 1

    return path_dict

def is_any_small_cave_visited_twice(path: list[str]) -> bool:
    path_dict = get_path_dictionary(path)
    for k, v in path_dict.items():
        if v == 2 and k.islower():
            return True

    return False