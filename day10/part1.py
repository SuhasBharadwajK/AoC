import day10.helpers as helpers

def program(sytnax_lines):
    illegal_chars_found = []
    for line in sytnax_lines:
        syntax_stack = []
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
                    illegal_chars_found.append(char)
                    break

    score = 0

    for illegal_char in illegal_chars_found:
        score += helpers.illegal_scorecard[illegal_char]
    
    return score