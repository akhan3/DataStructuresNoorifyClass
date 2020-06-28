class Node(object):
    def __init__(self, data=None, next=None):
        super(Node, self).__init__()
        self.data = data
        self.next = next

    def __str__(self):
        return "{} -> {}".format(self.data, self.next)


class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self.head = None

    def size(self):
        print("Complete the implementation")

    def find(self, data):
        print("Complete the implementation")

    def update(self, data, new_data):
        print("Complete the implementation")

    def push_front(self, data):
        print("Complete the implementation")

    def pop_front(self):
        print("Complete the implementation")

    def top_front(self):
        print("Complete the implementation")

    def push_back(self, data):
        print("Complete the implementation")

    def pop_back(self):
        print("Complete the implementation")

    def top_back(self):
        print("Complete the implementation")

    def remove(self, data):
        print("Complete the implementation")

    def _reverse_iterative(self):
        print("Complete the implementation")

    def reverse(self, method="recurrsive"):
        if method == "iterative":
            return self._reverse_iterative()
        else:
            self._reverse_recurrsive(None, self.head)
            return self.head

    def _reverse_recurrsive(self, prev, curr):
        print("Complete the implementation")

    def __str__(self):
        result = "\n*** LinkedList ***\n"
        node = self.head
        while node:
            result += "{} -> ".format(node)
            node = node.next

        result += "None"

        return result
