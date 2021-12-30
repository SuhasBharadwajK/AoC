def parse_input(input_lines):
    template_string: str = input_lines[0]
    insertion_rules_list: list[tuple[str]] = list(map(lambda x: tuple(map(lambda y: y.strip(), x.split('->'))), input_lines[2:]))
    insertion_rules: dict[str:str] = {}
    for rule in insertion_rules_list:
        insertion_rules[rule[0]] = rule[1]

    return template_string, insertion_rules

def get_min_and_max_occurrence_difference(element_occurrence_map: dict[str:int]):
    occurrence_element_map = {value: key for (key, value) in element_occurrence_map.items()}
    max_occurrence: int = max(occurrence_element_map)
    min_occurrence: int = min(occurrence_element_map)
    
    return max_occurrence - min_occurrence
