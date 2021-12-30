import day14.helpers as helpers
import copy

def program(input_lines):
    template, insertion_rules = helpers.parse_input(input_lines)
    template_map = get_template_map(template)
    steps_required = 40
    new_map = insert(template_map, insertion_rules, steps_required)
    last = template[-1:]
    count_map = get_count_map(new_map, last)
    diff = helpers.get_min_and_max_occurrence_difference(count_map)
    return diff

def insert(template_map: dict[str:int], insertion_rules: dict[str:str], steps: int):
    for step in range(steps):
        new_map = {}
        for pair in template_map:
            if pair in insertion_rules:
                element = insertion_rules[pair]
                new_pairs = pair[0] + element, element + pair[1]
                for new_pair in new_pairs:
                    if new_pair not in new_map:
                        new_map[new_pair] = 0

                    new_map[new_pair] += template_map[pair]

        template_map = copy.deepcopy(new_map)
    
    return template_map

def get_count_map(template_map, last: str = None):
    count_map = {}
    index = 0
    for key in template_map:
        if key[0] not in count_map:
            count_map[key[0]] = 0

        count_map[key[0]] += template_map[key]
        index += 1

        if index == len(template_map) - 1 and last is not None:
            if last not in count_map:
                count_map[last] = 0

            count_map[last] += 1
    
    return count_map

def get_template_map(template):
    template_map: dict[str:int] = {}
    for i in range(len(template) - 1):
        key = template[i : i + 2]

        if key not in template_map:
            template_map[key] = 0

        template_map[template[i : i + 2]] += 1
    
    return template_map
