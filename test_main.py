"""
# Title: test_main.py
# What/When: started main testing 04/23/2022
# ALarson
#
"""

from unittest import TestCase
import main
import users as u
import user_status as us


# main tests
class TestInitUser(TestCase):
    """This will test the user collection __init__ and that it
    creates an empty database/dictionary"""

    def test_init_user_collection(self):
        """This will test the user collection __init__ and that it
        creates an empty database/dictionary
        """
        # test that it was instantiated?
        # expect an instantiated object which has a database/empty dictionary
        expected = {}
        # actual = main.init_user_collection()
        # message = 'test'
        self.assertEqual(expected, main.init_user_collection().database)
        # self.assertIsInstance(expected, actual, message)


class TestInitStatus(TestCase):
    """
    This will test the status collection __init__ and that it creates an
    empty database/dictionary
    """

    def test_init_status_collection(self):
        """This will test the status collection __init__ and that it creates
        an empty database/dictionary"""
        expected = {}
        self.assertEqual(expected, main.init_status_collection().database)


class TestMainUserFunctions(TestCase):
    """This class will test the functions re: users in main.py"""

    def setUp(self) -> None:
        user_id = 225
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'
        filename = 'accounts.csv'

        self.user_db = u.UserCollection().database
        self.load_users = main.load_users(filename, self.user_db)
        self.save_users = main.save_users(filename, self.user_db)
        self.add_user = main.add_user(user_id, email, user_id, user_last_name, self.user_db)
        self.update_user = main.update_user(user_id, email, user_name, user_last_name, self.user_db)
        self.delete_user = main.delete_user(user_id, self.user_db)
        self.search_user = main.search_user(user_id, self.user_db)

    def test_load_users(self):
        """This will test loading users"""

    def test_save_users(self):
        """This will test saving users to file"""

    def test_add_users(self):
        """This will test adding a new user"""
        user_id = 225
        email = 'email@email.com'
        user_name = 'Amanda'
        user_last_name = 'Larson'

        new_user = self.add_user(user_id, email, user_name, user_last_name, self.user_db)
        self.assertIsInstance(new_user, object)

    def test_update_users(self):
        """This will test updating a user"""

    def test_delete_users(self):
        """This will test deleting a user"""

    def test_search_users(self):
        """This will test searching for a user"""

    def tearDown(self) -> None:
        pass


class TestMainStatusFunctions(TestCase):
    """This class will test the functions re: status in main.py"""

    def setUp(self) -> None:
        status_test = 'Good morning, Starshine!'
        user_id = 225
        status_id = 100
        filename = 'status_updates.csv'
        status_db = us.UserStatusCollection().database

        self.load_status_updates = main.load_status_updates(filename, status_db)
        self.save_status_updates = main.save_status_updates(filename, status_db)
        self.add_status = main.add_status(user_id, status_id, status_test, status_db)
        self.update_status = main.update_status(status_id, user_id, status_test, status_db)
        self.delete_status = main.delete_status(status_id, status_db)
        self.search_status = main.search_status(status_id, status_db)

    def test_load_status_updates(self):
        """This will test loading status updates from file"""

    def test_save_status_updates(self):
        """This will test saving status updates to file"""

    def test_add_status(self):
        """This will test adding a status"""

    def test_update_status(self):
        """This will test updating a status"""

    def test_delete_status(self):
        """This will test deleting a status"""

    def test_search_status(self):
        """This will test searching for a status"""
