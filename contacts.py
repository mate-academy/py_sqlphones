"""contacts phone book"""
from pickle import dump


def save(func):
    """save phone book decorator"""
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        with open(args[0].filename, "wb") as save_file:
            dump(args[0].filename, save_file)
    return wrapper


def check_present_name(method):
    """return NONE, i don`t know why.."""
    def inner(*args, **kwargs):
        if args[1] in args[0].users:
            method(*args, **kwargs)
        else:
            raise ValueError
    return inner


class PhoneBook:
    """represent phone book"""
    def __init__(self):
        self.filename = "phone_book.pickle"
        self.users = {}

    @save
    def create(self, name, phone):
        """create new user"""
        self.users[name] = phone

    def read(self, name):
        """read new user"""
        if name in self.users:
            return self.users[name]
        raise KeyError

    @save
    def update(self, name, phone):
        """update information"""
        if name in self.users:
            self.users[name] = phone
        else:
            raise ValueError

    @save
    def delete(self, name):
        """delete user"""
        if name in self.users:
            self.users.pop(name)
        else:
            raise ValueError
