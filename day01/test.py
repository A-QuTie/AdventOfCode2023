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

regex_string = r"one|two|three|four|five|six|seven|eight|nine|[0-9]"
line = "6oneightskl"
for n in numwords.keys():
    print(n)
    line = line.replace(n, numwords[n])

print(line)
# print(line.replace("eight", "ei8ght"))
n = re.findall(regex_string, line)
print(n)
# print(n)