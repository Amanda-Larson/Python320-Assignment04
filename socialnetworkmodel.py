"""social network database model"""

import peewee as pw
from loguru import logger
import os

# check to see if the files exists, if it does, delete it
file = 'social_network.db'
if os.path.exists(file):
    os.remove(file)

# connect to the database
db = pw.SqliteDatabase(file)


# set up a base model for inheritance into the classes which become database tables
class BaseModel(pw.Model):
    logger.info("allows database to be defined or changed in one place")

    class Meta:
        database = db

    # @staticmethod
    # def main():
    #     db.connect()
    #     db.execute_sql('PRAGMA foreign_keys = ON;')
    #     db.create_tables([users.UserTable, user_status.UserStatusTable])
