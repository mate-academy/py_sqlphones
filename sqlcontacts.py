"""modules for working with data."""
import sqlite3


class PhoneBook:
    """Class to represent phone book"""
    def __init__(self):
        self.data_base = sqlite3.connect(":memory:")
        self.data_base.execute("""create table phone_book
            (id integer primary key,
            name varchar(30),
            phone varchar(30)
            )""")

    def create(self, name, phone):
        """
        Create new contact in phone book.
        :param name: name of contact
        :param phone: phone number of contact
        :return: string report to user
        :raise ValueError in case of invalid number or name
        """
        if not name or not phone:
            raise ValueError
        self.data_base.execute("""insert into phone_book
                            (name, phone) values (?, ?)""", (name, phone))
        return "Added"

    def read(self, name):
        """
        Read contact in phone book
        :param name: name of contact
        :return: phone of specified contact
        :raise KeyError if contact doesnt exist
        """
        cursor = self.data_base.execute("""select name, phone from phone_book
                                        where name=?""", (name,))
        cursor = cursor.fetchall()
        if not cursor:
            raise KeyError
        return int(cursor[0][1])

    def update(self, name, phone):
        """
        Update contact in phone book
        :param name: name to update
        :param phone: phone number to update
        :return: string report to user
        :raise: KeyError if contact doesnt exist
        """

        cursor = self.data_base.execute("""select id, name from phone_book
                                        where name=?""", (name,))
        cursor = cursor.fetchall()
        if not cursor:
            raise KeyError
        id_ = cursor[0][0]
        self.data_base.execute("""update phone_book set phone=?
                                        where id=?""", (phone, id_))
        return "Updated"

    def delete(self, name):
        """
        Delete contact from phone book
        :param name: name of contact
        :return: string report to user
        :raise: KeyError if contact doesnt exist
        """
        cursor = self.data_base.execute("""select id, name from phone_book
                                        where name=?""", (name,))
        cursor = cursor.fetchall()
        if not cursor:
            raise KeyError
        id_ = cursor[0][0]
        self.data_base.execute("delete from phone_book where id=?", (id_,))
        return "Deleted"
