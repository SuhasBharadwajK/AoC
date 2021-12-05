def format(lines: list):
    numbers_called = list(map(lambda x: int(x), lines[0].split(',')))
    lines = lines[2:]
    lines.append('')
    boards = []
    board_indexes = []
    size = 5
    for i in range(0, int(len(lines) / (size + 1))):
        start = i * (size + 1)
        end = start + size
        selected_lines = lines[start : end]
        board_index = {}
        board = []
        for j in range(0, len(selected_lines)):
            line = selected_lines[j]
            numbers = list(map(lambda x: int(x), filter(lambda z: z != '', line.split(' '))))

            for k in range(0, len(numbers)):
                number = numbers[k]
                board_index[number] = { 'row': j, 'column': k, 'is_found': False }

            board.append(numbers)

        board_index['has_won'] = False

        boards.append(board)
        board_indexes.append(board_index)

    return numbers_called, boards, board_indexes