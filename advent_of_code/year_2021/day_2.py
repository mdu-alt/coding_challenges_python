from typing import List

"""This module implements the 2nd day of 2021 Advent Of Code: 'Dive!'

See https://adventofcode.com/2021/day/2"""


def main():
    puzzle_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    solution = (15, 10, 150)  # h, d, h * d

    assert (calculate_position(puzzle_input) == solution)


def calculate_position(instructions: List[str]):
    """Calculate the height, depth, and product of both after executing all the instruction in input."""
    (h, d) = (0, 0)

    for instruction in instructions:
        (direction, value) = instruction.split()
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
