import sqlite3


def create_db(con) -> None:
    db = sqlite3.connect(con)
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE Phonebook (
    Id INTEGER primary key /*autoincrement needs PK*/,
    Name VARCHAR(30),
    Phone INTEGER
    )""")
    db.commit()
    cursor.close()


def add_new_record_to_db(con, args=()) -> None:
    db = sqlite3.connect(con)
    cursor = db.cursor()
    cursor.execute("INSERT INTO Phonebook VALUES (?, ?)", args)
    db.commit()
    cursor.close()


def update_record_in_phone_book(con, args=()) -> None:
    db = sqlite3.connect(con)
    cursor = db.cursor()
    cursor.execute("UPDATE Phonebook SET Phone=? WHERE Name=?", args)
    db.commit()
    cursor.close()


def delete_record_from_phone_book(con, args=()) -> None:
    db = sqlite3.connect(con)
    cursor = db.cursor()
    cursor.execute("DELETE FROM Phonebook where Name=?", args)
    db.commit()
    cursor.close()


def get_all_records_from_phone_book(con) -> list:
    """
    Get all records from table.
    """
    db = sqlite3.connect(con)
    cursor = db.execute("SELECT * FROM Students")
    return cursor.fetchall()


if __name__ == "__main__":
    con = "phonebook.sqllite"
    create_db(con)
