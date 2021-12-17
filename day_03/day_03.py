"""
Solution for https://adventofcode.com/2021/day/...
"""

from collections import defaultdict
from typing import List


def read_input(file_path) -> List[int]:
    with open(file_path) as file:
        return [line.strip() for line in file if line]


def calculate_power_consumption(input_data):
    gamma, epsilon = "", ""
    for column in range(len(input_data[0])):
        counting = defaultdict(int)
        for line in input_data:
            counting[line[column]] += 1

        if counting["0"] > counting["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)


print(calculate_power_consumption(read_input("day_03/inputs/day_03_input.txt")))
