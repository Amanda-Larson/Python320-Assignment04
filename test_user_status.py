"""
# Title: test_user_status
# Purpose: to test user_status.py
# Who: ALarson
# What/When: 4/24/2022 - started assignment
#
"""
from unittest import TestCase
from mock import MagicMock
import user_status as us


# This tests if an object was instantiated...it works but is not the correct test
# class TestUserStatus(TestCase):
#     @mock.patch("user_status.UserStatus")
#     def test_user_status_called(self, mock_user_status):
#     mock_user_status.assert_called_with()


class TestUserStatusCollection(TestCase):
    """This class will test methods in UserStatusCollection class"""

    def setUp(self) -> None:
        status_id = 345
        user_id = 321
        status_test = "Hello world"

        self.add_status = us.UserStatusCollection().add_status(status_id, user_id, status_test)
        self.mod_status = us.UserStatusCollection().modify_status(status_id, user_id, status_test)
        self.del_status = us.UserStatusCollection().delete_status(status_id)
        self.search_status = us.UserStatusCollection().search_status(status_id)

        self.test_user_status = us.UserStatus(status_id, user_id, status_test)

    def test_user_status_collection(self):
        """This will test that the UserStatusCollection class creates an empty dict"""
        expected = {}
        self.assertEqual(expected, us.UserStatusCollection().database)

    def test_add_status(self):
        """This will test UserStatusCollection.add_status"""
        status_id = 203
        user_id = 222
        status_text = "Good night!"
        # I think this tests that if add_status is True, the database is not empty
        # If add_status is False, it would not add a status and may be empty
        if us.UserStatusCollection().add_status(status_id, user_id, status_text):
            self.assertIsNotNone(us.UserStatusCollection().database)

    def test_add_status_again(self):
        """Another test for add status"""
        self.add_status = MagicMock(return_value='user1')
        status_id = 203
        user_id = 222
        status_text = "Good night!"

        self.add_status(status_id, user_id, status_text)

        self.add_status.assert_called_with(status_id, user_id, status_text)

    def test_mod_status(self):
        """Testing modify status module"""
        self.mod_status = MagicMock()
        # tried putting nothing in magic mock
        status_id = 203
        user_id = 222
        status_text = "Good night!"

        self.mod_status(status_id, user_id, status_text)

        self.mod_status.assert_called_with(status_id, user_id, status_text)

    def test_del_status(self):
        """Testing deleting a status"""
        self.del_status = MagicMock()
        # again, don't really need anything in MagicMock()
        status_id = 456
        self.del_status(status_id)
        self.del_status.assert_called_with(status_id)

    def test_search_status(self):
        """Testing the search status method"""
        self.search_status = MagicMock()
        # tried putting the status id as an integer right in the assert statement - this works too
        status_id = 999
        self.search_status(status_id)
        self.search_status.assert_called_with(999)
