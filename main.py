import utils
import day1.part1 as d1p1
import day1.part2 as d1p2

def get_input_data(day_number, input_number, formatter):
    input_path = './day' + str(day_number) + '/inputs/' + str(input_number) + '.txt'
    input_lines = utils.read_file(input_path)
    input_data = list(map(formatter, input_lines))
    return input_data

def day1part1():
    formatter = lambda x: int(x)
    input_data = get_input_data(1, 1, formatter)
    return d1p1.program(input_data)

def day1part2():
    formatter = lambda x: int(x)
    input_data = get_input_data(1, 1, formatter)
    return d1p2.program_optimized(input_data)

if __name__ == '__main__':
    print('Day 1 Part 1: ' + str(day1part1()))
    print('Day 1 Part 2: ' + str(day1part2()))
