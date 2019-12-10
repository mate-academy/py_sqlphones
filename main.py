"""user interface"""
import sqlcontacts


def dialog():
    """dialog with user"""
    phb = sqlcontacts.PhoneBook()
    while True:
        print("""What do you want to do?
c - create
r - read
u - update
d - delete
q - quit
""")
        action = input("Choose:").lower()
        if action == 'q':
            break
        if action == 'c':
            try:
                name = input("User name: ")
                phone = input("User phone: ")
                phb.create(name, phone)
            except KeyError:
                print("Name must be unique!\n")
            else:
                print("Done!\n")
        elif action == 'r':
            try:
                name = input("User name: ")
                print(f"Phone number: {phb.read(name)}")
            except KeyError:
                print("This name is not present in list\n")
        elif action == "u":
            name = input("User name: ")
            phone = input("Phone: ")
            phb.update(name, phone)
            print("Successful!\n")
        elif action == "d":
            name = input("User name: ")
            phb.delete(name)
            print("Successful!\n")


if __name__ == "__main__":
    dialog()
