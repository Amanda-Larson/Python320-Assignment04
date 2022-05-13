"""
Provides a basic frontend
"""
import sys
from loguru import logger
import pysnooper
import main
import users
import user_status

logger.info("Let's get to debugging")
logger.add("out.log", backtrace=True, diagnose=True)


# @pysnooper.snoop(depth=2)
def load_users():
    """
    Loads user accounts from a file
    """
    filename = input('Enter filename of user file: ')
    main.load_users(filename)


# @pysnooper.snoop(depth=2)
def load_status_updates():
    """
    Loads status updates from a file
    """

    filename = input('Enter filename for status file: ')
    print('Loading...')
    main.load_status_updates(filename)


# @pysnooper.snoop()
def add_user():
    """
    Adds a new user into the database
    """
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not users.UserCollection.search_user(user_id=user_id) is None:
        print('Added users must be unique - please try a different user id.')
    elif main.add_user(user_id,
                     email,
                     user_name,
                     user_last_name):
        print("User was successfully added")
    else:
        print("Unknown error")


# @pysnooper.snoop()
def update_user():
    """
    Updates information for an existing user
    """
    user_id = input('User ID: ')
    email_update = input('User email: ')
    user_name_update = input('User name: ')
    user_last_name_update = input('User last name: ')
    try:
        if not main.update_user(user_id, email_update, user_name_update, user_last_name_update):
            print("An error occurred while trying to update user")
        elif users.UserCollection.search_user(user_id=user_id) is None:
            print('This user does not exist yet, please add the user first.')
        else:
            print("User was successfully updated")
    except TypeError:
        logger.exception("NEW EXCEPTION! - Look here!")


# @pysnooper.snoop(depth=2)
def search_user():
    """
    Searches a user in the database
    """
    user_id = input('Enter user ID to search: ')
    result = main.search_user(user_id)
    if not result:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")


# @pysnooper.snoop()
def delete_user():
    """
    Deletes user from the database
    """
    user_id = input('User ID: ')
    if not main.delete_user(user_id):
        print("An error occurred while trying to delete user")
    elif users.UserCollection.search_user(user_id=user_id) is None:
        print('This user does not exist yet, please add the user first.')
    else:
        print("User was successfully deleted")


# @pysnooper.snoop(depth=3)
# def save_users():
#     """
#     Saves user database into a file
#     """
#     # filename = input('Enter filename for users file: ')
#     main.save_users(user_collection)

# @pysnooper.snoop(depth=2)
def add_status():
    """
    Adds a new status into the database
    """
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(status_id, user_id, status_text):
        print("An error occurred while trying to add new status")
    elif users.UserCollection.search_user(user_id=user_id) is None:
        print('This user does not exist yet, please add the user first.')
    else:
        print("New status was successfully added")


# @pysnooper.snoop()
def update_status():
    """
    Updates information for an existing status
    """
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.update_status(status_id, user_id, status_text):
        print("An error occurred while trying to update status")
    elif users.UserCollection.search_user(user_id=user_id) is None:
        print('This user does not exist yet, please add the user first.')
    else:
        print("Status was successfully updated")


# @pysnooper.snoop(depth=2)
def search_status():
    """
    Searches a status in the database
    """
    status_id = input('Enter status ID to search: ')
    result = main.search_status(status_id)
    if not result:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Status ID: {result.status_id}")
        print(f"Status text: {result.status_text}")


# @pysnooper.snoop(depth=3)
def delete_status():
    """
    Deletes status from the database
    """
    status_id = input('Status ID: ')
    if not main.delete_status(status_id):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def quit_program():
    """
    Quits program
    """
    sys.exit()


if __name__ == '__main__':
    # user_collection = main.init_user_collection()
    users.UserCollection.db_connect()
    user_status.UserStatusCollection.db_connect()
    # status_collection = main.init_status_collection()

    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': add_status,
        'H': update_status,
        'I': search_status,
        'J': delete_status,
        'Q': quit_program
    }

    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Add status
                            H: Update status
                            I: Search status
                            J: Delete status
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
