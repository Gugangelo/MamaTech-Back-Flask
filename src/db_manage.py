from flask_sqlalchemy import SQLAlchemy

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Db_manager(metaclass=SingletonMeta):
    def __init__(self):
        self.db=None

    def int_db_connection(self):
        self.db = SQLAlchemy()
        return self.db

    def get_db(self):
        if self.db is None:
            self.int_db_connection()

        return self.db