import sys

from abc import abstractmethod, ABC
from typing import List, Optional


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        """
        :return: ``True`` if the iteration has more elements, ``False`` otherwise.
        """
        pass

    @abstractmethod
    def next(self) -> int:
        """
        :return: The next element in the iteration; should move the iteration to the next element, or raise an error if
                 no more elements.
        """
        pass

    @abstractmethod
    def peek(self) -> int:
        """
        :return: The next element in the iteration; should return the value of the next element, or raise an error if
                 no more elements.
        """
        pass


class MinIterator(Iterator):
    """
    Given an input list of ``Iterator``s, create a new ``Iterator`` whose ``next()`` and ``peek()`` methods return the
    minimum value from that list.
    """

    def __init__(self, iterators: List[Iterator]):
        self._iterators = iterators
        self._min_index = self._find_min()

    def has_next(self) -> bool:
        for iterator in self._iterators:
            if iterator.has_next():
                return True

        return False

    def next(self) -> int:
        self._assign_min_or_raise()
        next_ = self._iterators[self._min_index].next()
        self._min_index = self._find_min()

        return next_

    def peek(self) -> int:
        if self._min_index is None:
            self._assign_min_or_raise()

        return self._iterators[self._min_index].peek()

    def _assign_min_or_raise(self) -> None:
        if (min_index := self._find_min()) is None:
            raise IndexError("Iterator is empty")
        self._min_index = min_index

    def _find_min(self) -> Optional[int]:
        """
        Loop through all iterators and return the minimum element.

        :return: The index of the minimum element in ``self._iterators``, ``None`` otherwise.
        """
        index, minimum = None, sys.maxsize

        for i, iterator in enumerate(self._iterators):
            if iterator.has_next() and iterator.peek() <= minimum:
                minimum, index = iterator.peek(), i

        return index
