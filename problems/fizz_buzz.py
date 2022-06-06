from typing import List


class FizzBuzz:
    """
    Implements the "FizzBuzz" problem, for numbers 1 to 100 included.

    Reference: https://en.wikipedia.org/wiki/Fizz_buzz
    """

    @staticmethod
    def compute() -> List[str]:
        output = [''] * 100

        for n in range(1, 101):
            s = ''

            if n % 3 == 0:
                s += 'fizz'
            if n % 5 == 0:
                s += 'buzz'

            output[n - 1] = s if len(s) else str(n)

        return output
