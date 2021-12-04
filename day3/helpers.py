def binary_to_decimal(binary_number):
    number = 0
    length = len(binary_number)
    for i in range(0, length):
        power = length - i - 1
        number += (2 ** power) * int(binary_number[i])

    return number