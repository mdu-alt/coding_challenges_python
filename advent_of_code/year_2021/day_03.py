from typing import List

import numpy as np

"""This module implements the 3rd day of 2021 Advent Of Code: 'Binary Diagnostic'

See https://adventofcode.com/2021/day/3"""


def main():
    puzzle_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010',
                    '01010']
    solution = 198

    assert calculate_power_consumption(puzzle_input) == solution


def calculate_power_consumption(report: List[str]) -> int:
    report_size = len(report)
    ones_count = np.zeros(len(report[0]), dtype=int)

    for row in report:
        ones_count += np.array(list(row), dtype=int)

    gamma_rate, epsilon_rate = 0, 0

    for val in ones_count:
        bit = val >= report_size // 2
        gamma_rate = (gamma_rate << 1) + bit
        epsilon_rate = (epsilon_rate << 1) + (1 - bit)

    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    main()
