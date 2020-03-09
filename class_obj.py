# OOP

# syntax
'''
class ClassName (PrantClass)
    property
    method
'''
class Restaurant():
    # Global variable 
    name = ''
    owner = ''

    # self pass automatic
    def details(self):
        print(self.name, self.owner)

    def details_with_address(self, address):
        print(self.name, self.owner)
        print(address)

restaurant1 = Restaurant()

restaurant1.name = 'KFC'
restaurant1.owner = 'Shahriar'

restaurant1.details()
restaurant1.details_with_address('Dhaka')
print(type(restaurant1))


class Person:
    # constructor / magic method  
    def __init__(self, name, age):
        # attribute/prooerty/field var 
        self.name = name 
        self.age = age 

    def details(self):
        print(self.name, self.age, sep=' | ')
bill = Person('Bill', 55)
bill.details()
print(bill.name, bill.age)
