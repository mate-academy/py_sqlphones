"""Module sqlcontacts"""


import _sqlite3


class PhoneBook:
    """Class PhoneBook"""
    def __init__(self):
        self.database = _sqlite3.connect(":memory:")
        self.database.execute("""
        create table phonebook (
        id integer primary key,
        name varchar(10),
        phone int
        )""")

    def create(self, name, phone):
        """Create new name and phone"""
        self.database.execute("""insert into phonebook \
            (name, phone) values (?, ?)""", (name, phone))

    def read(self, name):
        """Read phone number"""
        cur = self.database.execute("""select name, phone \
        from phonebook where name=?""", (name,))
        try:
            return cur.fetchone()[1]
        except TypeError:
            raise KeyError

    def update(self, name, phone):
        """Update phone number"""
        cur = self.database.execute("""select name \
                from phonebook where name=?""", (name,))
        if not cur:
            raise KeyError
        self.database.execute("""update phonebook set phone=? \
         where name=?""", (phone, name))

    def delete(self, name):
        """Delete name"""
        self.database.execute("delete from phonebook where name=?", (name,))
