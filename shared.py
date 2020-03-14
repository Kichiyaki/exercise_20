import math
valid_chars = '0123456789ABCDEF'

def parse_line(line):
    return line.replace("\n", "").split(" ")

def convert_from_decimal(number, system):
    other_system_representation = ''
    is_greater_than_0 = True
    if number < 0:
        number *= -1
        is_greater_than_0 = False
    while number != 0:
        other_system_representation = valid_chars[number % system] \
            + other_system_representation
        number = math.floor(number / system)
    if not is_greater_than_0:
        other_system_representation = "-" + other_system_representation
    return other_system_representation