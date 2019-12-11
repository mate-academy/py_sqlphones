"""Main module to work with user's input"""
import sqlcontacts


def dialog():
    """Dialog with the user
    for creating, updating and reading phone book
    """
    phone_book = sqlcontacts.PhoneBook()
    while True:
        action = input(
            """What do you want to do?
            c - create
            r - read
            u - update
            d - delete
            q - quit""")
        action.lower()
        if action == 'c':
            name = input('Please, enter the name')
            phone = int(input('Please, enter the phone'))
            phone_book.create(name, phone)
            print('Success!')
        elif action == 'r':
            name = input('Please, enter the name')
            print(phone_book.read(name))
        elif action == 'u':
            name = input('Please, enter the name')
            phone = int(input('Please, enter the phone'))
            phone_book.update(name, phone)
            print('Contact was updated!')
        elif action == 'd':
            name = input('Please, enter the name')
            phone_book.delete(name)
            print('Contact was deleted!')
        elif action == 'q':
            break


if __name__ == '__main__':
    dialog()
