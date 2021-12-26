def parse_input(input_lines):
    template = input_lines[0]
    insertion_rules = list(map(lambda x: list(map(lambda y: y.strip(), x.split('->'))), input_lines[2:]))
    return template, insertion_rules