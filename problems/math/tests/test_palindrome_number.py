from problems.math.palindrome_number import PalindromeNumber


def test_is_palindrome():
    assert PalindromeNumber.is_palindrome(0) is True
    assert PalindromeNumber.is_palindrome(121) is True
    assert PalindromeNumber.is_palindrome(555555) is True
    assert PalindromeNumber.is_palindrome(990434099) is True

    assert PalindromeNumber.is_palindrome_with_string(0) is True
    assert PalindromeNumber.is_palindrome_with_string(121) is True
    assert PalindromeNumber.is_palindrome_with_string(555555) is True
    assert PalindromeNumber.is_palindrome_with_string(990434099) is True


def test_is_not_palindrome():
    assert PalindromeNumber.is_palindrome(-1) is False
    assert PalindromeNumber.is_palindrome(-55555) is False
    assert PalindromeNumber.is_palindrome(129585920) is False
    assert PalindromeNumber.is_palindrome(1233433211) is False

    assert PalindromeNumber.is_palindrome_with_string(-1) is False
    assert PalindromeNumber.is_palindrome_with_string(-55555) is False
    assert PalindromeNumber.is_palindrome_with_string(129585920) is False
    assert PalindromeNumber.is_palindrome_with_string(1233433211) is False
