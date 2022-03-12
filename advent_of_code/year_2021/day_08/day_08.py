from typing import List

"""This module implements the 8th day of 2021 Advent Of Code: 'Seven Segment Search'

See https://adventofcode.com/2021/day/8"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = content
    solution = 26

    assert count_increases(puzzle_input) == solution


def count_increases(notes: List[str]) -> int:
    digits_1_4_7_8 = 0

    for line in notes:
        _, output = line.split('|')
        
        for value in output.split():
            if len(value) in (2, 4, 3, 7):
                digits_1_4_7_8 += 1

    return digits_1_4_7_8


if __name__ == '__main__':
    main()
