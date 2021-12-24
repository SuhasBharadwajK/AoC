grid_height = 10
grid_width = 10

def print_grid(dumbo_grid: list[list[int]]):
    print('----------------------------------')
    for i in range(len(dumbo_grid)):
        for j in range(len(dumbo_grid[i])):
            print(str(dumbo_grid[i][j]) + " ", end="")

        print()


def step_one(dumbo_grid: list[list[int]]):
    about_to_blow: list[(int, int)] = []
    for i in range(len(dumbo_grid)):
        for j in range(len(dumbo_grid[i])):
            dumbo_grid[i][j] += 1
            if dumbo_grid[i][j] > 9:
                about_to_blow.append((i, j))

    return about_to_blow


def step_two(dumbo_grid: list[list[int]], about_to_blow: list[(int, int)]):
    if len(about_to_blow) == 0:
        return

    for position in about_to_blow:
        i = position[0]
        j = position[1]
        coordinates = get_cartesian_product(i, j)
        for coordinate in coordinates:
            x = coordinate[0]
            y = coordinate[1]

            if dumbo_grid[x][y] == 9:
                about_to_blow.append((x, y))

            dumbo_grid[x][y] += 1

        about_to_blow.remove((i, j))

    step_two(dumbo_grid, about_to_blow)


def step_three(dumbo_grid: list[list[int]]):
    glow_count = 0
    for i in range(len(dumbo_grid)):
        for j in range(len(dumbo_grid[i])):
            if dumbo_grid[i][j] > 9:
                glow_count += 1
                dumbo_grid[i][j] = 0

    return glow_count


def get_cartesian_product(i: int, j: int):
    cartesian_product = []
    x_coordinates = [i, i - 1, i + 1]
    y_coordinates = [j, j - 1, j + 1]

    for x in x_coordinates:
        for y in y_coordinates:
            if x >= 0 and y >= 0 and x < grid_width and y < grid_height:
                cartesian_product.append((x, y))

    return cartesian_product[1:]