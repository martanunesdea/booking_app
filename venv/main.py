# Entry point for using the database manager 
# This will temporarily host the development code for the database manager
# The fully-featured and tested code will at a later stage make up the module "db_handler"

from db_handler import *
from user import * 
from timeslot import *

def main():
    my_author = Author(first_name = 'maria', last_name = 'pm')
    time1 = my_author.create_timeslot(date(2020, 10, 12), 'available')
    my_user = Client(first_name = 'marta', last_name = 'nunes')
    my_user.book_slot(time1)

    my_db = DBHandler()
    
    # On program startup, bootloader will create all tables necessary for execution
    # TODO: add ifdef-type conditional for bootloader mode 
    #my_db.bootloader() 
   
    #my_db.update(time1, my_author, my_user)
    users_list = my_db.get_users() # print separately as these are different tables    
    my_db.print_bookings()    


if __name__ == "__main__": main()