from typing import List

import numpy as np

"""This module implements the 5th day of 2021 Advent Of Code: 'Hydrothermal Venture'

See https://adventofcode.com/2021/day/5"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = content
    solution = 5

    assert calculate_lines_overlap(puzzle_input) == solution


def calculate_lines_overlap(lines: List[str]) -> int:
    field = np.zeros((10, 10), dtype=int)

    for line in lines:
        coordinates = line.split(' -> ')
        x1, y1 = [int(n) for n in coordinates[0].split(',')]
        x2, y2 = [int(n) for n in coordinates[1].split(',')]

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            field[y1:y2 + 1, x1] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            field[y1, x1:x2 + 1] += 1

    return np.count_nonzero(field > 1)


if __name__ == '__main__':
    main()
