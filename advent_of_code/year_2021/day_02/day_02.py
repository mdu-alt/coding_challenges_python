from typing import List, Tuple

"""This module implements the 2nd day of 2021 Advent Of Code: 'Dive!'

See https://adventofcode.com/2021/day/2"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = content
    solution = (15, 10, 150)  # h, d, h * d

    assert calculate_position(puzzle_input) == solution


def calculate_position(instructions: List[str]) -> Tuple[int, int, int]:
    h, d = 0, 0

    for instruction in instructions:
        direction, value = instruction.split()
        value = int(value)

        if direction == 'forward':
            h += value
        elif direction == 'down':
            d += value
        elif direction == 'up':
            d -= value

    return h, d, h * d


if __name__ == '__main__':
    main()
