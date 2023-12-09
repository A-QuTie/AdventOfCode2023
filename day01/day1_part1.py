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

with open("day1input.txt", 'r', encoding = 'utf-8') as f:
    calibration_value: int = 0;
    while line := f.readline().strip():
        for n in list(numwords.keys()):
            line.replace(n, numwords[n])
        nums = re.findall(r"[0-9]", line);
        val: int = int(nums[0] + nums[-1]);
        calibration_value += val;
        

    print(f"Calibration value is: {calibration_value}")