# Instructions to run these tests
#   $ pytest-3 -l
#   $ python3-coverage run -m pytest -l
#   $ python3-coverage html
#   $ xdg-open htmlcov/index.html


import pytest
from math import pi
from ll import Node, LinkedList


def test_node_constructor():
    assert Node().data == None
    assert Node().next == None
    assert Node(None).data == None
    assert Node(None).next == None
    assert Node(pi).data == pi
    assert Node(pi).next == None
    assert Node("Hello").data == "Hello"
    assert Node("Hello").next == None


def test_list_constructor():
    assert LinkedList().size == 0
    assert LinkedList(None).size == 0
    assert LinkedList([]).size == 0
    assert LinkedList([5]).size == 1
    assert LinkedList("Hello").size == len("Hello")
    assert LinkedList(range(10)).size == 10
    assert LinkedList({"Hello", 5, 6, 7, 5}).size == 4


def test_isempty():
    assert LinkedList().isempty()
    assert LinkedList(None).isempty()
    assert LinkedList([]).isempty()
    assert not LinkedList([5]).isempty()
    assert not LinkedList("Hello").isempty()
    assert not LinkedList(range(10)).isempty()
    l = LinkedList({"Hello", 5, 6, 7, 5})
    assert not l.isempty()
    l.clear()
    assert l.isempty()


def test_size_when_created_from_iterable():
    N = 8
    l = LinkedList(range(N))
    assert l.size == N


def test_size_when_created_from_iterable_string():
    seed = "Hello World!"
    l = LinkedList(seed)
    assert l.size == len(seed)


def test_size_when_created_from_middle_node_of_existing_linkedlist():
    N = 8
    l = LinkedList(range(N))
    l2 = LinkedList(l.head.next.next)
    assert l2.size == N - 2
    assert l2.head.data == 2


def test_size_when_created_from_node():
    node = Node("Hello")
    l = LinkedList(node)
    assert l.size == 1
    assert l.head is node


def test_size_when_empty():
    l = LinkedList()
    assert l.head is None
    assert l.size == 0
    assert l.isempty()


def test_size_when_cleared():
    N = 23
    l = LinkedList(range(N))
    l.clear()
    assert l.head is None
    assert l.size == 0
    assert l.isempty()


def test_size():
    for k in range(7):
        l = LinkedList(range(k))
        assert l.size == k


def test_pop_when_empty():
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_pop_when_1():
    x = pi
    l = LinkedList([x])
    assert l.pop() == x
    assert l.head is None
    assert l.size == 0
    assert l.isempty()


def test_pop():
    for k in range(2, 7):
        l = LinkedList(range(k))
        head = l.head
        assert l.pop() == k - 1
        assert l.size == k - 1
        assert head == l.head


def test_indexing_when_empty():
    l = LinkedList()
    with pytest.raises(IndexError):
        l[0]
    with pytest.raises(IndexError):
        l[100]


def test_indexing():
    N = 4
    x = list(range(100, 100 + N + 1))
    l = LinkedList(x)
    for k in range(len(x)):
        assert l[k] == x[k]
    with pytest.raises(IndexError):
        l[N + 100]


def test_popleft_when_empty():
    l = LinkedList()
    with pytest.raises(IndexError):
        l.popleft()


def test_popleft_when_1():
    x = pi
    l = LinkedList([x])
    assert l.popleft() == x
    assert l.head is None
    assert l.size == 0
    assert l.isempty()


def test_popleft():
    for k in range(2, 7):
        l = LinkedList(range(k))
        curr_data = l.head.data
        next_head = l.head.next
        assert l.popleft() == curr_data
        assert l.size == k - 1
        assert l.head == next_head
