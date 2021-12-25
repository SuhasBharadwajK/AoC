import day13.helpers as helpers

def program(input_lines):
    dot_pattern, fold_instructions = helpers.parse_input(input_lines)
    resltant_pattern = helpers.fold_paper(dot_pattern, fold_instructions, 1)
    return len(resltant_pattern)