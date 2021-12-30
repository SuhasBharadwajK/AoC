import day14.helpers as helpers

def program(input_lines):
    template, insertion_rules = helpers.parse_input(input_lines)
    steps_required = 10
    polymer = get_polymer(steps_required, template, insertion_rules)
    occurrences = get_element_occurrences(polymer)
    result = helpers.get_min_and_max_occurrence_difference(occurrences)
    return result

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
            pair = rule
            pair_match_indexes = get_substring_indexes(template, pair)

            for index in pair_match_indexes:
                rule_index_map[index] = (pair, insertion_rules[pair])

        elements_inserted = []
        last_template_index = 0
        index = 0
        while last_template_index < len(template):
            elements_inserted.append(template[last_template_index])
            last_template_index += 1

            if index in rule_index_map:
                rule = rule_index_map[index]
                element = insertion_rules[rule[0]]
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
