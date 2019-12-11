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
        try:
            if action == 'q':
                break
            if action == 'c':
                name = input("Name: ")
                number = input("Number: ")
                phone_book.create(name, number)
                print("Added")
            elif action == "r":
                name = input("Name: ")
                print(phone_book.read(name))
            elif action == "u":
                name = input("Name: ")
                number = input("Number: ")
                phone_book.update(name, number)
                print("Updated")
            elif action == "d":
                name = input("Name: ")
                phone_book.delete(name)
                print("Deleted")
            else:
                print("Incorrect action.Try again")
        except KeyError:
            print("Number not in phone book or number must be unique")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
