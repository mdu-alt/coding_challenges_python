from collections import deque
from typing import List

import pytest

from problems.merge_k_iterators import Iterator, MinIterator


class _Deque(Iterator):
    def __init__(self, input_: List[int]):
        self._deque = deque(input_)

    def has_next(self) -> bool:
        return len(self._deque) != 0

    def next(self) -> int:
        return self._deque.popleft()

    def peek(self) -> int:
        return self._deque[0]

    def append(self, value: int) -> None:
        self._deque.append(value)


def test_three_iterators__example():
    mi = MinIterator([_Deque([1, 2, 3, 4]), _Deque([5, 6, 7, 8]), _Deque([4, 4, 5, 9])])

    assert mi.has_next() is True
    assert mi.peek() == 1
    assert mi.next() == 1
    assert mi.peek() == 2
    assert mi.next() == 2
    assert mi.next() == 3
    assert mi.has_next() is True
    assert mi.next() == 4
    assert mi.next() == 4


def test_one_iterator__empty():
    mi = MinIterator([_Deque([])])

    assert mi.has_next() is False

    with pytest.raises(IndexError) as excinfo:
        mi.next()
        assert "Iterator is empty" in str(excinfo.value)
    with pytest.raises(IndexError):
        mi.peek()
        assert "Iterator is empty" in str(excinfo.value)


def test_one_iterator__single_element():
    mi = MinIterator([_Deque([0])])

    assert mi.has_next() is True
    assert mi.peek() == 0
    assert mi.next() == 0
    assert mi.has_next() is False

    with pytest.raises(IndexError) as excinfo:
        mi.next()
        assert "Iterator is empty" in str(excinfo.value)
    with pytest.raises(IndexError) as excinfo:
        mi.peek()
        assert "Iterator is empty" in str(excinfo.value)


def test_two_iterators__interleaved():
    mi = MinIterator([_Deque([1, 3, 5, 7]), _Deque([2, 4, 6, 8])])

    assert mi.has_next() is True
    assert mi.next() == 1
    assert mi.peek() == 2
    assert mi.peek() == 2
    assert mi.next() == 2
    assert mi.next() == 3


def test_two_iterators__pushed_after():
    deque_1, deque_2 = _Deque([3]), _Deque([7])
    mi = MinIterator([deque_1, deque_2])

    assert mi.has_next() is True
    assert mi.next() == 3
    assert mi.peek() == 7
    assert mi.next() == 7
    assert mi.has_next() is False

    deque_1.append(14)
    deque_2.append(9)

    assert mi.has_next() is True
    assert mi.peek() == 9
    assert mi.next() == 9
    assert mi.next() == 14
    assert mi.has_next() is False
