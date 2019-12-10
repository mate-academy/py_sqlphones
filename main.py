"""Dialog realisation with user"""
import sqlcontacts


def dialog():
    """dialog with user"""
    phone_book = sqlcontacts.PhoneBook()
    while True:
        print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit""")
        action = input("?").lower()
        if action == 'c':
            name = input("Input new contact name \n")
            phone = input("Input the phone \n")
            phone_book.create(name, phone)
        elif action == 'r':
            name = input("Input the contact name \n")
            print(phone_book.read(name))
        elif action == 'u':
            name = input("Input the contact name \n")
            phone = input("Input new phone \n")
            phone_book.update(name, phone)
        elif action == 'd':
            name = input("Input the contact name for deleting \n")
            phone_book.delete(name)
        elif action == 'q':
            break


if __name__ == "__main__":
    dialog()
