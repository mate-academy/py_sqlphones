"""
Controller
"""
from interface import Interface
from sqlcontacts import PhoneBook


def main_menu():
    """
    Main function where we create menu and receive input.
    :return: None
    """
    phone_book = PhoneBook()
    interface = Interface(phone_book)
    try:
        while True:
            selection = input("""
----MAIN MENU----
1: Get all data from phone book
2: Create a new record to phone book
3: Update phone book record by using contact name
4: Delete phone book record by using contact name
5: Get phone number by using contact name
6: Logout
Please enter your choice: """)

            if selection == '1':
                print(phone_book.get_all_data())
            elif selection == '2':
                interface.add_record_by_user_input()
            elif selection == '3':
                interface.update_record_by_user_input()
            elif selection == '4':
                interface.remove_record_by_user_input()
            elif selection == '5':
                interface.get_phone_by_user_input()
            elif selection == '6':
                break
            else:
                print("I don't know what you try to tell me")
    except KeyboardInterrupt:
        print("As you wish...")


if __name__ == "__main__":
    main_menu()
