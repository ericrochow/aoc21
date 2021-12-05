#!/usr/bin/env python3

from solutions.day1 import Day1

test_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

day = Day1()
day.day_input = test_input


def test_compare_depths():
    assert day.compare_depths(8, 7)


def test_part1() -> int:
    assert day.part1() == 7


def test_part2():
    pass
