"""
Module with phonebook options
create
read
update
delete
_save into pickle file
"""
import pickle


class PhoneBook:
    """
    Phonebook class
    """
    def __init__(self):
        self._file = 'phone_book.pickle'
        self._book = {}

    def create(self, name, phone):
        """
        Create a new contact
        :param name:
        :param phone:
        :return:
        """
        if name in self._book:
            raise KeyError
        self._book[name] = phone
        self._save()

    def read(self, name):
        """
        Return contact by name
        :param name:
        :return:
        """
        self._load()
        if name in self._book:
            return self._book[name]
        raise KeyError

    def update(self, name, phone):
        """
        Update phone number by name
        :param name:
        :param phone:
        :return:
        """
        self._load()
        if name not in self._book:
            raise KeyError
        self._book[name] = phone
        self._save()

    def delete(self, name):
        """
        Delete contact
        :param name:
        :return:
        """
        self._load()
        if name not in self._book:
            raise KeyError
        del self._book[name]
        self._save()

    def _save(self):
        """
        Save changes into pickle file
        :return:
        """
        with open(self._file, 'wb') as data:
            pickle.dump(self._book, data)

    def _load(self):
        """
        load pickle file
        :return:
        """
        with open(self._file, 'rb') as _file:
            self._book = pickle.load(_file)

    def _clear(self):
        """
        Clear a dict
        :return:
        """
        self._book = {}
