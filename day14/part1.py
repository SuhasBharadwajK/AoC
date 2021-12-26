import day14.helpers as helpers
import re

def program(input_lines):
    template, insertion_rules = helpers.parse_input(input_lines)
    steps_required = 10
    polymer = helpers.get_polymer(steps_required, template, insertion_rules)
    occurrences = helpers.get_element_occurrences(polymer)
    result = helpers.get_min_and_max_occurrence_difference(occurrences)
    return result
