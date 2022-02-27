from typing import List

import numpy as np

"""This module implements the 3rd day of 2021 Advent Of Code: 'Binary Diagnostic'

See https://adventofcode.com/2021/day/3"""


def main():
    puzzle_input = ['00100',
                    '11110',
                    '10110',
                    '10111',
                    '10101',
                    '01111',
                    '00111',
                    '11100',
                    '10000',
                    '11001',
                    '00010',
                    '01010']
    solution = 198

    assert (calculate_power_consumption(puzzle_input) == solution)


def calculate_power_consumption(report: List[str]) -> int:
    report_size = len(report)
    ones = np.zeros(len(report[0]), dtype=int)

    for line in report:
        ones += np.array(list(line), dtype=int)

    gamma_rate = np.vectorize(lambda x: 1 if x >= report_size // 2 else 0)(ones)
    epsilon_rate = np.vectorize(lambda x: 1 if x == 0 else 0)(gamma_rate)

    gamma_rate = int(''.join(str(n) for n in gamma_rate), base=2)
    epsilon_rate = int(''.join(str(n) for n in epsilon_rate), base=2)

    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    main()
