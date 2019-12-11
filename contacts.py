"""
Realisation phone book model.
Classes
-------
PhoneBook
"""
import pickle


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
        self._db_name = "dump.pickle"
        self._phone_book = {}

    def _save(self):
        """Save self._phone_book in pickle file"""
        with open(self._db_name, 'wb') as data:
            pickle.dump(self._phone_book, data)

    def create(self, name, phone):
        """
        Create record in phone book
        """
        if name in self._phone_book:
            raise KeyError
        self._phone_book[name] = phone
        self._save()

    def read(self, name):
        """
        Read record from phone book
        """
        if name in self._phone_book:
            return self._phone_book[name]
        raise KeyError

    def update(self, name, phone):
        """
        Update record in phone book
        """
        if name not in self._phone_book:
            raise KeyError
        self._phone_book[name] = phone
        self._save()

    def delete(self, name):
        """
        Delete record from phone book
        """
        self._phone_book.pop(name)
        self._save()
