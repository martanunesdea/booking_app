# Entry point for using the database manager 
# This will temporarily host the development code for the database manager
# The fully-featured and tested code will at a later stage make up the module "db_manager"

import sqlite3

def main():
    my_conn = connect()
    
    ##
    ## test that my_conn is operational
    ##

    c = my_conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    my_conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close() 

def connect():
    conn = sqlite3.connect('example.db')
    return conn

if __name__ == "__main__": main()