class Node:
    """ A class to represent a node in a singly linked list
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "({}, {})".format(self.data, hex(id(self.next)))


class LinkedList:
    """ A class to represent a singly linked list
    """

    def __init__(self, iterable=None):
        """ Overloaded constructor
        """
        self.clear()  # start as blank
        try:
            for item in iterable:
                self.append(item)
        except TypeError:  # if not iterable
            if isinstance(iterable, Node):  # check if it's a Node
                self.head = iterable
                self.size = self._getsize()

    def __getitem__(self, key):
        """ Overloaded index operator []
        """
        node = self.head
        try:
            data = node.data
            for k in range(key):
                node = node.next
                data = node.data
            return data
        except AttributeError:
            raise IndexError("index out of range")

    def _getsize(self):
        """ Calculate size by traversing the list
        """
        n = 0
        node = self.head
        while node:
            node = node.next
            n += 1
        return n

    def clear(self):
        """ Clear the list
        """
        self.head = None
        self.size = 0

    def isempty(self):
        """ Check if the list is empty
        """
        return self.size == 0

    def appendleft(self, data):
        """ Append a node at the end of the list
        """
        n1 = Node(data, self.head)
        self.head = n1
        self.size += 1

    def append(self, data):
        node = self.head
        try:
            while node.next is not None:
                node = node.next
            n1 = Node(data)
            node.next = n1
            self.size += 1
        except AttributeError:  # if list is empty
            self.appendleft(data)

    def _gotoNextToLastNode(self):
        node = self.head
        while node.next.next is not None:
            node = node.next
        return node

    def pop(self):
        if self.size == 0:
            raise IndexError("index out of range")
        elif self.size == 1:
            data = self.head.data
            self.clear()
            return data
        else:
            n1 = self._gotoNextToLastNode()
            data = n1.next.data
            n1.next = None
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
