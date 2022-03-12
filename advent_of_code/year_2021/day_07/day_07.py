import statistics
from typing import List

"""This module implements the 7th day of 2021 Advent Of Code: 'The Treachery of Whales'

See https://adventofcode.com/2021/day/7"""


def main():
    with open('example.txt') as f:
        content = f.read()

    puzzle_input = list(map(int, content.split(',')))
    solution = 37

    assert find_cheapest_fuel_consumption(puzzle_input) == solution


def find_cheapest_fuel_consumption(positions: List[int]) -> int:
    mean = statistics.median(positions)
    consumption = 0

    for n in positions:
        consumption += abs(n - mean)

    return consumption


if __name__ == '__main__':
    main()
