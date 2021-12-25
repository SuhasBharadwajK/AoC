from typing import ByteString

def parse_input(lines: list[str]):
    separation_line = 0
    for line in lines:
        if line == '':
            break

        separation_line += 1

    dot_pattern = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), lines[:separation_line]))
    fold_instructions = list(map(lambda x: list(map(lambda y: (str(y.split('=')[0]), int(y.split('=')[1])), x.split(' ')[-1:]))[0], lines[separation_line + 1:]))
    return dot_pattern, fold_instructions

def fold_paper(dot_pattern: list[list[int]], fold_instructions: list[tuple[str, int]], number_of_folds: int):
    fold_count = 0
    remaining_coordinates = []

    for instruction in fold_instructions:
        fold_count += 1
        if fold_count > number_of_folds:
            break

        transform_index = 1 if instruction[0] == 'y' else 0 # Get if the transformation needs to be done along x or y
        folding_point = instruction[1]

        for coordinate in dot_pattern:
            if coordinate[transform_index] > folding_point:
                coordinate[transform_index] -= 2 * (coordinate[transform_index] - folding_point)

            if coordinate not in remaining_coordinates:
                remaining_coordinates.append(coordinate)

    return remaining_coordinates

def get_paper(dot_pattern: list[list[int]]):
    max_x = max(map(lambda x: x[1], dot_pattern))
    max_y = max(map(lambda x: x[0], dot_pattern))
    paper: list[list[int]] = []
    for i in range(max_x + 1):
        line = []
        for j in range(max_y + 1):
            line.append('.')
        
        paper.append(line)

    return paper

def plot_on_paper(paper: list[list[int]], dot_pattern: list[list[int]]):
    for coordinate in dot_pattern:
        x = coordinate[1]
        y = coordinate[0]

        paper[x][y] = '#'
    
    return paper

def print_paper(paper: list[list[int]]):
    for line in paper:
        for char in line:
            print(char, end='')
        
        print()
