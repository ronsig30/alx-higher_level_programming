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

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents Singly-linked list."""

    def __init__(self):
        """New SinglyLinkedLIst is initialized."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the list.
        Node is inserted to the list at a correct ordered
        numerical position.
        Args:
            value (Node); New node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defining the print() represantation of a List."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
