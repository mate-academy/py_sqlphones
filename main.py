"""module for working with user interface"""
import sqlcontacts


def main():
    """main function"""
    phone_book = sqlcontacts.PhoneBook()
    while True:
        print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit
    """)
        action = input("?").lower()
        if action == 'q':
            break
        if action == 'c':
            name = input("Name: ")
            number = input("Number: ")
            print(phone_book.create(name, number))
        if action == "r":
            name = input("Name: ")
            print(phone_book.read(name))
        if action == "u":
            name = input("Name: ")
            number = input("Number: ")
            print(phone_book.update(name, number))
        if action == "d":
            name = input("Name: ")
            print(phone_book.delete(name))


if __name__ == "__main__":
    main()
