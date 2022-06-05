from typing import Dict, Set

from data_structures import DoublyListNode


class CustomerLogger:
    """
    On some company’s ecommerce website, customers go shopping and hopefully buy something.

    When they don’t log into the website for a long time, we want to email them with some promotion, so they’d come
    again.

    The requirement is to implement these two functions:
      * ``log_customer()`` to track whenever a customer logs into the website,
      * ``get_oldest_customer_for_email()`` to return the customer ID:

        * That hasn't logged in for the longest time, **AND**
        * Has logged in once and only once, **AND**
        * To whom we never emailed (we don’t want to spam them).

    Example of sequential calls:

    >>> logger = CustomerLogger()
    >>> logger.log_customer('1')
    >>> logger.log_customer('2')
    >>> logger.log_customer('4')
    >>> logger.log_customer('2')
    >>> logger.log_customer('5')
    >>> logger.get_oldest_customer_for_email()
    '1'
    >>> logger.get_oldest_customer_for_email()
    '4'
    >>> logger.get_oldest_customer_for_email()
    '5'
    """

    def __init__(self):
        self._head = DoublyListNode()
        self._tail = DoublyListNode()
        self._hashmap: Dict[str, DoublyListNode] = {}
        self._emailed_or_seen: Set[str] = set()

        self._head.next_node = self._tail
        self._tail.prev_node = self._head

    def log_customer(self, customer_id: str) -> None:
        if customer_id in self._emailed_or_seen:
            return
        elif customer_id in self._hashmap:
            self._emailed_or_seen.add(customer_id)
            DoublyListNode.remove_node(self._hashmap[customer_id])
            self._hashmap.pop(customer_id, None)
        else:
            self._hashmap[customer_id] = self._insert_tail(DoublyListNode(customer_id))

    def get_oldest_customer_for_email(self) -> str:
        if self._head.next_node == self._tail:
            return 'N/A'

        customer_id = self._head.next_node.value

        self._emailed_or_seen.add(customer_id)
        DoublyListNode.remove_node(self._head.next_node)
        self._hashmap.pop(customer_id, None)

        return customer_id

    def _insert_tail(self, new_node: DoublyListNode) -> DoublyListNode:
        new_node.prev_node = self._tail.prev_node
        new_node.prev_node.next_node = new_node

        self._tail.prev_node = new_node
        new_node.next_node = self._tail

        return new_node
