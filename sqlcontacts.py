"""
Model
"""
import db_func as db


class PhoneBook:
    """
    Class represents phone book.
    """

    def __init__(self):
        self._phone_book = {}
        self._con_name = "phonebook.sqllite"

    def __str__(self) -> str:
        return f"{self._phone_book}"

    def __repr__(self) -> str:
        return f"PhoneBook:{self._phone_book}"

    def get_all_data(self):
        """
        Get phone book dictionary.
        :return: dict
        """
        return self._phone_book

    def get_phone_by_name(self, contact_name):
        """
        Get phone information by contact name.
        :param contact_name: str
        :return: int
        """
        return self._phone_book[contact_name]

    def check_name_exist(self, contact_name):
        """
        Check if name exist in phone book dict.
        :param contact_name: str
        :return: bool
        """
        return contact_name in self._phone_book

    def create_new_record(self, new_contact_name, new_contact_phone):
        """
        Add a new record to the phone book that avoids to add duplicates.
        :param new_contact_name: str
        :param new_contact_phone: int
        :return: None
        """
        if not self.check_name_exist(new_contact_name):
            self._phone_book[new_contact_name] = new_contact_phone
            db.add_new_record_to_db(self._con_name, (new_contact_name, new_contact_phone))

    def remove_record_by_name(self, contact_name):
        """
        Remove record from phone book by contact name.
        :param contact_name: str
        :return: None
        """
        self._phone_book.pop(contact_name)
        db.delete_record_from_phone_book(self._con_name, (contact_name,))

    def update_record_by_name(self, contact_name, new_phone_number):
        """
        Update record in phone book by contact name.
        :param contact_name: str
        :param new_phone_number: int
        :return: None
        """
        self._phone_book[contact_name] = new_phone_number
        db.update_record_in_phone_book(self._con_name, (new_phone_number, contact_name))
