import pytest

import day_03.day_03 as solution


@pytest.fixture
def sample_input():
    return solution.read_input("day_03/inputs/day_03_sample.txt")


def test_calculate_power_consumption(sample_input):
    assert solution.calculate_power_consumption(sample_input) == 198
