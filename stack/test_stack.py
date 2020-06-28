import unittest
from stack import Stack


class StackTests(unittest.TestCase):
    def test_push_when_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act
        stack.push("Umair")

        # Assert
        self.assertEqual("Umair", stack.pop())

    def test_push_when_non_empty_stack(self):
        # Arrange
        stack = Stack()
        stack.push("Umair")

        # Act
        stack.push("Aamir")

        # Assert
        self.assertEqual("Aamir", stack.pop())

    def test_pop_when_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act
        # Assert
        self.assertRaises(ValueError, stack.pop)

    def test_pop_when_non_empty_stack(self):
        # Arrange
        stack = Stack()
        stack.push("Umair")
        stack.push("Aamir")
        stack.push("Usman")

        # Act
        # Assert
        self.assertEqual("Usman", stack.pop())

    def test_top_when_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act
        # Assert
        self.assertRaises(ValueError, stack.top)

    def test_top_when_non_empty_stack(self):
        # Arrange
        stack = Stack()
        stack.push("Umair")
        stack.push("Aamir")
        stack.push("Usman")

        # Act
        # Assert
        self.assertEqual("Usman", stack.top())

    def test_size_when_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act
        # Assert
        self.assertEqual(0, stack.size())

    def test_size_when_non_empty_stack(self):
        # Arrange
        stack = Stack()
        stack.push("Umair")

        # Act
        # Assert
        self.assertEqual(1, stack.size())

    def test_isEmpty_when_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act
        # Assert
        self.assertTrue(stack.isEmpty())

    def test_isEmpty_when_non_empty_stack(self):
        # Arrange
        stack = Stack()
        stack.push("Umair")

        # Act
        # Assert
        self.assertFalse(stack.isEmpty())
