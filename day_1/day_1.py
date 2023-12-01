import re


def get_values_for_calibration(data):
    numbers = re.findall(r'\d', data)
    return int(f"{numbers[0]}{numbers[-1]}")


def get_calibration_sum(data):
    data_list = [y for y in (x.strip() for x in data.splitlines()) if y]
    cal_list = []
    for elem in data_list:
        cal_list.append(get_values_for_calibration(elem))

    print(cal_list)
    return sum(cal_list)


##### PART 1 #####

with open('puzzle_input.txt', 'r') as file:
    puzzle_input = file.read()
print(puzzle_input)
print(get_calibration_sum(puzzle_input))
