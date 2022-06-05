from __future__ import annotations


class SinglyListNode:
    def __init__(self, value=None, next_node: SinglyListNode = None):
        self.value = value
        self.next_node = next_node

    @staticmethod
    def from_list(ll: list):
        head = SinglyListNode()
        current = head

        for value in ll:
            current.next_node = SinglyListNode(value)
            current = current.next_node

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
    def from_list(ll: list):
        head = DoublyListNode()
        current = head

        for value in ll:
            current.next_node = DoublyListNode(value)
            if current.next_node.prev_node != head:
                current.next_node.prev_node = current
            current = current.next_node

        return head.next_node

    @staticmethod
    def insert_node(prev_node: DoublyListNode, new_node: DoublyListNode) -> DoublyListNode:
        if prev_node.next_node:
            prev_node.next_node.prev_node = new_node
        new_node.next_node = prev_node.next_node

        new_node.prev_node = prev_node
        prev_node.next_node = new_node

        return new_node

    @staticmethod
    def remove_node(old_node: DoublyListNode) -> None:
        old_node.prev_node.next_node = old_node.next_node
        old_node.next_node.prev_node = old_node.prev_node

        old_node.prev_node = old_node.next_node = None
