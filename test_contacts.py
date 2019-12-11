import pytest
import sqlcontacts

p = sqlcontacts.PhoneBook()

def test_create():
    p.create("Bill", 911)
    assert p.read('Bill') == 911
    p.delete("Bill")


def test_update():
    p.create("Bill", 911)
    p.update("Bill", 112)
    assert p.read('Bill') == 112
    p.delete("Bill")


def test_delete():
    p.create("Bill", 911)
    p.delete("Bill")
    with pytest.raises(KeyError):
        p.read('Bill')
