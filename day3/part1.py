import day3.helpers as helpers

def program(diagnostics):
    gamma_rate_code = ''
    epsilon_rate_code = ''
    
    for j in range(0, len(diagnostics[0])):
        count_of_1s = 0
        count_of_0s = 0
        
        for i in range(0, len(diagnostics)):
            digit = diagnostics[i][j]
            if digit == '1':
                count_of_1s += 1
            else:
                count_of_0s += 1
        
        if count_of_0s > count_of_1s:
            gamma_rate_code += '0'
            epsilon_rate_code += '1'
        else:
            gamma_rate_code += '1'
            epsilon_rate_code += '0'

    gamma_rate = helpers.binary_to_decimal(gamma_rate_code)
    epsilon_rate = helpers.binary_to_decimal(epsilon_rate_code)

    return gamma_rate * epsilon_rate