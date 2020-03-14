from shared import *

def get_days_with_invalid_hour(file, base_system):
    days = {}
    index = 0
    prev_hour = 0
    with open(file, "r") as file:
        for line in file.readlines():
            parsed_line = parse_line(line)
            hour = int(parsed_line[0], base_system)
            if index == 0:
                prev_hour = hour
            elif hour - prev_hour != 24:
                days[index] = True
                prev_hour += 24
            else:
                prev_hour += 24
            index += 1
    return days


station_1 = get_days_with_invalid_hour("dane_systemy1.txt", 2)
station_2 = get_days_with_invalid_hour("dane_systemy2.txt", 4)
station_3 = get_days_with_invalid_hour("dane_systemy3.txt", 8)
count = 0
for key in station_1.keys():
    if key in station_2 and key in station_3:
        count+=1
print(count)