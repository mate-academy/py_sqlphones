'''
This a console-based application
'''
import pickle


class PhoneBook:
    '''
    Class for working only with phone book db
    Have methods:
        save(), create(name, phone), read(name),
        update(name, phone), delete(name)
    '''
    def __init__(self):
        self.data_base_file_name = 'phone_db'
        self.phone_book = {}

    def save(self):
        '''Method for save all information in db'''
        with open(self.data_base_file_name, 'ab') as d_b:
            pickle.dump(self.phone_book, d_b)

    def create(self, name, phone):
        '''Create new contact and save in db'''
        if name in self.phone_book.keys():
            return "A phone with this name already exists"
        self.phone_book[name] = phone
        self.save()
        return "Phone : Name:{} Number:{} create".format(name, phone)

    def read(self, name):
        '''Read contact from db'''
        if name in self.phone_book.keys():
            return self.phone_book[name]
        raise KeyError

    def update(self, name, phone):
        '''Update contact adn save in db'''
        if name in self.phone_book.keys():
            self.phone_book[name] = phone
            self.save()
            return "Update phone number"
        raise KeyError

    def delete(self, name):
        '''Delete contact and save db'''
        if name in self.phone_book.keys():
            del self.phone_book[name]
            self.save()
            return "Delete phone number"
        raise KeyError
