import utils
import day1.program as day1code

def get_input_data(day_number, input_number, formatter):
    input_path = './day' + str(day_number) + '/inputs/' + str(input_number) + '.txt'
    input_lines = utils.read_file(input_path)
    input_data = list(map(formatter, input_lines))
    return input_data

def day1():
    formatter = lambda x: int(x)
    input_data = get_input_data(1, 1, formatter)
    return day1code.program(input_data)

def day2():
    pass

if __name__ == '__main__':
    print(day1())
    pass
