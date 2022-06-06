from problems.two_sum import TwoSum


def test_two_sum():
    assert TwoSum.find_indices([2, 7, 11, 15], 9) == [0, 1]
    assert TwoSum.find_indices([3, 2, 4], 6) == [1, 2]
    assert TwoSum.find_indices([3, 3], 6) == [0, 1]
