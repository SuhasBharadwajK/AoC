import utils
import copy
import day1.part1 as d1p1
import day1.part2 as d1p2
import day2.part1 as d2p1
import day2.part2 as d2p2
import day3.part1 as d3p1
import day3.part2 as d3p2
import day4.part1 as d4p1
import day4.part2 as d4p2
import day5.part1 as d5p1
import day5.part2 as d5p2
import day6.part1 as d6p1
import day6.part2 as d6p2
import day8.part1 as d8p1
import day8.part2 as d8p2
import day9.part1 as d9p1
import day9.part2 as d9p2
import day10.part1 as d10p1
import day10.part2 as d10p2
import day11.part1 as d11p1
import day11.part2 as d11p2
import day12.part1 as d12p1
import day12.part2 as d12p2
import day13.part1 as d13p1
import day13.part2 as d13p2

def get_input_data(day_number, input_number, formatter, is_single_line = False):
    input_path = './day' + str(day_number) + '/inputs/' + str(input_number) + '.txt'
    input_lines = utils.read_file(input_path)
    input_data = list(map(formatter, input_lines))
    if is_single_line:
        input_data = input_data[0]
    return input_data

def day1():
    formatter = lambda x: int(x)
    input_data = get_input_data(1, 1, formatter)
    return d1p1.program(input_data), d1p2.program_optimized(input_data)

def day2():
    formatter = lambda x: [x.split(' ')[0], int(x.split(' ')[1])]
    input_data = get_input_data(2, 1, formatter)
    return d2p1.program(input_data), d2p2.program(input_data)

def day3():
    formatter = lambda x: x.strip()
    input_data = get_input_data(3, 1, formatter)
    return d3p1.program(input_data), d3p2.program(input_data)

def day4():
    formatter = lambda x: x.strip()
    input_data = get_input_data(4, 1, formatter)
    return d4p1.program(input_data), d4p2.program(input_data)

def day5():
    formatter = lambda x: tuple(map(lambda y: tuple(map(lambda z: int(z), y.strip().split(','))), x.split(' -> ')))
    input_data = get_input_data(5, 1, formatter)
    return d5p1.program(input_data), d5p2.program(input_data)

def day6():
    formatter = lambda x: list(map(lambda y: int(y), x.split(',')))
    input_data = get_input_data(6, 1, formatter, True)
    return d6p1.program(input_data), d6p2.program(input_data)

def day8():
    formatter = lambda x: list(map(lambda y: y.strip(), x.split('|')))
    input_data = get_input_data(8, 1, formatter)
    return d8p1.program(input_data), d8p2.program(input_data)

def day9():
    formatter = lambda x: list(map(lambda y: int(y), list(x.strip())))
    input_data = get_input_data(9, 1, formatter)
    return d9p1.program(input_data), d9p2.program(input_data)

def day10():
    formatter = lambda x: x.strip()
    input_data = get_input_data(10, 1, formatter)
    return d10p1.program(input_data), d10p2.program(input_data)

def day11():
    formatter = lambda x: list(map(lambda y: int(y), list(x.strip())))
    input_data = get_input_data(11, 1, formatter)[:]
    return d11p1.program(copy.deepcopy(input_data)), d11p2.program(input_data[:])

def day12():
    formatter = lambda x: x.strip().split('-')
    input_data = get_input_data(12, 3, formatter)
    return d12p1.program(copy.deepcopy(input_data)), d12p2.program(input_data)

def day13():
    formatter = lambda x: x.strip()
    input_data = get_input_data(13, 1, formatter)
    return d13p1.program(copy.deepcopy(input_data)), d13p2.program(input_data)

if __name__ == '__main__':
    print('Day 1 : ' + str(day1()))
    print('Day 2 : ' + str(day2()))
    print('Day 3 : ' + str(day3()))
    print('Day 4 : ' + str(day4()))
    print('Day 5 : ' + str(day5()))
    print('Day 6 : ' + str(day6()))
    print('Day 8 : ' + str(day8()))
    print('Day 9 : ' + str(day9()))
    print('Day 10: ' + str(day10()))
    print('Day 11: ' + str(day11()))
    print('Day 12: ' + str(day12()))
    print('Day 13: ' + str(day13()))
