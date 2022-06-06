class PalindromeNumber:
    """
    Given an integer ``n``, return ``True`` if ``n`` is a palindrome integer.

    Constraints:
      * ``-2e31 <= n <= 2e31 - 1``

    Reference: https://leetcode.com/problems/palindrome-number/
    """

    @staticmethod
    def is_palindrome_using_string(n: int) -> bool:
        if n < 0 or (n > 0 and n % 10 == 0):
            return False

        s = str(n)

        return s == s[::-1]

    @staticmethod
    def is_palindrome_using_arithmetic(n: int) -> bool:
        if n < 0 or (n > 0 and n % 10 == 0):
            return False

        output = 0

        while n > output:
            output = output * 10 + n % 10
            n //= 10

        return n == output or n == output // 10
