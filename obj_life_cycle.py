# object life cycle 
class X:
    def __init__(self, name):
        self.name = name 
        print(self.name + ' created')
    # garbase collection 
    def __del__(self):
        print(self.name + ' is destroyed')

# uncomment this to check lifecycle 
x = X('x')
y = X('y')
#print("Hello World")