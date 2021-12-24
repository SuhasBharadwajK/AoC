import day10.helpers as helpers

def program(sytnax_lines):
    incomplete_lines = []

    for line in sytnax_lines:
        syntax_stack = []
        is_line_illegal = False
        
        for char in line:
            if len(syntax_stack) == 0:
                syntax_stack.append(char)
            
            else:
                previous_char = syntax_stack[-1:][0]
                if char in helpers.legal_pairs:
                    syntax_stack.append(char)

                elif helpers.legal_pairs[previous_char] == char:
                    syntax_stack = syntax_stack[:-1]

                else:
                    is_line_illegal = True
                    break

        if not is_line_illegal:
            syntax_stack.reverse()
            incomplete_lines.append(syntax_stack)

    autocomplete_scores = []

    for line in incomplete_lines:
        score = 0
        for char in line:
            score = ((score * 5) + helpers.autocomplete_scorecard[char])

        autocomplete_scores.append(score)

    autocomplete_scores.sort()
    middle_score_index = int(len(autocomplete_scores) / 2)
    return autocomplete_scores[middle_score_index]