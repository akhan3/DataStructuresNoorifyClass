import unittest
from queue import Queue


class QueueTests(unittest.TestCase):
    def test_push_when_empty_queue(self):
        # Arrange
        queue = Queue()

        # Act
        queue.push("Umair")

        # Assert
        self.assertEqual("Umair", queue.pop())

    def test_push_when_non_empty_queue(self):
        # Arrange
        queue = Queue()
        queue.push("Umair")

        # Act
        queue.push("Aamir")

        # Assert
        self.assertEqual("Umair", queue.pop())

    def test_pop_when_empty_queue(self):
        # Arrange
        queue = Queue()

        # Act
        # Assert
        self.assertRaises(ValueError, queue.pop)

    def test_pop_when_non_empty_queue(self):
        # Arrange
        queue = Queue()
        queue.push("Umair")
        queue.push("Aamir")
        queue.push("Usman")

        # Act
        # Assert
        self.assertEqual("Umair", queue.pop())

    def test_top_when_empty_queue(self):
        # Arrange
        queue = Queue()

        # Act
        # Assert
        self.assertRaises(ValueError, queue.top)

    def test_top_when_non_empty_queue(self):
        # Arrange
        queue = Queue()
        queue.push("Umair")
        queue.push("Aamir")
        queue.push("Usman")

        # Act
        # Assert
        self.assertEqual("Umair", queue.top())

    def test_size_when_empty_queue(self):
        # Arrange
        queue = Queue()

        # Act
        size = queue.size()

        # Assert
        self.assertEqual(0, size)

    def test_size_when_non_empty_queue(self):
        # Arrange
        queue = Queue()
        queue.push("Umair")

        # Act
        size = queue.size()

        # Assert
        self.assertEqual(1, size)

    def test_isEmpty_when_empty_queue(self):
        # Arrange
        queue = Queue()

        # Act
        # Assert
        self.assertTrue(queue.isEmpty())

    def test_isEmpty_when_non_empty_queue(self):
        # Arrange
        queue = Queue()
        queue.push("Umair")

        # Act
        # Assert
        self.assertFalse(queue.isEmpty())
