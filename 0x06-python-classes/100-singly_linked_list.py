#!/usr/bin/python3
class Node:
    """ Class to each node of a Singly linked list
    """

    def __init__(self, data, next_node=None):
        """ Class constructor

        Args:
            data (int): Payload
            next_node (object Node): Porter to the next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Class getter for data

        Returns:
            data (int): The payload node
        """
        return self.__data

    @data.setter
    def data(self, data):
        """ Class setter for data
        """
        if not type(data) is int:
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        """ Class getter for next_node

        Returns:
            next_node (Object): The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """ Class setter for next_node
        """
        if (not type(next_node) is Node) and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """ Class to support the Singly linked list
    """

    def __init__(self):
        """ Class constructor
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Ordered inserting method

        Args:
            value (int): The payload for the node
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
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ Formating list of date for print
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
