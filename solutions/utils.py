#!/usr/bin/env python3

from pathlib import Path


HERE = Path(__file__).parent.absolute()


def read_input(day: int) -> list:
    """
    Read the specified day's input file.txt

    Args:
        day: An integer specifying which day's input file to read.
    Returns:
        A list containing the input values as a list.
    """
    input_file = HERE / ".." / "inputs" / f"day{day}.txt"
    with open(input_file) as f:
        output = f.read().splitlines()
    return output
