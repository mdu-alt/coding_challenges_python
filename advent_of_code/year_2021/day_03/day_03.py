from typing import List

import numpy as np

"""This module implements the 3rd day of 2021 Advent Of Code: 'Binary Diagnostic'

See https://adventofcode.com/2021/day/3"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = content
    solution = 198

    assert calculate_power_consumption(puzzle_input) == solution


def calculate_power_consumption(report: List[str]) -> int:
    report_size = len(report)
    ones_count = np.zeros(len(report[0]), dtype=int)

    for row in report:
        ones_count += np.array(list(row), dtype=int)

    gamma_rate, epsilon_rate = 0, 0

    for n in ones_count:
        bit = (n >= report_size // 2)
        gamma_rate = (gamma_rate << 1) + bit
        epsilon_rate = (epsilon_rate << 1) + (1 - bit)

    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    main()
