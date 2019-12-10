"""
Module with functions for main
"""
from sqlcontacts import PhoneBook


class Interface:
    """
    Class Interface interacts with user input from console.
    """

    def __init__(self, phone_book: PhoneBook):
        self.phone_book = phone_book

    def add_record_by_user_input(self):
        """
        Create new record in phone book by using user input.
        :return: None
        """
        record_id = int(input('Id of user: '))
        full_name = input('Full name: ').lower().capitalize()
        phone = int(input('Phone: '))
        self.phone_book.create_new_record(record_id, full_name, phone)

    def remove_record_by_user_input(self):
        """
        Remove record from phone book by using user input.
        :return: None
        """
        full_name = input('Full name: ').lower().capitalize()
        self.phone_book.remove_record_by_name(full_name)

    def update_record_by_user_input(self):
        """
        Update record in phone book by using user input.
        :return: None
        """

        full_name = input('Full name: ').lower().capitalize()
        phone = int(input('Phone: '))
        self.phone_book.update_record_by_name(full_name, phone)

    def get_phone_by_user_input(self):
        """
        Get phone information by using user input.
        :return: None
        """
        full_name = input('Full name: ').lower().capitalize()
        print(self.phone_book.get_phone_by_name(full_name))
