import day11.helpers as helpers

def program(dumbo_grid: list[list[int]]):
    days = 100
    glow_count = 0
    for day in range(1, days + 1):
        about_to_blow = helpers.step_one(dumbo_grid)
        helpers.step_two(dumbo_grid, about_to_blow)
        glow_count += helpers.step_three(dumbo_grid)

    return glow_count
