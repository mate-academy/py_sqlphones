import _sqlite3


class PhoneBook:
    def __init__(self):
        self.database = _sqlite3.connect(":memory:")
        self.database.execute("""
        create table phonebook (
        id integer primary key,
        name varchar(10),
        phone int
        )""")

    def create(self, name, phone):
        self.database.execute("insert into phonebook (name, phone) values (?, ?)", (name, phone))

    def read(self, name):
        c = self.database.execute("select name, phone from phonebook where name=?", (name,))
        try:
            return c.fetchone()[1]
        except TypeError:
            raise KeyError

    def update(self, name, phone):
        self.database.execute("update phonebook set phone=? where name=?", (phone, name))

    def delete(self, name):
        self.database.execute("delete from phonebook where name=?", (name,))
