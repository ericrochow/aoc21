#!/usr/bin/env python

from solutions.utils import read_input


class Day1:
    def __init__(self):
        self.day = 1
        self.day_input = [int(x) for x in read_input(self.day)]

    @staticmethod
    def compare_depths(current_depth: int, previous_depth: int) -> bool:
        """"""
        if previous_depth:
            if current_depth > previous_depth:
                return True

    def part1(self) -> int:
        """"""
        previous_depth = None
        increases = []
        for current_depth in self.day_input:
            if self.compare_depths(current_depth, previous_depth):
                increases.append(current_depth)
            previous_depth = current_depth
        return len(increases)

    def part2(self):
        pass


if __name__ == "__main__":
    day = Day1()
    p1 = day.part1()
    p2 = day.part2()
    print(p1)
    print(p2)
