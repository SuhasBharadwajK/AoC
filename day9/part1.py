import day9.helpers as helpers

def program(floor_map):
    low_points, low_point_positions = helpers.get_low_points(floor_map)
    return sum(low_points) + len(low_points)