# This file describes the concept of the timeslot within a calendar
# Timeslot requirements:
#   - A date: dd-mm-yyyy
#   - A state: "available" or "not available"
#   - An author: admin name
from user import * 

class Timeslot:
    def __init__(self, date, author, state = None, attendees = None, max_capacity = None):
        if date:
            self._date = date
        else:
            raise ArgumentError('Timeslot requires a specific date to be created')
        if author:
            self._author = author
        else:  
            raise ArgumentError('Timeslots requires a specific author to be created')
        if state != None:
            self._state = state
        else:
            self._state = "available"
        if attendees:
            self._attendees = attendess
        else:
            self._attendees = 0
        if max_capacity:
            self._capacity = max_capacity
        else:
            self._capacity = 1

    ### Set methods
    def set_date(self, date):
        self._date = date

    def set_author(self, author):
        raise ArgumentError("Changing author value is not permitted")

    def set_state(self, state):
        self._state = state

    def set_capacity(self, max_capacity):
        self._capacity = max_capacity

    ### Get methods
    def get_date(self):
        return self._date
        
    def get_author(self):
        return self._author

    def get_state(self):
        return self._state

    def get_capcity(self):
        return self._capacity

    ### Helper methods
    def __str__(self):
        return f''' 
                Date: {self._date} 
                Author: {self._author} 
                State: {self._state}
                Attendees: {self._attendees} 
                Capacity: {self._capacity}'''
    
    def get_details(self):
        print(f'Timeslot {self._date} created by {self._author} has {self._attendees} booking(s) and is {self._state}')

    def add_booking(self):
        self._attendees += 1
        ## check capacity is full
        if self._capacity == self._attendees:
            self._state = "fully booked"            

def main():
    my_author = Author(first_name = "maria", last_name = "pm")
    time1 = my_author.create_timeslot("10-09-2020", "available")
    time2 = my_author.create_timeslot("12-12-2020", "available")
    time1.get_details()
    time2.get_details()

    my_user = Client(first_name = 'marta', last_name = 'nunes')
    my_user.book_slot(time1)
    my_user.get_booked_slots()
    print(time1)
    bookings_total = my_author.get_bookings_created()
    print(bookings_total)

if __name__ == "__main__": main()