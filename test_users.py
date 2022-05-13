"""
# ------
# What/When: Started testing, 4/24/2022
# Name: ALarson
# Title: test_users.py
# ------
"""

from unittest import TestCase
from unittest.mock import MagicMock
from users import Users
from users import UserCollection


class TestUsers(TestCase):
    """Testing Users"""

    def setUp(self) -> None:
        user_id = 202
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'

        # test_user = UserCollection().database

        self.add_user = UserCollection().add_user(user_id, email, user_name, user_last_name)
        self.mod_user = UserCollection().modify_user(user_id, email, user_name, user_last_name)
        self.del_name = UserCollection().delete_user(user_id)
        self.search_user = UserCollection().search_user(user_id)

        self.test_user = Users(self.add_user, self.mod_user, self.del_name, self.search_user)
        # test_user.append(self.test_user)

    def test_user_collection(self):
        """Testing User Collection"""
        expected = {}
        self.assertEqual(expected, UserCollection().database)

    def test_add_user_call(self):
        """Testing Add User"""
        self.add_user = MagicMock(return_value='user1')
        # not sure what the point of return_value is for this
        user_id = 202
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'

        self.add_user(user_id, email, user_name, user_last_name)

        self.add_user.assert_called_with(user_id, email, user_name, user_last_name)

    def test_modify_user_call(self):
        """Testing modify user call"""
        self.mod_user = MagicMock(return_value='user1')
        # not sure what the point of return_value is for this

        user_id = 202
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'

        self.mod_user(user_id, email, user_name, user_last_name)

        self.mod_user.assert_called_with(user_id, email, user_name, user_last_name)

    def test_delete_user_call(self):
        """Testing delete user call"""
        self.del_name = MagicMock(return_value='user1')
        # not sure what the point of return_value is for this
        user_id = 202
        self.del_name(user_id)
        # I'm not sure that asserting it was called when I just called it
        # counts as a test or what it proves, but here it is...
        self.del_name.assert_called()

    def test_search_user(self):
        """Testing the search user was called"""
        self.search_user = MagicMock()
        user_id = 202
        self.search_user(user_id)

        self.search_user.assert_called()
