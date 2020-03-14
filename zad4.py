from shared import *

with open("dane_systemy1.txt") as file:
    numbers = []
    for line in file.readlines():
        parsed_line = parse_line(line)
        numbers.append(int(parsed_line[1], 2))
    max_difference = 0
    length = len(numbers)
    for i in range(length-1):
        for j in range(i+1, length, 1):
            r = (numbers[i] - numbers[j]) ** 2
            s = math.fabs(i - j)
            difference = 0
            if r > 0 and s > 0:
                difference = math.ceil(r/ s)
            if difference > max_difference:
                max_difference = difference
    print(max_difference)