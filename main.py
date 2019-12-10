"""
For py_phones (https://github.com/mate-academy/py_phones)
create a new sqlcontacts module.
In this module, you must provide the ability to work with
data in a SQLite database. main.py should be left unchanged,
except for importing and creating the class.

Для py_phones ( https://github.com/mate-academy/py_phones )
создайте новый модуль sqlcontacts. В этом модуле вы должны
предоставить возможность работать с данными в базе данных SQLite.
main.py следует оставить без изменений, за исключением импорта
и создания класса.
"""

# import contacts
import sqlcontacts


def interface():
    """Phone interface"""
    # phone_book = contacts.PhoneBook()
    phone_book = sqlcontacts.PhoneBook()

    while True:
        print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit
    """)
        funcs = {'c': create, 'r': read, 'u': update}
        action = input("?").lower()

        if action == 'q':
            break

        funcs.get(action, 'You enter wrong command')(phone_book)


def create(phone_book):
    """Create new name"""
    name = input('Please enter new name: ')
    phone = input('Please enter phone number: ')
    phone_book.create(name, phone)


def read(phone_book):
    """Read phone number """
    name = input('Please enter name: ')
    phone_book.read(name)


def update(phone_book):
    """Update phone number"""
    name = input('Please enter name (update): ')
    phone = input('Please enter phone number: ')
    phone_book.update(name, phone)


if __name__ == '__main__':
    interface()
