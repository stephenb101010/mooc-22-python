# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    subordinates = 0
    for emp in employee.subordinates:
        subordinates += 1
        subordinates += count_subordinates(emp)
    return subordinates

"""
def count_subordinates(employee: Employee):
    if employee is None:
        return 0
    no_of_subordinates = 0
    for subordinate in employee.subordinates:
        no_of_subordinates += count_subordinates(subordinate)+1
    return no_of_subordinates
"""