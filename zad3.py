from shared import *


def get_station_record_days(file, base_system):
    days = {}
    prev_record = 0
    day = 0
    with open(file, "r") as file:
        for line in file.readlines():
            parsed_line = parse_line(line)
            temperature = int(parsed_line[1], base_system)
            if day == 0:
                prev_record = temperature
            elif prev_record < temperature:
                days[day] = temperature
                prev_record = temperature
            day += 1
    return days


cache = {}
count = 1
stations = [get_station_record_days("dane_systemy1.txt", 2),
            get_station_record_days("dane_systemy2.txt", 4),
            get_station_record_days("dane_systemy3.txt", 8)]
for obj in stations:
    for key in obj.keys():
        if key not in cache:
            count += 1
            cache[key] = obj[key]

print(count)
