"""
Model
"""
from db_func import PhoneBookDatabase


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
        return PhoneBookDatabase.get_all_records_from_pb(self._con_name)

    def get_phone_by_name(self, contact_name):
        """
        Get phone information by contact name.
        :param contact_name: str
        :return: int
        """
        return PhoneBookDatabase.get_phone_from_pb(self._con_name,
                                                   (contact_name,))

    def create_new_record(self, record_id, new_cont_name, new_cont_phone):
        """
        Add a new record to the phone book that avoids to add duplicates.
        :param new_cont_name: str
        :param new_cont_phone: int
        :return: None
        """
        PhoneBookDatabase.add_new_record_to_db(self._con_name,
                                               (record_id, new_cont_name,
                                                new_cont_phone))

    def remove_record_by_name(self, contact_name):
        """
        Remove record from phone book by contact name.
        :param contact_name: str
        :return: None
        """
        PhoneBookDatabase.delete_record_from_pb(self._con_name,
                                                (contact_name,))

    def update_record_by_name(self, contact_name, new_phone_number):
        """
        Update record in phone book by contact name.
        :param contact_name: str
        :param new_phone_number: int
        :return: None
        """
        PhoneBookDatabase.update_record_in_pb(self._con_name,
                                              (new_phone_number, contact_name))
