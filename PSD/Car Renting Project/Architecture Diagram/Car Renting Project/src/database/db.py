# import sqlite3
# from src.patterns.singleton import SingletonMeta

# class Database(metaclass=SingletonMeta):
#     def __init__(self, db_name="car_rental.db"):
#         self.connection = sqlite3.connect(db_name)
#         self.connection.row_factory = sqlite3.Row

#     def get_connection(self):
#         return self.connection

import sqlite3
from pathlib import Path
from src.patterns.singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    def __init__(self):
        db_path = Path("car_rental.db")
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row

    def get_connection(self):
        return self.connection

    def close(self):
        self.connection.close()