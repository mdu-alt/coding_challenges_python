from problems.palindrome_number import PalindromeNumber


def test_is_palindrome():
    assert PalindromeNumber.is_palindrome_using_string(0) is True
    assert PalindromeNumber.is_palindrome_using_string(121) is True
    assert PalindromeNumber.is_palindrome_using_string(555555) is True
    assert PalindromeNumber.is_palindrome_using_string(990434099) is True

    assert PalindromeNumber.is_palindrome_using_arithmetic(0) is True
    assert PalindromeNumber.is_palindrome_using_arithmetic(121) is True
    assert PalindromeNumber.is_palindrome_using_arithmetic(555555) is True
    assert PalindromeNumber.is_palindrome_using_arithmetic(990434099) is True


def test_is_not_palindrome():
    assert PalindromeNumber.is_palindrome_using_string(-1) is False
    assert PalindromeNumber.is_palindrome_using_string(-55555) is False
    assert PalindromeNumber.is_palindrome_using_string(129585920) is False
    assert PalindromeNumber.is_palindrome_using_string(1233433211) is False

    assert PalindromeNumber.is_palindrome_using_arithmetic(-1) is False
    assert PalindromeNumber.is_palindrome_using_arithmetic(-55555) is False
    assert PalindromeNumber.is_palindrome_using_arithmetic(129585920) is False
    assert PalindromeNumber.is_palindrome_using_arithmetic(1233433211) is False
