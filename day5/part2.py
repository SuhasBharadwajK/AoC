import day5.helpers as helpers


def program(lines):
    floor = helpers.get_floor(lines)

    for line in lines:
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]

        if x1 == x2:
            y_min = min(y1, y2)
            y_max = max(y1, y2)

            for i in range(y_min, y_max + 1):
                floor[i][x1] += 1

        if y1 == y2:
            x_min = min(x1, x2)
            x_max = max(x1, x2)

            for i in range(x_min, x_max + 1):
                floor[y1][i] += 1

        factor = 0
        if x1 - y1 == x2 - y2:
            factor = 1

        if x1 + y1 == x2 + y2:
            factor = -1
        
        if factor != 0:
            x_min = min(x1, x2)
            x_max = max(x1, x2)
            
            y = y1 if x_min == x1 else y2
            for i in range(x_min, x_max + 1):
                floor[y][i] += 1
                y += factor

    hazard_score = helpers.get_hazard_scrore(floor)
    return hazard_score
