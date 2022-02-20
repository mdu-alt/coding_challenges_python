import queue

import numpy as np

"""This module implements the 11th day of 2021 Advent Of Code: 'Dumbo Octopus'

See https://adventofcode.com/2021/day/11"""


def main():
    puzzle_input = ["5483143223",
                    "2745854711",
                    "5264556173",
                    "6141336146",
                    "6357385478",
                    "4167524645",
                    "2176841721",
                    "6882881134",
                    "4846848554",
                    "5283751526"]
    solution = 1656

    matrix = np.array([np.array(list(row), dtype=int) for row in puzzle_input], dtype=int)
    assert (count_flashes(matrix, 100) == solution)


def count_flashes(matrix: np.ndarray, cycles: int):
    """Count the number of flashes over some cycles."""
    flashes = 0

    for _ in range(cycles):
        matrix += 1

        for (i, j), _ in np.ndenumerate(matrix):
            if matrix[i][j] == 10:
                flashes += 1 + _flash_around(matrix, i, j)

    print("flashes:", flashes)
    return flashes


def _flash_around(matrix: np.ndarray, x: int, y: int):
    """Increment a cell's surrounding by one, and repeat the operation for any neighbor whose value is greater than 1
    (BFS)."""
    flashes = 0
    q = queue.SimpleQueue()

    for i in range(x - 1, x + 2):
        if not (0 <= i < len(matrix)):
            continue

        for j in range(y - 1, y + 2):
            if not (0 <= j < len(matrix[i])) or matrix[i][j] > 9 or matrix[i][j] == 0:
                continue

            matrix[i][j] += 1

            if matrix[i][j] == 10:
                flashes += 1
                q.put((i, j))

    matrix[x][y] = 0

    while not q.empty():
        x, y = q.get()
        flashes += _flash_around(matrix, x, y)

    return flashes


if __name__ == "__main__":
    main()
