from shared import *


def get_min_temperature(file, base_system):
    min_temperature = 99999
    min_temperature_str = ""
    with open(file, "r") as file:
        for line in file.readlines():
            parsed_line = parse_line(line)
            #hour = int(parsed_line[0], base_system)
            temperature = int(parsed_line[1], base_system)
            if temperature < min_temperature:
                min_temperature = temperature
                min_temperature_str = convert_from_decimal(temperature, 2)
    return min_temperature_str


print(get_min_temperature("dane_systemy1.txt", 2), get_min_temperature("dane_systemy2.txt", 4), get_min_temperature("dane_systemy3.txt", 8))
