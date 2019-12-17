'''
This a console-based application
'''
import sqlcontacts


def main():
    '''
    :return:
    '''
    while True:
        print("""What do you want to do?
c - create
r - read
u - update
d - delete
q - quit
""")
        phone_book = sqlcontacts.PhoneBook()
        action = input("?").lower()
        if action == 'c':
            name = input("Input name:")
            number = input("Input number")
            print(phone_book.create(name, number))
        if action == 'r':
            name = input("Input name:")
            print(phone_book.read(name))
        if action == 'u':
            name = input("Input name:")
            number = input("Input number")
            print(phone_book.update(name, number))
        if action == 'd':
            name = input("Input name:")
            print(phone_book.delete(name))
        if action == 'q':
            break


if __name__ == "__main__":
    main()
