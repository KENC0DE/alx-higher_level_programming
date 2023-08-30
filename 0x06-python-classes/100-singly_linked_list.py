#!/usr/bin/python3
""" Node Class """


class Node:
    """ Initializer """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Singly Linked list class"""


class SinglyLinkedList:
    """ Initializer """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        nw = Node(value)
        if self.__head is None:
            nw.next_node = None
            self.__head = nw
        elif self.__head.data > value:
            nw.next_node = self.__head
            self.__head = nw
        else:
            tp = self.__head
            while tp.next_node:
                if value < tp.next_node.data:
                    break
                tp = tp.next_node

            nw.next_node = tp.next_node
            tp.next_node = nw

    def __str__(self):
        tp = self.__head
        inf = []
        while tp:
            inf.append(str(tp.data))
            tp = tp.next_node

        return ("\n".join(inf))
