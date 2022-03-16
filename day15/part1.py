import day15.helpers as helpers

def program(input_data):
    grid = input_data
    memo = get_memo(grid)
    cost = trace_path(grid, 0, 0, memo) - grid[0][0]
    print(memo)
    return cost

def trace_path(grid, x, y, memo):
    if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
        return 99999999999999

    if memo[x][y] > 0:
        return memo[x][y]
    
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        memo[x][y] = grid[x][y]
        return grid[x][y]

    right = trace_path(grid, x, y + 1, memo)
    down  = trace_path(grid, x + 1, y, memo)
    cost = min(right, down)
    if x > 0 or y > 0:
        cost += grid[x][y]
    memo[x][y] = cost
    
    return cost

def get_memo(grid):
    memo = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            row.append(0)

        memo.append(row)
    
    return memo

