"""
classes to manage the user status messages
"""
# pylint: disable=R0903
# pylint: disable=W0703

from loguru import logger
import peewee as pw

import users
import socialnetworkmodel as sn

logger.info("Let's get to debugging user_status/py")
logger.add("users_and_status.log", backtrace=True, diagnose=True)


class UserStatusCollection(sn.BaseModel):
    """
    Collection of UserStatus messages
    """

    logger.info("notice peewee data type")

    user_id = pw.ForeignKeyField(users.UserCollection, to_field='user_id',
                                 related_name='the user', null=False)
    status_id = pw.CharField(primary_key=True)
    status_text = pw.CharField(max_length=140, constraints=[pw.Check("LENGTH(user_id) < 30")])

    @staticmethod
    def db_connect():
        """This connects the database and creates the table"""
        logger.info("Set up the database.")
        # sn.db.connect()
        # sn.db.execute_sql('PRAGMA foreign_keys = ON;')
        sn.db.create_tables([UserStatusCollection])
        logger.info('db is connected')

    @staticmethod
    def add_status(status_id, user_id, status_text):
        """
        add a new status message to the collection
        """
        try:
            new_status = UserStatusCollection.create(
                status_id=status_id,
                user_id=user_id,
                status_text=status_text
            )
            new_status.save()
            return True
        except pw.IntegrityError as error:
            logger.exception(error)
            return False

    @staticmethod
    def modify_status(status_id, user_id, status_text):
        """
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        """

        try:
            if status_id not in UserStatusCollection.status_id:
                logger.info("Status_id {status_id} does not exist")
                return False
            modify_status = UserStatusCollection.get(UserStatusCollection.status_id == status_id)
            modify_status.user_id = user_id
            modify_status.status_text = status_text
            modify_status.save()
            return True
        except pw.DoesNotExist as error:
            logger.exception(error)
            return False

    @staticmethod
    def delete_status(status_id):
        """
        deletes the status message with id, status_id
        """
        try:
            del_status = UserStatusCollection.get(
                UserStatusCollection.status_id == status_id)
            del_status.delete_instance()
            return del_status
        except pw.DoesNotExist as error:
            logger.exception(error)
            return False

    @staticmethod
    def search_status(status_id):
        """
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        """
        try:
            find_status = UserStatusCollection.select().where(
                UserStatusCollection.status_id == status_id).get()
            return find_status
        except pw.DoesNotExist:
            # logger.info(e)
            print('Status ID does not exist, please try again.')
            return None

    @staticmethod
    def search_all_status_updates(user_id):
        """This searches all status updates"""
        try:
            find_statuses = UserStatusCollection.select() \
                .where(UserStatusCollection.user_id == user_id)
            logger.info(find_statuses)
            statuses = [status.status_text for status in find_statuses]
            return statuses
        except pw.DoesNotExist:
            print('This user id does not exist, please try another...')
            return None
        except TypeError as error:
            logger.info(error)
            return None

    @staticmethod
    def filter_status_by_string(string):
        """This filters all statuses by a user-input string"""
        query = UserStatusCollection.select() \
            .where(UserStatusCollection.status_text.contains(string)).iterator()
        logger.info(query)
        # matching_statuses = [status.status_text for status in query]
        return query
