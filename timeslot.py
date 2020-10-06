# This file describes the concept of the timeslot within a calendar
# Timeslot requirements:
#   - A date: dd-mm-yyyy
#   - A state: "available" or "not available"
#   - An author: admin name


class Timeslot:
    def __init__(self, date, author, state = None):
        self._date = date
        self._author = author
        if state != None:
            self._state = state



def main():
    time1 = Timeslot(10, "marta", "available")


if __name__ == "__main__": main()