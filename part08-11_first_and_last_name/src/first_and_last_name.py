class Person:
    def __init__(self, fullname) -> None:
        self.name = fullname

    def return_first_name(self):
        return self.name.split(" ")[0]

    def return_last_name(self):
        return self.name.split(" ")[1]