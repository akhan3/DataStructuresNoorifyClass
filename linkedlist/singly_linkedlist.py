class Node(object):
    def __init__(self, data=None, next=None):
        super(Node, self).__init__()
        self.data = data
        self.next = next

    def __str__(self):
        return "0x{:x}:[{}|0x{:x}]".format(id(self), self.data, id(self.next))


class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None
        self._size = 0

    def clear(self):
        """ Clear the list
        """
        self.__init__()

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

    def size(self):
        return self._size

    def find(self, data):
        """ Find the first occurence of an item in the list
        """
        if self._size == 0:
            raise ValueError("cannot find in an empty list")
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        raise ValueError("item not found")

    def update(self, data, new_data):
        """ Update the first occurence of an item in the list
        """
        if self._size == 0:
            raise ValueError("cannot update in an empty list")
        node = self.head
        while node is not None:
            if node.data == data:
                node.data = new_data
                return True
            node = node.next
        raise ValueError("item not found")

    def push_front(self, data):
        """ Append a node at the beginning of the list
        """
        self.head = Node(data, self.head)
        self._size += 1
        return True

    def pop_front(self):
        data = self.top_front()
        self.head = self.head.next
        self._size -= 1
        return data

    def top_front(self):
        if self._size == 0:
            raise ValueError("cannot pop from an empty list")
        else:
            data = self.head.data
            return data

    def push_back(self, data):
        """ Append a node at the end of the list
        """
        node = self.head
        try:
            while node.next is not None:
                node = node.next
            node.next = Node(data)
            self._size += 1
        except AttributeError:  # if list is empty
            self.push_front(data)
        return True

    # TODO: Refactor top_back and pop_back
    def pop_back(self):
        if self._size == 0:
            raise ValueError("cannot pop from an empty list")
        elif self._size == 1:
            data = self.head.data
            self.clear()
            return data
        else:
            node = self._goto_next_to_last_node()
            data = node.next.data
            node.next = None
            self._size -= 1
            return data

    def top_back(self):
        if self._size == 0:
            raise ValueError("cannot pop from an empty list")
        elif self._size == 1:
            data = self.head.data
            # self.clear()
            return data
        else:
            node = self._goto_next_to_last_node()
            data = node.next.data
            # node.next = None
            # self._size -= 1
            return data

    def remove(self, data):
        """ Remove the first occurence of an item in the list
        """
        if self._size == 0:
            raise ValueError("cannot remove in an empty list")
        node = self.head
        node_prev = None
        while node is not None:
            if node.data == data:
                if node == self.head:  # if head node
                    self.pop_front()
                elif node.next == None:  # if tail node
                    self.pop_back()
                else:  # if somewhere in the middle
                    node_prev.next = node.next
                    self._size -= 1
                return True
            node_prev = node
            node = node.next
        raise ValueError("item not found")

    # TODO: Refactor below
    def _reverse_iterative(self):
        """ Reverse a linked list in-place (iterative method)
        """
        if self._size == 0:
            return
        elif self._size == 1:
            return
        node = self.head.next  # start from 2nd node
        orig_prev_node = self.head
        orig_prev_node.next = None  # turn original head into tail
        while node is not None:
            orig_next_node = node.next
            node.next = orig_prev_node
            orig_prev_node = node
            node = orig_next_node
        self.head = orig_prev_node  # assign the new head

    # def reverse(self, method="recurrsive"):
    def reverse(self, method="iterative"):
        if method == "iterative":
            return self._reverse_iterative()
        else:
            self._reverse_recurrsive(None, self.head)
            return self.head

    def _reverse_recurrsive(self, prev, curr):
        print("Complete the implementation")

    def __str__too_long(self):
        result = "\n*** LinkedList ***\n"
        node = self.head
        while node:
            result += "{} -> ".format(node)
            node = node.next

        result += "None"

        return result

    def __repr__(self):
        result = "*** LinkedList (size = {}) ***\t".format(self._size)
        node = self.head
        while node:
            result += "{} -> ".format(node.data)
            node = node.next
        return result
