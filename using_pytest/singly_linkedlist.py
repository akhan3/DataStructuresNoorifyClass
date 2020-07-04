""" This module contains class definitions for a singly linked list
"""


class SinglyNode:
    """ A class to represent a node in a singly linked list
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "({}, {})".format(self.data, hex(id(self.next)))


class SinglyLinkedList:
    """ A class to represent a singly linked list
    """

    def __init__(self, iterable=None):
        """ Overloaded constructor
        """
        self.head = None
        self.size = 0
        try:
            for item in iterable:
                self.append(item)
        except TypeError:  # if not iterable
            if isinstance(iterable, SinglyNode):  # check if it's a node
                self.head = iterable
                self.size = self._count_nodes()

    def __getitem__(self, key):
        """ Overloaded index operator []
        """
        node = self.head
        try:
            data = node.data
            for _ in range(key):
                node = node.next
                data = node.data
            return data
        except AttributeError:
            raise IndexError("index out of range")

    def _count_nodes(self):
        """ Count nodes in the list by traversing it in full.
            This method is only ever called in the constructor to get the size
            if the list was initialized from a subset of an existing list.
            From there onwards, ".size" is maintained through book-keeping without
            ever a need to call this method.
        """
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        return count

    def clear(self):
        """ Clear the list
        """
        self.__init__()

    def isempty(self):
        """ Check if the list is empty
        """
        return self.size == 0

    def appendleft(self, data):
        """ Append a node at the beginning of the list
        """
        self.head = SinglyNode(data, self.head)
        self.size += 1

    def append(self, data):
        """ Append a node at the end of the list
        """
        node = self.head
        try:
            while node.next is not None:
                node = node.next
            node.next = SinglyNode(data)
            self.size += 1
        except AttributeError:  # if list is empty
            self.appendleft(data)

    def _goto_next_to_last_node(self):
        """ Traverse to second to the last node in the list
        """
        try:
            node = self.head
            while node.next.next is not None:
                node = node.next
            return node
        except AttributeError:
            raise IndexError("index out of range")

    def pop(self):
        if self.size == 0:
            raise IndexError("index out of range")
        elif self.size == 1:
            data = self.head.data
            self.clear()
            return data
        else:
            node = self._goto_next_to_last_node()
            data = node.next.data
            node.next = None
            self.size -= 1
            return data

    def popleft(self):
        if self.size == 0:
            raise IndexError("index out of range")
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def __repr__(self):
        result = "*** LinkedList (size = {}) ***\t".format(self.size)
        node = self.head
        while node:
            result += "{} -> ".format(node.data)
            node = node.next
        return result


# def main():
#     mylist = LinkedList()
#     print(mylist)

#     mylist.append(3)
#     print(mylist)

#     mylist.append(34)
#     print(mylist)

#     mylist.append(35)
#     print(mylist)

#     for k in range(5):
#         mylist.append(k + 100)

#     print(mylist)


# if __name__ == "__main__":
#     main()
