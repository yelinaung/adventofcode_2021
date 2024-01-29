"""
Solution for https://adventofcode.com/2021/day/1
"""

import collections
from itertools import islice, pairwise
from typing import List


# from https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def read_input(file_path) -> List[int]:
    with open(file_path) as file:
        return [int(line) for line in file.read().splitlines() if line]


# using pairwise to get the previous and next value
# https://twitter.com/mathsppblog/status/1466018491253854213
def find_larger_measurements(measurements) -> int:
    return sum(p2 > p1 for p1, p2 in pairwise(measurements))


def find_three_measurements_sum(measurements) -> int:
    sums = [sum(sw) for sw in sliding_window(measurements, 3)]
    return find_larger_measurements(sums)


# print(find_larger_measurements(read_input("day_01/inputs/day_one_input.txt")))
# print(find_three_measurements_sum(read_input("day_01/inputs/day_one_input.txt")))
