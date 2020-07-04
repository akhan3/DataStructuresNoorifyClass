""" This module contains test cases for a singly linked list
"""

# Instructions to run these tests
#   $ pytest-3 -l
#   $ python3-coverage run -m pytest -l
#   $ python3-coverage html
#   $ xdg-open htmlcov/index.html
#   $ pylint --good-names=x,k,N *.py


from math import pi
import pytest
from singly_linkedlist import SinglyNode, SinglyLinkedList


def test_node_constructor():
    assert SinglyNode().data is None
    assert SinglyNode().next is None
    assert SinglyNode(None).data is None
    assert SinglyNode(None).next is None
    assert SinglyNode(pi).data == pi
    assert SinglyNode(pi).next is None
    assert SinglyNode("Hello").data == "Hello"
    assert SinglyNode("Hello").next is None


def test_list_constructor():
    assert SinglyLinkedList().size == 0
    assert SinglyLinkedList(None).size == 0
    assert SinglyLinkedList([]).size == 0
    assert SinglyLinkedList([5]).size == 1
    assert SinglyLinkedList("Hello").size == len("Hello")
    assert SinglyLinkedList(range(10)).size == 10
    assert SinglyLinkedList({"Hello", 5, 6, 7, 5}).size == 4


def test_isempty():
    assert SinglyLinkedList().isempty()
    assert SinglyLinkedList(None).isempty()
    assert SinglyLinkedList([]).isempty()
    assert not SinglyLinkedList([5]).isempty()
    assert not SinglyLinkedList("Hello").isempty()
    assert not SinglyLinkedList(range(10)).isempty()
    lis = SinglyLinkedList({"Hello", 5, 6, 7, 5})
    assert not lis.isempty()
    lis.clear()
    assert lis.isempty()


def test_size_when_created_from_iterable():
    N = 8
    lis = SinglyLinkedList(range(N))
    assert lis.size == N


def test_size_when_created_from_iterable_string():
    seed = "Hello World!"
    lis = SinglyLinkedList(seed)
    assert lis.size == len(seed)


def test_size_when_created_from_middle_node_of_existing_linkedlist():
    N = 8
    lis = SinglyLinkedList(range(N))
    lis2 = SinglyLinkedList(lis.head.next.next)
    assert lis2.size == N - 2
    assert lis2.head.data == 2


def test_size_when_created_from_node():
    node = SinglyNode("Hello")
    lis = SinglyLinkedList(node)
    assert lis.size == 1
    assert lis.head is node


def test_size_when_empty():
    lis = SinglyLinkedList()
    assert lis.head is None
    assert lis.size == 0
    assert lis.isempty()


def test_size_when_cleared():
    N = 23
    lis = SinglyLinkedList(range(N))
    lis.clear()
    assert lis.head is None
    assert lis.size == 0
    assert lis.isempty()


def test_size():
    for k in range(7):
        lis = SinglyLinkedList(range(k))
        assert lis.size == k


def test_pop_when_empty():
    lis = SinglyLinkedList()
    with pytest.raises(IndexError):
        lis.pop()


def test_pop_when_1():
    x = pi
    lis = SinglyLinkedList([x])
    assert lis.pop() == x
    assert lis.head is None
    assert lis.size == 0
    assert lis.isempty()


def test_pop():
    for k in range(2, 7):
        lis = SinglyLinkedList(range(k))
        head = lis.head
        assert lis.pop() == k - 1
        assert lis.size == k - 1
        assert head == lis.head


def test__goto_next_to_last_node_when_empty():
    lis = SinglyLinkedList()
    with pytest.raises(IndexError):
        lis._goto_next_to_last_node()


def test__goto_next_to_last_node_when_1():
    x = pi
    lis = SinglyLinkedList([x])
    with pytest.raises(IndexError):
        lis._goto_next_to_last_node()


def test__goto_next_to_last_node():
    for k in range(2, 7):
        lis = SinglyLinkedList(range(k))
        assert lis._goto_next_to_last_node().data == k - 2


def test_indexing_when_empty():
    lis = SinglyLinkedList()
    with pytest.raises(IndexError):
        _ = lis[0]
    with pytest.raises(IndexError):
        _ = lis[100]


def test_indexing():
    N = 4
    x = list(range(100, 100 + N + 1))
    lis = SinglyLinkedList(x)
    for k, val in enumerate(x):
        assert lis[k] == val
    with pytest.raises(IndexError):
        _ = lis[N + 100]


def test_popleft_when_empty():
    lis = SinglyLinkedList()
    with pytest.raises(IndexError):
        lis.popleft()


def test_popleft_when_1():
    x = pi
    lis = SinglyLinkedList([x])
    assert lis.popleft() == x
    assert lis.head is None
    assert lis.size == 0
    assert lis.isempty()


def test_popleft():
    for k in range(2, 7):
        lis = SinglyLinkedList(range(k))
        curr_data = lis.head.data
        next_head = lis.head.next
        assert lis.popleft() == curr_data
        assert lis.size == k - 1
        assert lis.head == next_head
