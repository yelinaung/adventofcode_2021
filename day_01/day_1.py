"""
Solution for https://adventofcode.com/2021/day/1
"""
from itertools import pairwise


# using pairwise to get the previous and next value
# https://twitter.com/mathsppblog/status/1466018491253854213
def find_larger_measurements(file_path) -> int:
    with open(file_path) as file:
        measurements = [int(line) for line in file.read().splitlines()]

    return sum(p2 > p1 for p1, p2 in pairwise(measurements))
