def calculate_winning_score(winning_board, winning_index):
    non_winning_sum = 0
    for i in range(0, len(winning_board)):
        current_row = winning_board[i]
        for j in range(0, len(current_row)):
            if not winning_index[winning_board[i][j]]['is_found']:
                non_winning_sum += winning_board[i][j]

    return non_winning_sum * winning_index['winning_number']

def get_winning_order(numbers_to_be_called: list[int], boards: list, board_indexes: dict):
    won_boards = []
    won_indexes: list[dict] = []
    board_size = 5

    for number in numbers_to_be_called:
        for current_board in range(0, len(boards)):

            board = boards[current_board]
            index: dict = board_indexes[current_board]
            index['board_number'] = current_board

            if not index['has_won']:
                if number in index:
                    index[number]['is_found'] = True
                    row = index[number]['row']
                    column = index[number]['column']
                    row_count = 0
                    column_count = 0

                    for i in range(0, board_size):
                        if index[board[row][i]]['is_found']:
                            row_count += 1

                    if row_count == board_size:
                        index['winning_number'] = number
                        index['has_won'] = True
                        won_boards.append(board)
                        won_indexes.append(index)

                    for i in range(0, board_size):
                        if index[board[i][column]]['is_found']:
                            column_count += 1

                    if column_count == board_size:
                        index['winning_number'] = number
                        index['has_won'] = True
                        won_boards.append(board)
                        won_indexes.append(index)

    return won_indexes