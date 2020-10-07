# This file describes the concept of "Calendar"
# It will store all the timeslots instances in a dictionary struct

from datetime import date

class Calendar:
    def __init__(self):
        self._all_slots = {'':0}
    
    def add_slot(self, slot):
        self._all_slots.update( {'id':0, 'instance': slot})

    def get_slot(self, slot):
        return self._all_slots['instance':slot]


def main():
    cal1 = Calendar()
    cal1.add_slot(date(2020, 10, 9))


if __name__ == "__main__": main()