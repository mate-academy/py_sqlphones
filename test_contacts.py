"""
Test module.
"""

from db_func import PhoneBookDatabase
from sqlcontacts import PhoneBook

CON_NAME = "phonebook.sqllite"
PhoneBookDatabase.create_db(con_name=CON_NAME)
PHONE = PhoneBook(con_name=CON_NAME)


def test_create():
    """
    Test creation record in database.
    :return: bool
    """
    PHONE.create_new_record(1, "Bill", 911)
    assert PHONE.get_phone_by_name('Bill') == [(911,)]


def test_update():
    """
    Test record update in database.
    :return: bool
    """
    PHONE.create_new_record(2, "Bill2", 912)
    PHONE.update_record_by_name("Bill2", 112)
    assert PHONE.get_phone_by_name('Bill2') == [(112,)]


def test_delete():
    """
    Test record deletion in database.
    :return: bool
    """
    PHONE.create_new_record(3, "Bill3", 913)
    PHONE.remove_record_by_name("Bill3")
    assert PHONE.get_phone_by_name('Bill3') == []
