"""Module contacts"""


import pickle


class PhoneBook:
    """Class PhoneBook"""
    def __init__(self):
        self.data = {}
        self.file_name = 'db_phonebook.txt'

    def create(self, name, phone):
        """Create new name and phone"""
        if name in self.data:
            raise KeyError
        self.data[name] = phone
        self.data_save()

    def read(self, name):
        """Read phone number"""
        if name in self.data:
            return self.data[name]
        raise KeyError

    def update(self, name, phone):
        """Update phone number"""
        if name not in self.data:
            raise KeyError
        self.data[name] = phone
        self.data_save()

    def delete(self, name):
        """Delete name"""
        self.data.pop(name)
        self.data_save()

    def data_save(self):
        """Save data to file"""
        with open(self.file_name, 'wb') as wfile:
            pickle.dump(self.data, wfile)