from typing import List


def fizz_buzz() -> List[str]:
    """
    Implements the "FizzBuzz" problem, for numbers 1 to 100 included (https://en.wikipedia.org/wiki/Fizz_buzz).
    """
    output: List[str] = []

    for n in range(1, 101):
        s = ''

        if n % 3 == 0:
            s += 'fizz'
        if n % 5 == 0:
            s += 'buzz'

        output.append(s if len(s) else str(n))

    return output
