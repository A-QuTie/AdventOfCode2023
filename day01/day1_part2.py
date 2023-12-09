#!/usr/bin/python3

import re

numwords = {
    "one": "on1e",
    "two": "tw2o",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "eig8ht",
    "nine": "ni9ne"
}

"""
Not even used
"""
def str_to_nums(nums: list[str]):
    str_numbers: list[str] = []
    for num in nums:
        if num in numwords.keys():
            str_numbers.append(numwords[num])
        else:
            str_numbers.append(num)
    return str_numbers


# numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 1, 2, 3, 4, 5, 6, 7, 8, 9]
# regex_string = r"one|two|three|four|five|six|seven|eight|nine|[0-9]"
with open("day1input.txt", 'r', encoding='utf-8') as f:
    calibration_value: int = 0
    while line := f.readline().strip():
        print(line)
        for n in numwords.keys():
            line = line.replace(n, numwords[n])
        print(line)
        nums = re.findall(r"[0-9]", line)
        
        value: int = int(nums[0] + nums[-1])
        
        calibration_value += value
    print(f"Calibration value: {calibration_value}")
