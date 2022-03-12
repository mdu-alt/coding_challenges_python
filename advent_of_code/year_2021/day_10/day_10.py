from typing import List

"""This module implements the 10th day of 2021 Advent Of Code: 'Syntax Scoring'

See https://adventofcode.com/2021/day/10"""


def main():
    with open('example.txt') as f:
        content = f.read().splitlines()

    puzzle_input = content
    solution = 26397

    assert compute_total_syntax_error_score(puzzle_input) == solution


def compute_total_syntax_error_score(lines: List[str]) -> int:
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

    stack: List[str] = []
    points = 0

    for line in lines:
        for ch in line:
            if stack:
                if ch in pairs:
                    if pairs[ch] == stack[-1]:
                        stack.pop()
                        continue
                    else:
                        points += scores[ch]
                        break

            stack.append(ch)

    return points


if __name__ == '__main__':
    main()
