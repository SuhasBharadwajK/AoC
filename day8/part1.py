import day8.helpers as helpers

def program(input_lines):
    segment_map_lengths = helpers.get_segment_map_lenghts()
    easy_numbers = 0
    for line in input_lines:
        pattern = line[0]
        digits = list(map(lambda y: y.strip(), line[1].split(' ')))
        for digit in digits:
            if len(segment_map_lengths[len(digit)]) == 1:
                easy_numbers += 1

    return easy_numbers
    