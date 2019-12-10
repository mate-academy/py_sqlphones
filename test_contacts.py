import db_func as db
import sqlcontacts

con = "phonebook.sqllite"
db.create_db(con)
phone = sqlcontacts.PhoneBook(con)


def test_create():
    phone.create_new_record(1, "Bill", 911)
    assert phone.get_phone_by_name('Bill') == [(911,)]


def test_update():
    phone.create_new_record(2, "Bill2", 912)
    phone.update_record_by_name("Bill2", 112)
    assert phone.get_phone_by_name('Bill2') == [(112,)]


def test_delete():
    phone.create_new_record(3, "Bill3", 913)
    phone.remove_record_by_name("Bill3")
    assert phone.get_phone_by_name('Bill3') == []
