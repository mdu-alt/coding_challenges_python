from typing import List

"""This module implements the 11st day of 2021 Advent Of Code: 'Sonar Sweep'

See https://adventofcode.com/2021/day/1"""


def main():
    puzzle_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    solution = 7

    assert (count_increases(puzzle_input) == solution)


def count_increases(arr: List[int]):
    """Count the number of times a depth measurements increases (from the previous measurements)."""
    increases = 0
    previous = arr[0]

    for elem in arr:
        if elem > previous:
            increases += 1
        previous = elem

    return increases


if __name__ == '__main__':
    main()
