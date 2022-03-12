import numpy as np

"""This module implements the 9th day of 2021 Advent Of Code: 'Smoke Basin'

See https://adventofcode.com/2021/day/9"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = np.array([np.array(list(row), dtype=int) for row in content], dtype=int)
    solution = 15

    assert count_increases(puzzle_input) == solution


def count_increases(heightmap: np.ndarray) -> int:
    risk_level_sum = 0

    for (i, j), _ in np.ndenumerate(heightmap):
        if is_local_min(heightmap, i, j):
            risk_level_sum += heightmap[i][j] + 1

    return risk_level_sum


def is_local_min(matrix: np.ndarray, x: int, y: int) -> bool:
    v = matrix[x][y]

    if matrix[max(0, x - 1)][y] < v or matrix[min(np.size(matrix, 0) - 1, x + 1)][y] < v:
        return False
    elif matrix[x][max(0, y - 1)] < v or matrix[x][min(np.size(matrix, 1) - 1, y + 1)] < v:
        return False

    return True


if __name__ == '__main__':
    main()
