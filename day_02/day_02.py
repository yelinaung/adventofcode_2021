"""
Solution for https://adventofcode.com/2021/day/2
"""

from typing import List


def read_input(file_path) -> List[int]:
    with open(file_path) as file:
        input = [line.split(" ") for line in file.read().splitlines() if line]
        return [
            {
                "direction": i[0],
                "unit": int(i[1]),
            }
            for i in input
        ]


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


def calculate_aim(positions):
    total_forward = 0
    total_depth = 0
    aim = 0
    for position in positions:
        direction = position["direction"]
        unit = position["unit"]
        if direction == "down":
            aim += unit
        elif direction == "up":
            aim -= unit
        else:
            # forward X does two things:
            # It increases your horizontal position by X units.
            total_forward += unit
            # It increases your depth by your aim multiplied by X.
            total_depth += aim * unit

    return total_forward * total_depth


# print(calcuate_position(read_input("day_02/inputs/day_02_input.txt")))
# print(calculate_aim(read_input("day_02/inputs/day_02_input.txt")))
