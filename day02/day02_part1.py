#!/usr/bin/python3



cube_colors: dict[str, list[int]] = {}

cube_colors["red"]: str = int(input("How many red cubes? "))
cube_colors["green"]: str = int(input("How many green cubes? "))
cube_colors["blue"]: str = int(input("How many blue cubes? "))

def check_cubes(cubes: dict[str, int]):
    for color in cube_colors:
        for 


with open("day02input.txt", "r", encoding="utf-8") as f:
    valid_games = [];
    while line := f.readline().strip():
        game, line = line.split(":")
        sets = line.split(";")
        num_cubes = {}
        for s in sets:
            num, cube = cube.split()
            if cube not in num_cubes:
                num_cubes[cube] = int(num)
            else:
                num_cubes[cube] += int(num)
        print(game, num_cubes)
        if num_cubes["red"] > red or num_cubes["green"] > green or num_cubes["blue"] > blue:
            continue
        valid_games.append(game)

    print(valid_games)

        

