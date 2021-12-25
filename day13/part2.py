import day13.helpers as helpers

def program(input_lines):
    dot_pattern, fold_instructions = helpers.parse_input(input_lines)
    resltant_pattern = helpers.fold_paper(dot_pattern, fold_instructions, len(fold_instructions))

    paper = helpers.get_paper(resltant_pattern)
    plotted_paper = helpers.plot_on_paper(paper, resltant_pattern)
    helpers.print_paper(plotted_paper)
    
    return len(resltant_pattern)