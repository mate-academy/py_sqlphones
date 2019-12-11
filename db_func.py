"""
Module for working with database.
"""
import sqlite3


class PhoneBookDatabase:
    """
    Class with CRUD properties for phone book database.
    """

    @staticmethod
    def create_db(con_name) -> None:
        """
        Create database.
        :param con_name: str
        :return: None
        """
        database = sqlite3.connect(con_name)
        cursor = database.cursor()
        cursor.execute("""CREATE TABLE Phonebook (
        Id INTEGER PRIMARY KEY,
        Name VARCHAR(30) NOT NULL UNIQUE,
        Phone INTEGER
        )""")
        database.commit()
        cursor.close()

    @staticmethod
    def add_new_record_to_db(con_name, args=()) -> None:
        """
        Create new record in database.
        :param con_name: str
        :param args: tuple
        :return: None
        """
        try:
            database = sqlite3.connect(con_name)
            cursor = database.cursor()
            cursor.execute("INSERT INTO Phonebook VALUES (?, ?, ?)", args)
            database.commit()
            cursor.close()
        except sqlite3.IntegrityError:
            raise KeyError

    @staticmethod
    def update_record_in_pb(con_name, args=()) -> None:
        """
        Update record in database.
        :param con_name: str
        :param args: tuple
        :return: None
        """
        database = sqlite3.connect(con_name)
        cursor = database.cursor()
        cursor.execute("UPDATE Phonebook SET Phone=? WHERE Name=?", args)
        database.commit()
        cursor.close()

    @staticmethod
    def delete_record_from_pb(con_name, args=()) -> None:
        """
        Delete record in database.
        :param con_name: str
        :param args: tuple
        :return: None
        """
        database = sqlite3.connect(con_name)
        cursor = database.cursor()
        cursor.execute("DELETE FROM Phonebook where Name=?", args)
        database.commit()
        cursor.close()

    @staticmethod
    def get_all_records_from_pb(con_name) -> list:
        """
        Get all records from table.
        :param con_name: str
        :return: None
        """
        database = sqlite3.connect(con_name)
        cursor = database.execute("SELECT * FROM Phonebook")
        return cursor.fetchall()

    @staticmethod
    def get_phone_from_pb(con_name, args=()) -> list:
        """
        Get all records from table.
        :param con_name: str
        :param args: tuple
        :return: list
        """
        database = sqlite3.connect(con_name)
        cursor = database.execute("SELECT Phone FROM Phonebook WHERE Name=?",
                                  args)
        return cursor.fetchall()
