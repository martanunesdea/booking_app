# Entry point for using the database manager 
# This will temporarily host the development code for the database manager
# The fully-featured and tested code will at a later stage make up the module "db_manager"

import sqlite3

class DBHandler:
##
##    object variables:
##      connection handler
##      cursor
##    method variables:
##      table_name ??     
##

    def __init__(self):
        self._conn = sqlite3.connect('example.db')
        self._cursor = self._conn.cursor()

    def create_table(self, table_name, **kwargs):
        self._cursor.execute('''CREATE TABLE ? ''', table_name)
        print("Caught error")

    def add_row(self, table_name, *kargs):     
        self._cursor.execute('INSERT INTO ? VALUE ?', table_name, kargs)
    
    
    # def update_table(self, **kwargs):
        

    # def get_count(self, **kwargs):
        # outputs total count of rows in table

    def print_table(self, table_name, *kargs):
        for row in self._cursor.execute('SELECT * FROM ?', table_name):
            print(row)


def main():
    if test(): print("Status: OK")
    else: print("Status: NOK")



def test():
    ## methods to create and test
    my_db = DBHandler()
    if my_db: return True
    
    # TODO: add unit test
    my_db.create_table("users")
    
    # TODO: add unit test
    my_db.add_row("users", ["user1", "buy"])
    
    # TODO: add unit test
    my_db.print_table("users")

    # my_db.update_row(table_string, range params)
    # my_db.show_table(string table)
    # my_db.show_rows(string table, range rows)
    # my_db.delete()
    
        



if __name__ == "__main__": main()