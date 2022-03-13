import day_01

example = day_01.read_file('example.txt')


def test_count_increases_part_1():
    assert day_01.part_1(example) == 7


def test_count_increases_part_2():
    assert day_01.part_2(example) == 5
