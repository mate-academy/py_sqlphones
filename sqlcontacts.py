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
            phone int
            )""")

        except sqlite3.OperationalError:
            pass

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
        sql = "select phone from contacts where name=?"
        result = self._conn.execute(sql, (name,))
        result = result.fetchone()
        if not result:
            raise KeyError
        return result[0]

    def update(self, name, phone):
        """
        Update record in phone book
        """
        self.read(name)
        sql = "update contacts set phone=? where name=?"
        self._conn.execute(sql, (phone, name))
        self._conn.commit()

    def delete(self, name):
        """
        Delete record from phone book
        """
        self.read(name)
        sql = "delete from contacts where name=?"
        self._conn.execute(sql, (name,))
        self._conn.commit()
