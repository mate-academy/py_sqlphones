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
        try:
            full_name = input('Full name: ').lower().capitalize()
            phone = int(input('Phone: '))
            if not self.phone_book.check_name_exist(full_name):
                self.phone_book.create_new_record(full_name, phone)
                print(f"Successfully created record with name {full_name} "
                      f"and phone number {phone}")
            else:
                print(f"This contact name: {full_name} "
                      f"with phone number: {phone} "
                      f"is already exist in our phone book")
        except ValueError:
            print("Please try again and insert integer value")

    def remove_record_by_user_input(self):
        """
        Remove record from phone book by using user input.
        :return: None
        """
        full_name = input('Full name: ').lower().capitalize()
        if self.phone_book.check_name_exist(full_name):
            self.phone_book.remove_record_by_name(full_name)
            print(f"Successfully removed contact name {full_name}")
        else:
            print(f"This contact name: {full_name} "
                  f"doesn't exist in our phone book")

    def update_record_by_user_input(self):
        """
        Update record in phone book by using user input.
        :return: None
        """
        try:
            full_name = input('Full name: ').lower().capitalize()
            phone = int(input('Phone: '))
            if self.phone_book.check_name_exist(full_name):
                self.phone_book.update_record_by_name(full_name, phone)
                print(f"Successfully updated record with "
                      f"name {full_name} and new phone number {phone}")
            else:
                print(f"This contact name: {full_name} "
                      f"doesn't exist in our phone book")
        except ValueError:
            print("Please try again and insert integer value")

    def get_phone_by_user_input(self):
        """
        Get phone information by using user input.
        :return: None
        """
        full_name = input('Full name: ').lower().capitalize()
        if self.phone_book.check_name_exist(full_name):
            print(self.phone_book.get_phone_by_name(full_name))
        else:
            print(f"This contact name: {full_name} "
                  f"doesn't exist in our phone book")
