import contacts


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