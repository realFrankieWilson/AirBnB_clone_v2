#!/usr/bin/python3
"""
    A file that treats the directory as a package.
"""

from os import getenv


if_database = getenv("HBNB_TYPE_STORAGE")

if if_database == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
