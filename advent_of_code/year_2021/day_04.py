from typing import List

import numpy as np

"""This module implements the 4th day of 2021 Advent Of Code: 'Giant Squid'

See https://adventofcode.com/2021/day/4"""


def main():
    puzzle_input = ('7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
                    ['22 13 17 11  0\
                       8  2 23  4 24\
                      21  9 14 16  7\
                       6 10  3 18  5\
                       1 12 20 15 19',
                     ' 3 15  0  2 22\
                       9 18 13 17  5\
                      19  8  7 25 23\
                      20 11 10 24  4\
                      14 21 16 12  6',
                     '14 21 17 24  4\
                      10 16 15  9 19\
                      18  8 23 26 20\
                      22 11 13  6  5\
                       2  0 12  3  7'])
    solution = 4512

    assert calculate_power_consumption(*puzzle_input) == solution


def calculate_power_consumption(draw: str, boards: List[str]) -> int:
    draw = np.fromstring(draw, dtype=int, sep=',')
    boards = [np.fromstring(board, dtype=int, sep=' ').reshape((5, 5)) for board in boards]

    for val in draw:
        for board in boards:
            indices = np.where(board == val)

            if indices:
                i, j = indices[0][0], indices[1][0]
                board[i][j] = -1

                if board[:, j].sum() == -5 or board[i, :].sum() == -5:
                    return board[board > -1].sum() * val


if __name__ == '__main__':
    main()
