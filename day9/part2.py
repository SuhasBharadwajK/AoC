import day9.helpers as helpers
from functools import reduce

def program(floor_map):
    low_points, low_point_positions = helpers.get_low_points(floor_map)
    all_basins = []

    limit_x = len(floor_map)
    limit_y = len(floor_map[0])

    for i in range(len(low_points)):
        pos = low_point_positions[i]
        pos_x = pos[0]
        pos_y = pos[1]
        basin = []
        trace_basin(floor_map, pos_x, pos_y, basin, limit_x, limit_y)
        all_basins.append(basin)
    
    top_lengths = []
    top_lengths_required = 3

    for basin in all_basins:
        basin_length = len(basin)
        min_length = min(top_lengths) if len(top_lengths) > 0 else 0

        if basin_length > min_length:
            top_lengths.append(basin_length)

            if len(top_lengths) > top_lengths_required:
                top_lengths.sort()
                top_lengths = top_lengths[1:]
            
    result = reduce(lambda x, y: x * y, top_lengths)

    return result

def trace_basin(floor_map, pos_x: int, pos_y: int, basin: list[int], limit_x: int, limit_y: int, scanned_positions: list = []):
    
    if pos_x < 0 or pos_y < 0 or pos_x >= limit_x or pos_y >= limit_y:
        return

    if [pos_x, pos_y] in scanned_positions:
        return

    point_value = floor_map[pos_x][pos_y]

    if point_value < 9:
        basin.append(point_value)
        scanned_positions.append([pos_x, pos_y])
        
        trace_basin(floor_map, pos_x - 1, pos_y, basin, limit_x, limit_y) # Trace up
        trace_basin(floor_map, pos_x + 1, pos_y, basin, limit_x, limit_y) # Trace down
        trace_basin(floor_map, pos_x, pos_y - 1, basin, limit_x, limit_y) # Trace right
        trace_basin(floor_map, pos_x, pos_y + 1, basin, limit_x, limit_y) # Trace left