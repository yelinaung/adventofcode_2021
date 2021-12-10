import pytest

import day_02.day_02 as d2


@pytest.fixture
def sample_input():
    return d2.read_input("day_02/inputs/day_02_sample.txt")


def test_calculate_position(sample_input):
    assert d2.calcuate_position(sample_input) == 150


def test_calculate_aim(sample_input):
    assert d2.calculate_aim(sample_input) == 900
