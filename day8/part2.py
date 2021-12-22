import day8.helpers as helpers

def program(input_lines):
    total = 0
    segment_map_lengths = helpers.get_segment_map_lenghts()
    for line in input_lines:
        pattern = line[0]
        digits = line[1]
        mapping = generate_mapping(pattern, segment_map_lengths)
        num = deduce_number(mapping, digits)
        total += num
    
    return total

def generate_mapping(pattern: str, segment_map_lengths: dict[int: list]) -> dict[str: str]:
    number_patterns = pattern.split(' ')
    mapping: dict[str: str] = {}
    unique_number_segments = {}
    for number_pattern in number_patterns:
        for number in helpers.unique_numbers:
            if segment_map_lengths[len(number_pattern)][0] == number:
                unique_number_segments[number] = number_pattern

    segment_of_1 = unique_number_segments[1]

    segment_of_6 = [x for x in number_patterns if len(x) == 6 and len([y for y in segment_of_1 if y not in x]) == 1][0]

    char_in_1_but_not_6 = [x for x in segment_of_1 if x not in segment_of_6][0]
    mapping[char_in_1_but_not_6] = 'c'
    other_char_of_1 = [x for x in segment_of_1 if x != char_in_1_but_not_6][0]
    mapping[other_char_of_1] = 'f'

    segment_of_7 = unique_number_segments[7]
    char_only_in_7 = [x for x in segment_of_7 if x not in mapping][0]
    mapping[char_only_in_7] = 'a'

    segment_of_4 = unique_number_segments[4]
    chars_in_4_and_not_in_7 = [x for x in segment_of_4 if x not in segment_of_7]

    segment_of_3 = [x for x in number_patterns if len(x) == 5 and len([y for y in segment_of_1 if y in x]) == 2][0]
    char_absent_in_3 = [x for x in chars_in_4_and_not_in_7 if x not in segment_of_3][0]
    char_present_in_3 = [x for x in chars_in_4_and_not_in_7 if x in segment_of_3][0]

    mapping[char_absent_in_3] = 'b'
    mapping[char_present_in_3] = 'd'

    char_only_in_3 = [x for x in segment_of_3 if x not in mapping][0]

    mapping[char_only_in_3] = 'g'

    segment_of_8 = unique_number_segments[8]
    missing_char = [x for x in segment_of_8 if x not in mapping][0]
    mapping[missing_char] = 'e'

    return mapping


def deduce_digit(mapping: dict[str: str], digit_string: str):
    chars = list(digit_string)
    deduced_array = []
    for c in chars:
        deduced_array.append(mapping[c])

    deduced_array.sort()

    for k, v in helpers.segment_maps.items():
        if deduced_array == v:
            return str(k)


def deduce_number(mapping: dict[str: str], number_string: str):
    digits = number_string.split()
    number = ''
    for digit in digits:
        number += deduce_digit(mapping, digit)
    
    return int(number)