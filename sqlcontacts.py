"""
sqlite database with contacts
"""
import sqlite3


class PhoneBook:
    """
    PhoneBook class
    """
    def __init__(self):
        self.conn = sqlite3.connect("phone_book.db")
        self.conn.execute("""CREATE TABLE IF NOT EXISTS first_phone_book(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30) UNIQUE, phone VARCHAR(30))""")

    def create(self, name, phone):
        """
        Update database
        :param name:
        :param phone:
        :return:
        """
        sql = "INSERT OR IGNORE INTO " \
              "first_phone_book (name, phone) VALUES(?, ?)"
        try:
            self.conn.execute(sql, (name, phone))
            self.conn.commit()
        except sqlite3.OperationalError:
            raise KeyError

    def read(self, name):
        """
        search contact
        :param name:
        :return:
        """
        sql = """SELECT phone FROM first_phone_book WHERE name=?"""
        res = self.conn.execute(sql, (name,))
        res = res.fetchone()
        if not res:
            raise KeyError
        return res[0]

    def update(self, name, phone):
        """
        Change contact
        :param name:
        :param phone:
        :return:
        """
        sql = """UPDATE first_phone_book SET phone=? WHERE name=?"""
        self.conn.execute(sql, (phone, name))
        self.conn.commit()

    def delete(self, name):
        """
        Delete contact
        :param name:
        :return:
        """
        sql = """DELETE FROM first_phone_book
                 WHERE name=?"""
        self.conn.execute(sql, (name,))
        self.conn.commit()
