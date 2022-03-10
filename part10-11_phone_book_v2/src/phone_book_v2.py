from unicodedata import name

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)

        self.__persons[name].add_address(address)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()

    def get_address(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()   

    def all_entries(self):
        return self.__persons

class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def add_address(self, address: str):
        self.__address = address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        address = self.__phonebook.get_address(name)
        if numbers == None or numbers == []:
            print("number unknown") 
        else:
            for number in numbers:
                print(number)
        if address == None:
            print("address unknown")
        else:
            print(address)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)      

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

"""
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def add_number(self, number: str):
        self.__numbers.append(number)

    def address(self):
        return self.__address

    def add_address(self, address: str):
        self.__address = address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons
 
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        data = self.__phonebook.get_numbers(name)
        if data==None:
            print("number unknown")
            print("address unknown")
            return
        numbers = data.numbers()
        if len(numbers)==0:
            print("number unknown") 
        else: 
            for number in numbers:
                print(number)
        address = data.address()
        if address!=None:
            print(address)
        else:
            print("address unknown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
"""