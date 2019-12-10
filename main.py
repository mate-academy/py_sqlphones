"""
Module with console based application
"""
import sqlcontacts


def user_interface():
    """
    Define options
    :return:
    """
    while True:
        print("""What do you want to do?
    c - create
    r - read
    u - update
    d - delete
    q - quit
    """)
        book = sqlcontacts.PhoneBook()
        action = input().lower()
        if action == 'c':
            print("Want to add a new contact? Please, print a name: ")
            name = input("Print name here: ")
            print("Now, please, fill the number: ")
            number = input("Print number here: ")
            book.create(name, number)
            print('Thank you!')
        elif action == 'r':
            print("Find a contact? Please, print a name: ")
            name = input("Print name here: ")
            book.read(name)
            print('Thank you!')
        elif action == 'u':
            print("OK. Please, print a contact name to update: ")
            name = input("Print name here: ")
            print("Now, please, update the number: ")
            number = input("Print number here: ")
            book.update(name, number)
            print('Thank you!')
        elif action == 'd':
            print("Contact is dead? Sorry... Please, print a name to delete: ")
            name = input("Print name here: ")
            book.delete(name)
            print('Thank you!')
        elif action == 'q':
            break
        elif action not in 'crudq':
            print('There is no such option, please try again!')
            continue


if __name__ == "__main__":
    user_interface()
