"""
# Title: main driver for a simple social network project
# Who: ALarson
# What/When: 4/24/2022 - started assignment
"""
import csv
from loguru import logger
import user_status
import users
import socialnetworkmodel as sn


def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    user = users.UserCollection
    return user


def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    status = user_status.UserStatusCollection
    return status


# @pysnooper.snoop
def load_users(filename):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    """
    # users.UserCollection.db_connect()
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            file_users = csv.DictReader(file)
            for row in file_users:
                try:
                    with sn.db.transaction():
                        new_user = users.UserCollection.create(
                            user_id=row['USER_ID'],
                            email=row['EMAIL'],
                            user_name=row['NAME'],
                            user_last_name=row['LASTNAME'])
                        new_user.save()


                except Exception as error:
                    logger.info('Error creating user')
                    logger.info(error)
    except FileNotFoundError:
        print('File not found')


# @pysnooper.snoop(depth=2)
def load_status_updates(filename):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """

    # i spent 4 hours trying to make it faster and this is actually slower - takes 4 minutes
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            dict_table = [{k.lower(): v for k, v in row.items()}
                          for row in csv.DictReader(file, skipinitialspace=True)]
    except FileNotFoundError:
        logger.info('File not found...')

    try:
        with sn.db.atomic():
            for idx in range(0, len(dict_table), 100):
                user_status.UserStatusCollection.insert_many(dict_table[idx:idx + 100]).execute()
    except Exception as error:
        logger.info('Did not add statuses to the database.')
        logger.info(error)


# # this works, but it is very slow vv
#     user_status.UserStatusCollection.db_connect()
#     try:
#         with open(filename, newline='', encoding="UTF-8") as file:
#             file_status = csv.DictReader(file)
#             for row in file_status:
#                 try:
#                     with sn.db.transaction():
#                         new_status = user_status.UserStatusCollection.create(
#                             user_id=row['USER_ID'],
#                             status_id=row['STATUS_ID'],
#                             status_text=row['STATUS_TEXT'])
#                         new_status.save()
#                         logger.info('Got to here')
#
#                 except Exception as e:
#                     logger.info('Error creating status')
#                     logger.info(e)
#     except FileNotFoundError:
#         print('File not found')


def add_user(user_id, email, user_name, user_last_name):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    new_user = users.UserCollection.add_user(user_id, email, user_name, user_last_name)
    # users.UserCollection.save()
    return new_user


def update_user(user_id, email_update, user_name_update, user_last_name_update):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    updated_user = users.UserCollection.modify_user(user_id,
                                                    email_update,
                                                    user_name_update,
                                                    user_last_name_update
                                                    )
    # updated_user.save()
    return updated_user


def delete_user(user_id):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    del_user = users.UserCollection.delete_user(user_id)
    return del_user


def search_user(user_id):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    find_user = users.UserCollection.search_user(user_id)
    return find_user


def add_status(status_id, user_id, status_text):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    add_new_status = user_status.UserStatusCollection.add_status(status_id, user_id, status_text)
    return add_new_status


def update_status(status_id, user_id, status_text):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    updated_status = user_status.UserStatusCollection.modify_status(status_id, user_id, status_text)
    return updated_status


def delete_status(status_id):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    del_status = user_status.UserStatusCollection.delete_status(status_id)
    return del_status


def search_status(status_id):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    if user_status.UserStatusCollection.search_status(status_id) is None:
        return False

    return user_status.UserStatusCollection.search_status(status_id)
