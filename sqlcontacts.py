"""use sqlLite"""
import _sqlite3


class PhoneBook:
    """phone book with sqlLite"""
    def __init__(self):
        self.conn = _sqlite3.connect(":memory:")
        self.curs = self.conn.cursor()
        self.curs.execute('CREATE TABLE IF NOT EXISTS phone_book'
                          '(name VARCHAR(30) PRIMARY KEY ,'
                          ' phone INTEGER NOT NULL ) ')

    def create(self, name, phone):
        """add new user into book"""
        try:
            self.curs.execute('INSERT INTO phone_book'
                              ' (name, phone) values (?, ?)', (name, phone))
            self.conn.commit()
        except _sqlite3.IntegrityError:
            raise KeyError

    def read(self, name):
        """return phone number"""
        try:
            self.curs.execute('SELECT phone '
                              'FROM phone_book WHERE name=?', (name,))
            return self.curs.fetchone()[0]
        except TypeError:
            raise KeyError

    def update(self, name, phone):
        """update phone"""
        self.curs.execute('UPDATE phone_book '
                          'SET phone=? WHERE name=?', (phone, name))
        self.conn.commit()

    def delete(self, name):
        """delete user"""
        self.curs.execute('DELETE FROM phone_book WHERE name=?', (name,))
        self.conn.commit()
