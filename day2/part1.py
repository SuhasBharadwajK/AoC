def program(instructions):
    horizontal_position = 0
    depth_position = 0
    for instruction in instructions:
        if instruction[0] == 'forward':
            horizontal_position += instruction[1]

        elif instruction[0] == 'up':
            depth_position -= instruction[1]

        elif instruction[0] == 'down':
            depth_position += instruction[1]
        
    result = horizontal_position * depth_position
    return result