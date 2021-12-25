from typing import ByteString

def parse_input(lines):
    separation_line = 0
    for line in lines:
        if line == '':
            break

        separation_line += 1

    dot_pattern = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), lines[:separation_line]))
    fold_instructions = list(map(lambda x: list(map(lambda y: y.split('='), x.split(' ')[-1:]))[0], lines[separation_line + 1:]))
    return dot_pattern, fold_instructions