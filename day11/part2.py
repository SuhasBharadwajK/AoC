import day11.helpers as helpers

def program(dumbo_grid: list[list[int]]):
    current_step = 0
    are_all_zeroes = False

    while (not are_all_zeroes):
        about_to_blow = helpers.step_one(dumbo_grid)
        helpers.step_two(dumbo_grid, about_to_blow)
        helpers.step_three(dumbo_grid)
        are_all_zeroes = is_zero_grid(dumbo_grid)
        current_step += 1
    
    return current_step

def is_zero_grid(dumbo_grid: list[list[int]]) -> bool:
    total_dumbos = len(dumbo_grid) * len(dumbo_grid[0])
    zero_dumbos = 0
    for i in range(len(dumbo_grid)):
        for j in range(len(dumbo_grid[i])):
            if dumbo_grid[i][j] == 0:
                zero_dumbos += 1
    
    return zero_dumbos == total_dumbos