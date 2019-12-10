"""
Module for working with database.
"""
import sqlite3


def create_db(con) -> None:
    """
    Create database.
    :param con: str
    :return: None
    """
    database = sqlite3.connect(con)
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE Phonebook (
    Id INTEGER PRIMARY KEY,
    Name VARCHAR(30) NOT NULL UNIQUE,
    Phone INTEGER
    )""")
    database.commit()
    cursor.close()


def add_new_record_to_db(con, args=()) -> None:
    """
    Create new record in database.
    :param con: str
    :param args: tuple
    :return: None
    """
    try:
        database = sqlite3.connect(con)
        cursor = database.cursor()
        cursor.execute("INSERT INTO Phonebook VALUES (?, ?, ?)", args)
        database.commit()
        cursor.close()
    except sqlite3.IntegrityError:
        raise KeyError


def update_record_in_phone_book(con, args=()) -> None:
    """
    Update record in database.
    :param con: str
    :param args: tuple
    :return: None
    """
    database = sqlite3.connect(con)
    cursor = database.cursor()
    cursor.execute("UPDATE Phonebook SET Phone=? WHERE Name=?", args)
    database.commit()
    cursor.close()


def delete_record_from_phone_book(con, args=()) -> None:
    """
    Delete record in database.
    :param con: str
    :param args: tuple
    :return: None
    """
    database = sqlite3.connect(con)
    cursor = database.cursor()
    cursor.execute("DELETE FROM Phonebook where Name=?", args)
    database.commit()
    cursor.close()


def get_all_records_from_phone_book(con) -> list:
    """
    Get all records from table.
    :param con: str
    :return: None
    """
    database = sqlite3.connect(con)
    cursor = database.execute("SELECT * FROM Phonebook")
    return cursor.fetchall()


def get_phone_from_phone_book(con, args=()) -> list:
    """
    Get all records from table.
    :param con: str
    :param args: tuple
    :return: list
    """
    database = sqlite3.connect(con)
    cursor = database.execute("SELECT Phone FROM Phonebook WHERE Name=?", args)
    return cursor.fetchall()
