# File describing the class Password

class Pwd:
    def __init__(self, password_entry, account, date):
        self._password = password_entry
        self._account = account
        self._date = date
    
    def __str__(self):
        return f'Account {self._account} had a password set in {self._date}'
     

def main():
    try: 
        test() 
    except: 
        print("Test didn't complete")


def test():
    password = Pwd("pass12345", "amazon", "2020-10-02")
    print("adding password...")
    print(password)



if __name__ == "__main__": main()