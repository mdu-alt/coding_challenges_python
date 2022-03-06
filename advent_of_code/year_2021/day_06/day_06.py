from typing import List

import numpy as np

"""This module implements the 6th day of 2021 Advent Of Code: 'Lanternfish'

See https://adventofcode.com/2021/day/6"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = (list(map(int, content[0].split(','))), int(content[1]))
    solution = 5934

    assert count_lanternfish(*puzzle_input) == solution


def count_lanternfish(initial_state: List[int], days: int) -> int:
    state = np.array(initial_state)

    for _ in range(days):
        state = np.append(np.where(state == 0, 6, state - 1), np.repeat(8, np.count_nonzero(state == 0)))

    return state.size


if __name__ == '__main__':
    main()
