"""
Module used to create phone books.

Functions
---------
open_book()
save_book()

Classes
-------
PhoneBook
"""
import pickle


def open_book(book_name):
    """
    Return content of a pickled file if this file
    exists, otherwise return None.
    """
    try:
        with open(book_name, 'rb') as book:
            return pickle.load(book)
    except FileNotFoundError:
        return None


def save_book(book_name, session):
    """Save changes made in the book in a pickle format"""
    with open(book_name, 'wb') as book:
        pickle.dump(session, book)


class PhoneBook:
    """
    Attributes
    ----------
    phone_book : dict -- storage for all names and numbers

    Methods
    -------
    create()
    read()
    update()
    delete()
    show_all()
    """
    def __init__(self):
        self.phone_book = {}

    def create(self, name, phone):
        """Add new name-number pair to the phone book"""
        if name in self.phone_book:
            raise NameError
        self.phone_book[name] = phone

    def read(self, name):
        """Print number of a person by name"""
        return self.phone_book[name]

    def update(self, name, phone):
        """Update number of a person by name"""
        if name in self.phone_book:
            self.phone_book[name] = phone
        else:
            raise NameError

    def delete(self, name):
        """Delete name-number pair from the phone book"""
        del self.phone_book[name]

    def show_all(self):
        """Print all names in the phone book"""
        return ' | '.join(self.phone_book.keys())
