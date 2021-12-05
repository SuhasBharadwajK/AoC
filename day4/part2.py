import day4.input_formatter as formatter
import day4.helpers as helpers

def program(input_data):
    numbers_to_be_called, boards, board_indexes = formatter.format(input_data)
    winning_indexes = helpers.get_winning_order(numbers_to_be_called, boards, board_indexes)
    winning_index = winning_indexes[len(winning_indexes) - 1]
    winning_board = boards[winning_index['board_number']]
    score = helpers.calculate_winning_score(winning_board, winning_index)
    return score