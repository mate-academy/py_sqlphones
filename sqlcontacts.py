"""modules for working with data."""
import sqlite3


class PhoneBook:
    """Class to represent phone book"""
    def __init__(self):
        self.data_base = sqlite3.connect(":memory:")
        self.data_base.execute("""create table phone_book
            (id integer primary key,
            name varchar(30) unique,
            phone varchar(30)
            )""")

    def create(self, name, phone):
        """
        Create new contact in phone book.
        :param name: name of contact
        :param phone: phone number of contact
        :return: None
        :raise ValueError in case of invalid number or name
        """
        if not name or not phone:
            raise ValueError
        try:
            self.data_base.execute("""insert into phone_book
                                (name, phone) values (?, ?)""", (name, phone))
        except sqlite3.IntegrityError:
            raise KeyError

    def read(self, name):
        """
        Read contact in phone book
        :param name: name of contact
        :return: phone of specified contact
        :raise KeyError if contact doesnt exist
        """
        row = self.data_base.execute("""select name, phone from phone_book
                                        where name=?""", (name,)).fetchone()
        if not row:
            raise KeyError
        return int(row[1])

    def update(self, name, phone):
        """
        Update contact in phone book
        :param name: name to update
        :param phone: phone number to update
        :return: None
        :raise: KeyError if contact doesnt exist
        """
        row = self.data_base.execute("""select name, phone from phone_book
                                        where name=?""", (name,)).fetchone()
        if not row:
            raise KeyError
        self.data_base.execute("""update phone_book set phone=?
                                        where name=?""", (phone, name))

    def delete(self, name):
        """
        Delete contact from phone book
        :param name: name of contact
        :return: None
        :raise: KeyError if contact doesnt exist
        """
        row = self.data_base.execute("""select name from phone_book
                                        where name=?""", (name,)).fetchone()
        if not row:
            raise KeyError
        self.data_base.execute("delete from phone_book where name=?", (name,))
