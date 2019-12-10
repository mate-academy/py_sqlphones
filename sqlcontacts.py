"""
Module used to create phone books.

Functions
---------
open_book()

Classes
-------
PhoneBook
"""


import sqlite3
import pickle


def open_book(book_name):
    """
    Return content of a pickled file if this file
    exists, otherwise return None.
    """
    new_book = PhoneBook()
    try:
        with open(book_name, 'rb') as book:
            old_book = pickle.load(book)
            for name, number in old_book:
                new_book.create(name, number)
            return new_book
    except FileNotFoundError:
        return None


class PhoneBook:
    """
    Attributes
    ----------
    book

    Methods
    -------
    save_book()
    create()
    read()
    update()
    delete()
    name_in_book()
    show_all()
    """
    def __init__(self):
        self.book = sqlite3.connect(":memory:")
        self.book.execute("""create table phone_book (
        id integer primary key,
        name varchar(20),
        number integer
        )""")

    def save_book(self, book_name):
        """Save changes made in the book in a pickle format"""
        names = self.show_all().split(' | ')
        numbers = [self.read(name) for name in names]
        new_data = zip(names, numbers)
        with open(book_name, 'wb') as book:
            pickle.dump(new_data, book)

    def create(self, name, phone):
        """Add new name-number pair to the phone book"""
        if self.name_in_book(name):
            raise NameError
        self.book.execute("insert into phone_book (name, number) \
                          values (?, ?)", (name, phone))

    def read(self, name):
        """Return number of a person by name"""
        try:
            phone = self.book.execute("select number from phone_book \
                                      where name=?", (name,)).fetchone()[0]
            if phone:
                return phone
        except TypeError:
            raise KeyError
        return 0  # for pylint

    def update(self, name, phone):
        """Update number of a person by name"""
        if self.name_in_book(name):
            self.book.execute("update phone_book set number=? \
                               where name=?", (phone, name))
        else:
            raise NameError

    def delete(self, name):
        """Delete name-number pair from the phone book"""
        if self.name_in_book(name):
            self.book.execute("delete from phone_book \
                               where name=?", (name,))
        else:
            raise NameError

    def name_in_book(self, name):
        """Return True if name is in the book, else False"""
        try:
            self.read(name)
            return True
        except KeyError:
            return False

    def show_all(self):
        """Return all names in the phone book"""
        return (' | '.join([name[0] for name
                            in self.book.execute("select \
                             name from phone_book")]))
