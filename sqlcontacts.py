"""
Model
"""
import db_func as db


class PhoneBook:
    """
    Class represents phone book.
    """

    def __init__(self, con_name):
        self._con_name = con_name

    def get_all_data(self):
        """
        Get phone book dictionary.
        :return: dict
        """
        return db.get_all_records_from_phone_book(self._con_name)

    def get_phone_by_name(self, contact_name):
        """
        Get phone information by contact name.
        :param contact_name: str
        :return: int
        """
        return db.get_phone_from_phone_book(self._con_name, (contact_name,))

    def create_new_record(self, record_id, new_contact_name, new_contact_phone):
        """
        Add a new record to the phone book that avoids to add duplicates.
        :param new_contact_name: str
        :param new_contact_phone: int
        :return: None
        """
        db.add_new_record_to_db(self._con_name,
                                (record_id, new_contact_name, new_contact_phone))

    def remove_record_by_name(self, contact_name):
        """
        Remove record from phone book by contact name.
        :param contact_name: str
        :return: None
        """
        db.delete_record_from_phone_book(self._con_name, (contact_name,))

    def update_record_by_name(self, contact_name, new_phone_number):
        """
        Update record in phone book by contact name.
        :param contact_name: str
        :param new_phone_number: int
        :return: None
        """
        db.update_record_in_phone_book(self._con_name,
                                       (new_phone_number, contact_name))
