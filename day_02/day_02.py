"""
Solution for https://adventofcode.com/2021/day/2
"""

from typing import List

def read_input(file_path) -> List[int]:
    with open(file_path) as file:
        input = [
            line.split(" ") for line in file.read().splitlines() if line
        ]
        return [{
            "direction": i[0],
            "unit": int(i[1]),
        } for i in input]

def calcuate_position(positions):
    total_forward = 0
    total_depth = 0
    for position in positions:
        direction = position["direction"]
        unit = position["unit"]
        if direction == "forward":
            total_forward += unit
        elif direction == "down":
            total_depth += unit
        elif direction == "up":
            total_depth -= unit

    return total_forward * total_depth

print(calcuate_position(read_input("day_02/inputs/day_02_input.txt")))
# print(find_three_measurements_sum(read_input("day_01/inputs/day_one_input.txt")))
