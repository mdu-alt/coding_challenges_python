import day_02

example = day_02.read_file('example.txt')


def test_count_increases_part_1():
    assert day_02.part_1(example) == (15, 10, 150)  # h, d, h * d


def test_count_increases_part_2():
    assert day_02.part_2(example) == (15, 60, 900)  # h, d, h * d
