"""Module describes phone book"""
import sqlite3


class PhoneBook:
    """Phone book class"""
    def __init__(self):
        self._db_file_name = 'phone_book.db'
        with sqlite3.connect(self._db_file_name) as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS phone_book(
                        contact_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        phone INTEGER NOT NULL);""")
            conn.commit()

    def create(self, *args):
        """Creating phone book
        (The must be validation of the phone)
        :param args: name, phone
        :return:
        """
        sql = """INSERT INTO phone_book(name, phone)
                            VALUES(?,?)"""
        self.create_connection_and_exec(sql, args)

    def update(self, *args):
        """
        Update data about contact (I'd add validation)
        :param args: name, phone
        :return:
        """
        sql = """UPDATE phone_book SET phone=? WHERE name=?"""
        self.create_connection_and_exec(sql, args[::-1])

    def delete(self, name):
        """Delete contact (I'd add validation)
        :param name: name of contact
        :return:
        """
        sql = """DELETE FROM phone_book WHERE name=?"""
        self.create_connection_and_exec(sql, (name,))

    def read(self, name):
        """Read from phone book
        :param name: name of contact
        :return:
        """
        contact = (name,)
        sql = """SELECT phone FROM phone_book WHERE name=?"""
        with sqlite3.connect(self._db_file_name) as conn:
            cur = conn.cursor()
            cur.execute(sql, contact)
            record = cur.fetchone()
        if not record:
            raise KeyError
        return record[0]

    def create_connection_and_exec(self, sql, data):
        """Reusable method for connecting with DB"""
        conn = sqlite3.connect(self._db_file_name)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
