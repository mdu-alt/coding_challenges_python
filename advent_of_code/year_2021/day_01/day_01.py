from typing import List

"""This module implements the 1st day of 2021 Advent Of Code: 'Sonar Sweep'

See https://adventofcode.com/2021/day/1"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = list(map(int, content))
    solution = 7

    assert count_increases(puzzle_input) == solution


def count_increases(measurements: List[int]) -> int:
    increases = 0
    previous = measurements[0]

    for n in measurements:
        increases += (n > previous)
        previous = n

    return increases


if __name__ == '__main__':
    main()
