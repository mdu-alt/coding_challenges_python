from typing import List, Tuple

"""This module implements the 2nd day of 2021 Advent Of Code: 'Dive!'

See https://adventofcode.com/2021/day/2"""


def main():
    puzzle_input = read_file('puzzle_input.txt')

    print(part_1(puzzle_input), '== (horizontal, depth, horizontal*depth)')
    print(part_2(puzzle_input), '== (horizontal, depth, horizontal*depth)')


def part_1(instructions: List[str]) -> Tuple[int, int, int]:
    h = d = 0

    for instruction in instructions:
        direction, unit = instruction.split()
        unit = int(unit)

        if direction == 'forward':
            h += unit
        elif direction == 'down':
            d += unit
        elif direction == 'up':
            d -= unit

    return h, d, h * d


def part_2(instructions: List[str]) -> Tuple[int, int, int]:
    h = d = a = 0

    for instruction in instructions:
        direction, unit = instruction.split()
        unit = int(unit)

        if direction == 'forward':
            h += unit
            d += a * unit
        elif direction == 'down':
            a += unit
        elif direction == 'up':
            a -= unit

    return h, d, h * d


def read_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == '__main__':
    main()
