# File describing the class Password


class User:
    def __init__(self, **kwargs):
        self._first_name = kwargs['first_name'] if 'first_name' in kwargs else 'example'
        self._last_name = kwargs['last_name'] if 'last_name' in kwargs else 'example'

    def set_user_name(self, first_name, last_name):
        if first_name == 0 and last_name == 0:
            raise ArgumentError(f'Expected at least one argument to set the name of the user ')
        if first_name: # if argument is filled, set first name to that
            self._first_name = first_name
        if last_name:
            self._last_name = last_name
        return self._first_name + ' ' + self._last_name

    def get_user_name(self):
        return self._first_name + ' ' + self._last_name

    def __str__(self):
        return f'User is {self._first_name} {self._last_name}'
     

def main():
    if test():
        print("Test passed")
    else: 
        print("Test didn't pass")
    

def test():
    my_user = User(first_name = 'marta', last_name = 'nunes')
    print(my_user)
    return True


if __name__ == "__main__": main()