#!/usr/bin/python3


def max_cubes(cubes: dict[str, int]):
    c = {}
    for color in ["red", "green", "blue"]:
            c[color] = max(cubes[color])
    return c

def cube_power(cubes: dict[str, int]):
    cp = 1
    for c in cubes.values():
        cp *= c
    # print(cp)
    return cp

def init_cubes():
    with open("day02input.txt", "r", encoding="utf-8") as f:
        power_of_cubes = 0
        while line := f.readline().strip():
            game, line = line.split(":")
            sets = line.split(";")
            num_cubes = {}
            for s in sets:

                cubes = s.split(",")

                for cube in cubes:

                    num, color = cube.strip().split(" ")
                    if color not in num_cubes:
                        num_cubes[color] = [int(num)]
                    else:
                        num_cubes[color].append(int(num))

            print(game, max_cubes(num_cubes))
            # cube_power(max_cubes(num_cubes))
            power_of_cubes += cube_power(max_cubes(num_cubes))
            print(power_of_cubes)
        

def main():
    init_cubes()
    
if __name__ == "__main__":
    main()