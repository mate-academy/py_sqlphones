'''
This a console-based application
'''
import sqlite3


class PhoneBook:
    '''
    Class for working only with phone book db
    Have methods:
        save(), create(name, phone), read(name),
        update(name, phone), delete(name)
    '''
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE phone_data
                          (Name_contact text, Number_contact text)""")

    def create(self, name, phone):
        '''Create new contact and save in db'''
        sql = "SELECT * FROM phone_data WHERE Name_contact=?"
        self.cursor.execute(sql, (name,))
        if self.cursor.fetchall() == []:
            sql_insert = "INSERT INTO phone_data VALUES (?, ?)"
            self.cursor.execute(sql_insert, (name, phone))
            return "create contact"
        raise KeyError

    def read(self, name):
        '''Read contact from db'''
        sql = "SELECT * FROM phone_data WHERE Name_contact=?"
        self.cursor.execute(sql, (name,))
        if self.cursor.fetchone() != None:
            sql_read = "SELECT Number_contact FROM phone_data " \
                       "WHERE Name_contact=?"
            self.cursor.execute(sql_read, (name,))
            return int(self.cursor.fetchall()[0][0])
        raise KeyError

    def update(self, name, phone):
        '''Update contact adn save in db'''
        sql = "SELECT * FROM phone_data WHERE Name_contact=?"
        self.cursor.execute(sql, (name,))
        if self.cursor.fetchall() != []:
            sql_update = """UPDATE phone_data SET Number_contact = ?
             WHERE Name_contact = ? """
            self.cursor.execute(sql_update, (phone, name))
            return "Update phone number"
        raise KeyError

    def delete(self, name):
        '''Delete contact and save db'''
        sql = "SELECT * FROM phone_data WHERE Name_contact=?"
        self.cursor.execute(sql, (name,))
        if self.cursor.fetchall() != []:
            sql_delete = """DELETE FROM phone_data WHERE Name_contact=?"""
            self.cursor.execute(sql_delete, (name,))
            return "Delete phone number"
        raise KeyError
