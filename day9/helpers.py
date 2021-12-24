def get_low_points(floor_map):
    low_points = []
    for i in range(0, len(floor_map)):
        for j in range(0, len(floor_map[i])):
            index_up = i - 1
            index_down = i + 1 if i < len(floor_map) - 1 else -1
            index_left = j - 1
            index_right = j + 1 if j < len(floor_map[i]) - 1 else -1

            up = floor_map[index_up][j] if index_up > -1 else -1
            down = floor_map[index_down][j] if index_down > -1 else -1
            left = floor_map[i][index_left] if index_left > -1 else -1
            right = floor_map[i][index_right] if index_right > -1 else -1

            current = floor_map[i][j]
            if (up == -1 or up > current) and (down == -1 or down > current) and (left == -1 or left > current) and (right == -1 or right > current):
                low_points.append(current)

    return low_points