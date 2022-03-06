from typing import List

import numpy as np

"""This module implements the 4th day of 2021 Advent Of Code: 'Giant Squid'

See https://adventofcode.com/2021/day/4"""


def main():
    with open('example.txt') as f:
        content = f.read().split('\n\n')

    puzzle_input = (list(map(int, content[0].split(','))), content[1:])
    solution = 4512

    assert calculate_power_consumption(*puzzle_input) == solution


def calculate_power_consumption(draw: List[int], boards: List[str]) -> int:
    draw = np.array(draw, dtype=int)
    boards = [np.fromstring(board, dtype=int, sep=' ').reshape((5, 5)) for board in boards]

    for n in draw:
        for board in boards:
            indices = np.where(board == n)

            if indices:
                i, j = indices[0][0], indices[1][0]
                board[i][j] = -1

                if board[:, j].sum() == -5 or board[i, :].sum() == -5:
                    return board[board > -1].sum() * n


if __name__ == '__main__':
    main()
