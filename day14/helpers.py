def parse_input(input_lines):
    template_string: str = input_lines[0]
    insertion_rules: list[tuple[str]] = list(map(lambda x: tuple(map(lambda y: y.strip(), x.split('->'))), input_lines[2:]))
    return template_string, insertion_rules


def get_substring_indexes(source, sub):
    indexes = []
    for i in range(len(source) - 1):
        if source[i : i + 2] == sub:
            indexes.append(i)

    return indexes

def get_polymer(steps_required, template, insertion_rules):
    for step in range(steps_required):
        rule_index_map = {}
        for rule in insertion_rules:
            pair = rule[0]
            pair_match_indexes = get_substring_indexes(template, pair)

            for index in pair_match_indexes:
                rule_index_map[index] = rule

        elements_inserted = []
        last_template_index = 0
        index = 0
        while last_template_index < len(template):
            elements_inserted.append(template[last_template_index])
            last_template_index += 1

            if index in rule_index_map:
                rule = rule_index_map[index]
                element = rule[1]
                elements_inserted.append(element)

            index += 1
            
        template = ''.join(elements_inserted)

    return template

def get_element_occurrences(polymer: str):
    occurrence_map: dict[str:int] = {}
    for element in polymer:
        if element not in occurrence_map:
            occurrence_map[element] = 0

        occurrence_map[element] += 1
        
    return occurrence_map

def get_min_and_max_occurrence_difference(element_occurrence_map: dict[str:int]):
    occurrence_element_map = {value: key for (key, value) in element_occurrence_map.items()}
    max_occurrence = max(occurrence_element_map)
    min_occurrence = min(occurrence_element_map)
    
    return max_occurrence - min_occurrence
