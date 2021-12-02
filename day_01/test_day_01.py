import pytest

import day_01.day_01_solution as d1


@pytest.fixture
def sample_input():
    return d1.read_input("day_01/inputs/day_one_input_2.txt")


def test_largest_measurement(sample_input):
    assert d1.find_larger_measurements(sample_input) == 7


def test_find_three_measurements_sum(sample_input):
    assert d1.find_three_measurements_sum(sample_input) == 5
