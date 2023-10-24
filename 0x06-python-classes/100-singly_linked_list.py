#!/usr/bin/python3
"""classes of singly-linked list to be defined"""


class Node:
    """represents node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """New node is initiated.
        Args:
            data integer: data of a Node.
            next_node (Node): Next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data of a node is set."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next node of the the Node is set."""
        return (self.__next_node)
