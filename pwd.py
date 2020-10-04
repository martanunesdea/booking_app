# File describing the class Password

class Pwd:
    def __init__(self, user, key, date):
        self._user = user
        self._key = key
        self._date = date
    
    def __str__(self):
        return f'User {self._user} was created in {self._date}'
     

def main():
    try: 
        test() 
    except: 
        print("Test didn't complete")


def test():
    password = Pwd("marta", "hello123", "2020-10-02")
    print(password)



if __name__ == "__main__": main()