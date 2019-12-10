"""
tests docstring
"""
import pytest
import sqlcontacts


def test_create():
    """

    :return:
    """
    phone_b = sqlcontacts.PhoneBook()
    phone_b.create("Bill", 911)
    assert phone_b.read('Bill') == 911


def test_update():
    """

    :return:
    """
    phone_b = sqlcontacts.PhoneBook()
    phone_b.create("Bill", 911)
    phone_b.update("Bill", 112)
    assert phone_b.read('Bill') == 112


def test_delete():
    """

    :return:
    """
    phone_b = sqlcontacts.PhoneBook()
    phone_b.create("Bill", 911)
    phone_b.delete("Bill")
    with pytest.raises(KeyError):
        phone_b.read('Bill')
