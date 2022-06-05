from __future__ import annotations

from typing import List


class SinglyListNode:
    def __init__(self, value=None, next_node: SinglyListNode = None):
        self.value = value
        self.next_node = next_node

    @staticmethod
    def from_list(ll: List):
        head = SinglyListNode()
        for elem in ll:
            head.next_node = SinglyListNode(elem)
        return head.next_node

    def __eq__(self, other: SinglyListNode):
        if isinstance(other, SinglyListNode):
            return self.value == other.value and self.next_node == other.next_node
        return False


class DoublyListNode:
    def __init__(self, value=None, prev_node: DoublyListNode = None, next_node: DoublyListNode = None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    @staticmethod
    def remove_node(old_node: DoublyListNode) -> None:
        old_node.prev_node.next_node = old_node.next_node
        old_node.next_node.prev_node = old_node.prev_node

        old_node.prev_node = old_node.next_node = None
