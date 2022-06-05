from problems.fizz_buzz import fizz_buzz


def test_fizz_buzz():
    output = fizz_buzz()

    assert output[0] == '1'
    assert output[2] == 'fizz'
    assert output[4] == 'buzz'
    assert output[14] == 'fizzbuzz'
    assert output[34] == 'buzz'
    assert output[63] == '64'
    assert output[86] == 'fizz'
    assert output[-1] == 'buzz'
