#!/usr/bin/python3



cube_colors: dict[str, list[int]] = {}

cube_colors["red"]: str = int(input("How many red cubes? "))
cube_colors["green"]: str = int(input("How many green cubes? "))
cube_colors["blue"]: str = int(input("How many blue cubes? "))

def check_cubes(cubes: dict[str, int]) -> bool:
    for color in ["red", "green", "blue"]:
        for num_cubes in cubes[color]:
            if num_cubes > cube_colors[color]:
                return False
    return True

def init_cubes():
    with open("day02input.txt", "r", encoding="utf-8") as f:
        valid_games = [];
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

            if check_cubes(num_cubes):
                valid_games.append(int(game.split(" ")[1]))
        print(sum(valid_games))

def main():
    init_cubes()
    
if __name__ == "__main__":
    main()

