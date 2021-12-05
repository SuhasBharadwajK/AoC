def get_floor(lines):
    max_x = 0
    max_y = 0

    for line in lines:
        if line[0][0] > max_x:
            max_x = line[0][0]
        
        if line[1][0] > max_x:
            max_x = line[1][0]
        
        if line[0][1] > max_y:
            max_y = line[0][1]

        if line[1][1] > max_y:
            max_y = line[1][1]

    floor = [[0] * (max_x + 1) for _ in range((max_y + 1))]
    return floor

def print_floor(floor):
    for i in range(0, len(floor)):
        for j in range(0, len(floor[i])):
            if (floor[i][j] == 0):
                print('.', end = ' ')
            else:
                print(floor[i][j], end=' ')

        print()

def get_hazard_scrore(floor):
    hazard_score = 0
    threshold = 2
    for i in range(0, len(floor)):
        for j in range(0, len(floor[i])):
            if floor[i][j] >= threshold:
                hazard_score += 1

    return hazard_score