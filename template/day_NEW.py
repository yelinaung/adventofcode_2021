"""
Solution for https://adventofcode.com/2021/day/...
"""

from typing import List


def read_input(file_path) -> List[int]:
    with open(file_path) as file:
        return [line.split(" ") for line in file.read().splitlines() if line]
