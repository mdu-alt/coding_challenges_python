import sys

from abc import abstractmethod, ABC
from typing import List


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
        self._min_index = None
        self._iterators = iterators

    def has_next(self) -> bool:
        for iterator in self._iterators:
            if iterator.has_next():
                return True

        return False

    def next(self) -> int:
        return self._iterators[self._find_min()].next()

    def peek(self) -> int:
        if not self.has_next():
            raise IndexError("Iterator is empty")

        if self._min_index is not None:
            return self._iterators[self._min_index].peek()
        else:
            return self._iterators[self._find_min()].peek()

    def _find_min(self) -> int:
        """
        Loop through all iterators and return the minimum elements.

        :raise IndexError: if iteration has no more elements.
        :return: The index of the minimum element in the list of Iterators.
        """
        index, minimum = None, sys.maxsize

        # Don't call ``self.has_next()`` before because we're looping the iterators just below, so we'll get the info
        # about at that time.
        for i, iterator in enumerate(self._iterators):
            if iterator.has_next() and iterator.peek() <= minimum:
                minimum, index = iterator.peek(), i

        if index is None:
            raise IndexError("Iterator is empty")

        self._min_index = index
        return self._min_index
