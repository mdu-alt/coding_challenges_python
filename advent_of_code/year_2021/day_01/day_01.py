from typing import List

"""This module implements the 1st day of 2021 Advent Of Code: 'Sonar Sweep'

See https://adventofcode.com/2021/day/1"""


def main():
    puzzle_input = read_file('puzzle_input.txt')

    print(part_1(puzzle_input), 'measurements are larger than the previous measurement.')
    print(part_2(puzzle_input), 'sums are larger than the previous sum.')


def part_1(measurements: List[int]) -> int:
    increases = 0

    for i, n in enumerate(measurements[1:]):
        increases += (n > measurements[i])

    return increases


def part_2(measurements: List[int]) -> int:
    increases = 0

    for i, n in enumerate(measurements[3:]):
        increases += (n > measurements[i])

    return increases


def read_file(filename: str) -> List[int]:
    with open(filename) as f:
        return list(map(int, f.read().splitlines()))


if __name__ == '__main__':
    main()
