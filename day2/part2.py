def program(instructions):
    aim = 0

    horizontal_position = 0
    depth_position = 0
    for instruction in instructions:
        direction = instruction[0]
        units = instruction[1]
        if direction == 'forward':
            horizontal_position += units
            depth_position += aim * units

        elif direction == 'up':
            aim -= units

        elif direction == 'down':
            aim += units
            
    result = horizontal_position * depth_position
    return result