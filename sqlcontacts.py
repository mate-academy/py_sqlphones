"""
Realisation phone book model.
Classes
-------
PhoneBook
"""
import sqlite3


class PhoneBook:
    """
    PhoneBook logic realisation
    Attributes
    ----------
    Methods
    -------
    create()
    read()
    update()
    delete()
    """
    def __init__(self):
        self._conn = sqlite3.connect(":memory:")
        try:
            self._conn.execute("""create table contacts (
            id integer primary key,
            name varchar(30) unique,
            phone varchar(30)
            )""")

        except sqlite3.OperationalError:
            pass

    def _empty_checker(self, name):
        """empty checker"""
        try:
            sql = "select name from contacts where name=?"
            return self._conn.execute(sql, (name,)).fetchone()[0]
        except TypeError:
            raise KeyError

    def create(self, name, phone):
        """
        Create record in phone book
        """
        sql = "insert into contacts (name, phone) values (?, ?)"
        try:
            self._conn.execute(sql, (name, phone))
            self._conn.commit()
        except sqlite3.IntegrityError:
            raise KeyError

    def read(self, name):
        """
        Read record from phone book
        """
        try:
            sql = "select phone from contacts where name=?"
            phone = self._conn.execute(sql, (name,)).fetchone()[0]
            return int(phone)
        except TypeError:
            raise KeyError

    def update(self, name, phone):
        """
        Update record in phone book
        """
        self._empty_checker(name)
        sql = "update contacts set phone=? where name=?"
        self._conn.execute(sql, (phone, name))
        self._conn.commit()

    def delete(self, name):
        """
        Delete record from phone book
        """
        self._empty_checker(name)
        sql = "delete from contacts where name=?"
        self._conn.execute(sql, (name,))
        self._conn.commit()
