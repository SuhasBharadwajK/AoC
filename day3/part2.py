import day3.helpers as helpers
from main import day1

def program(diagnostics):
    o2_value = helpers.binary_to_decimal(get_data(diagnostics, 0, True))
    co2_value = helpers.binary_to_decimal(get_data(diagnostics, 0, False))

    return o2_value * co2_value

def get_data(diagnostics, current_index, is_o2):
    result = []
    count_of_1s = 0
    count_of_0s = 0

    for i in range(0, len(diagnostics)):
        digit = diagnostics[i][current_index]
        if digit == '1':
            count_of_1s += 1
        else:
            count_of_0s += 1

    for i in range(0, len(diagnostics)):
        if count_of_1s >= count_of_0s:
            if diagnostics[i][current_index] == '1':
                if is_o2:
                    result.append(diagnostics[i])

            else:
                if not is_o2:
                    result.append(diagnostics[i])

        else:
            if diagnostics[i][current_index] == '0':
                if is_o2:
                    result.append(diagnostics[i])

            else:
                if not is_o2:
                    result.append(diagnostics[i])
    
    if len(result) == 1:
        return result[0]
    
    return get_data(result, current_index + 1, is_o2)