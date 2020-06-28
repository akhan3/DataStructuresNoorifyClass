import unittest
from singly_linkedlist import LinkedList


class LinkedListTests(unittest.TestCase):
    def test_size_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act
        size = linkedlist.size()

        # Assert
        self.assertEqual(0, size)

    def test_size_when_single_item_linkedlist(self):
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        size = linkedlist.size()

        # Assert
        self.assertEqual(1, size)

    def test_size_when_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        size = linkedlist.size()

        # Assert
        self.assertEqual(2, size)

    def test_size_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Maria")
        linkedlist.push_back("Umair")
        linkedlist.push_back("Usman")

        # Act
        size = linkedlist.size()

        # Assert
        self.assertEqual(4, size)

    def test_find_when_empty_linked_list(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.find, "Umair")

    def test_find_when_when_non_empty_linked_list_and_item_is_present(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        found = linkedlist.find("Umair")

        # Assert
        self.assertTrue(found)
        self.assertEqual("Umair", found.data)

    def test_find_when_when_non_empty_linked_list_and_item_is_not_present(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.find, "Usman")

    def test_update_when_empty_linked_list(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.update, "Umair", "Usman")

    def test_update_when_when_non_empty_linked_list_and_item_is_present(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        updated = linkedlist.update("Umair", "Usman")

        # Assert
        self.assertTrue(updated)
        self.assertTrue(linkedlist.find("Usman"))

    def test_update_when_when_non_empty_linked_list_and_item_is_not_present(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.update, "Usman", "Aamir")

    def test_push_front_when_empty_linked_list(self):
        # Arrange
        linkedlist = LinkedList()

        # Act
        pushed = linkedlist.push_front("Umair")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 1)
        self.assertTrue(linkedlist.find("Umair"))

    def test_push_front_when_single_item_linked_list(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_front("Umair")

        # Act
        pushed = linkedlist.push_front("Aamir")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 2)
        self.assertTrue(linkedlist.head.data == "Aamir")

    def test_push_front_when_more_than_one_items_linked_list(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_front("Umair")
        linkedlist.push_front("Aamir")

        # Act
        pushed = linkedlist.push_front("Rayan")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 3)
        self.assertTrue(linkedlist.head.data == "Rayan")

    def test_push_front_when_more_than_two_items_linked_list(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_front("Umair")
        linkedlist.push_front("Aamir")
        linkedlist.push_front("Usman")

        # Act
        pushed = linkedlist.push_front("Rayan")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 4)
        self.assertTrue(linkedlist.head.data == "Rayan")

    def test_pop_front_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.pop_front)

    def test_pop_front_when_single_item_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        linkedlist.pop_front()

        # Assert
        self.assertTrue(linkedlist.size() == 0)
        self.assertRaises(ValueError, linkedlist.find, "Umair")

    def test_pop_front_when_more_than_one_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        linkedlist.pop_front()

        # Assert
        self.assertTrue(linkedlist.size() == 1)
        self.assertRaises(ValueError, linkedlist.find, "Umair")
        self.assertEqual(linkedlist.head.data, "Aamir")

    def test_pop_front_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        linkedlist.pop_front()

        # Assert
        self.assertTrue(linkedlist.size() == 2)
        self.assertRaises(ValueError, linkedlist.find, "Umair")
        self.assertEqual(linkedlist.head.data, "Aamir")

    def test_top_front_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.top_front)

    def test_top_front_when_single_item_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        front = linkedlist.top_front()

        # Assert
        self.assertTrue(linkedlist.size() == 1)
        self.assertEqual(front, "Umair")

    def test_top_front_when_more_than_one_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        front = linkedlist.top_front()

        # Assert
        self.assertTrue(linkedlist.size() == 2)
        self.assertEqual(front, "Umair")

    def test_top_front_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        front = linkedlist.top_front()

        # Assert
        self.assertTrue(linkedlist.size() == 3)
        self.assertEqual(front, "Umair")

    def test_push_back_when_empty_linked_list(self):
        # Arrange
        linkedlist = LinkedList()

        # Act
        pushed = linkedlist.push_back("Umair")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 1)
        self.assertTrue(linkedlist.find("Umair"))

    def test_push_back_when_single_item_linked_list(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        pushed = linkedlist.push_back("Aamir")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 2)
        self.assertTrue(linkedlist.find("Aamir"))

    def test_push_back_when_more_than_two_items_linked_list(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Usman")
        linkedlist.push_back("Rayan")

        # Act
        pushed = linkedlist.push_back("Aamir")

        # Assert
        self.assertTrue(pushed)
        self.assertTrue(linkedlist.size() == 4)
        self.assertTrue(linkedlist.find("Aamir"))

    def test_pop_back_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.pop_back)
        self.assertTrue(linkedlist.size() == 0)

    def test_pop_back_when_single_item_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        linkedlist.pop_back()

        # Assert
        self.assertTrue(linkedlist.size() == 0)
        self.assertRaises(ValueError, linkedlist.find, "Umair")

    def test_pop_back_when_more_than_one_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        linkedlist.pop_back()

        # Assert
        self.assertTrue(linkedlist.size() == 1)
        self.assertRaises(ValueError, linkedlist.find, "Aamir")

    def test_pop_back_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        linkedlist.pop_back()

        # Assert
        self.assertTrue(linkedlist.size() == 2)
        self.assertRaises(ValueError, linkedlist.find, "Usman")

    def test_top_back_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.top_back)

    def test_top_back_when_single_item_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        topped = linkedlist.top_back()

        # Assert
        self.assertTrue(linkedlist.size() == 1)
        self.assertEqual(topped, "Umair")

    def test_top_back_when_more_than_one_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        topped = linkedlist.top_back()

        # Assert
        self.assertTrue(linkedlist.size() == 2)
        self.assertEqual(topped, "Aamir")

    def test_top_back_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        topped = linkedlist.top_back()

        # Assert
        self.assertTrue(linkedlist.size() == 3)
        self.assertEqual(topped, "Usman")

    def test_remove_when_empty_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.remove, "Umair")
        self.assertTrue(linkedlist.size() == 0)

    def test_remove_when_item_is_present_and_head_item_is_removed_when_linkedlist_is_only_one_item(
        self
    ):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        removed = linkedlist.remove("Umair")

        # Assert
        self.assertTrue(removed)
        self.assertRaises(ValueError, linkedlist.find, "Umair")
        self.assertTrue(linkedlist.size() == 0)

    def test_remove_when_item_is_present_and_head_item_is_removed_when_linkedlist_is_more_than_one_item(
        self
    ):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        removed = linkedlist.remove("Umair")

        # Assert
        self.assertTrue(removed)
        self.assertRaises(ValueError, linkedlist.find, "Umair")
        self.assertTrue(linkedlist.size() == 2)

    def test_remove_when_item_is_present_and_non_head_middle_item_is_removed_when_list_is_more_than_one_item(
        self
    ):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        removed = linkedlist.remove("Aamir")

        # Assert
        self.assertTrue(removed)
        self.assertRaises(ValueError, linkedlist.find, "Aamir")
        self.assertTrue(linkedlist.size() == 2)

    def test_remove_when_item_is_present_and_non_head_last_item_is_removed_when_linkedlist_is_more_than_one_item(
        self
    ):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        removed = linkedlist.remove("Usman")

        # Assert
        self.assertTrue(removed)
        self.assertRaises(ValueError, linkedlist.find, "Usman")
        self.assertTrue(linkedlist.size() == 2)

    def test_remove_when_item_is_not_present_when_linkedlist_is_more_than_one_item(
        self
    ):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act & Assert
        self.assertRaises(ValueError, linkedlist.remove, "Maria")
        self.assertTrue(linkedlist.size() == 3)

    def test_reverse_when_linkedlist_is_empty(self):
        # Arrange
        linkedlist = LinkedList()

        # Act
        linkedlist.reverse()

        # Assert
        self.assertFalse(linkedlist.head)

    def test_reverse_when_single_item_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")

        # Act
        linkedlist.reverse()

        # Assert
        self.assertTrue(linkedlist.head and linkedlist.head.data == "Umair")

    def test_reverse_when_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")

        # Act
        linkedlist.reverse()

        # Assert
        self.assertTrue(linkedlist.head and linkedlist.head.data == "Aamir")

    def test_reverse_when_more_than_two_items_linkedlist(self):
        # Arrange
        linkedlist = LinkedList()
        linkedlist.push_back("Umair")
        linkedlist.push_back("Aamir")
        linkedlist.push_back("Usman")

        # Act
        linkedlist.reverse()

        # Assert
        self.assertTrue(linkedlist.head and linkedlist.head.data == "Usman")
